import math
import renpy.exports as renpy
import renpy.config as config
import pygame
import entities
import tiles
import utils
import game_data

game_screen = None
game = None

# Callback for loading. Repairs broken voice->weapon references.
def repair_weapon_references():
    global game

    for weapon in game.all_weapons.sprites():
        weapon.wielder.weapon = weapon

class MentalControlGame:
    def __init__(self):
        global game

        self.all_entities = pygame.sprite.Group()
        self.all_voices = pygame.sprite.Group()
        self.all_projectiles = pygame.sprite.Group()
        self.all_weapons = pygame.sprite.Group()

        self.all_tiles, self.all_walls = tiles.load_map_image()

        self.player = entities.Player(self, (0, 0))
        self.pyro = entities.Pyromaniac(self, (50, 50))
        self.survivor = entities.Survivor(self, (100, 100))
        self.artist = entities.Artist(self, (150, 150))

        self.force_combat_winner = None
        self.allow_clickfwd = False
        self.combat_in_progress = False
        self.ai_active = False
        self.__screen_center = None

        game = self
        game_data.game = self

    def __new__(cls):
        global game

        i = super(MentalControlGame, cls).__new__(cls)

        game = i
        game_data.game = i

        return i

    def __getstate__(self):
        return {
            'screen_center': self.__screen_center,
            'allow_clickfwd': self.allow_clickfwd,
            'combat_in_progress': self.combat_in_progress,
            'ai_active': self.ai_active,
            'force_combat_winner': self.force_combat_winner,
            'projectiles': self.all_projectiles.sprites(),
            'weapons': self.all_weapons.sprites(),
            'tiles': self.all_tiles.sprites(),
            'player': self.player,
            'pyro': self.pyro,
            'survivor': self.survivor,
            'artist': self.artist,
        }

    def __setstate__(self, state):
        global game

        game = self
        game_data.game = self

        self.__screen_center = state['screen_center']
        self.allow_clickfwd = state['allow_clickfwd']
        self.combat_in_progress = state['combat_in_progress']
        self.ai_active = state['ai_active']
        self.force_combat_winner = state['force_combat_winner']

        self.all_entities = pygame.sprite.Group()
        self.all_voices = pygame.sprite.Group()
        self.all_projectiles = pygame.sprite.Group()
        self.all_weapons = pygame.sprite.Group()
        self.all_tiles = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()

        self.player = state['player']
        self.pyro = state['pyro']
        self.survivor = state['survivor']
        self.artist = state['artist']

        self.all_voices.add(self.player, self.pyro, self.survivor, self.artist)

        for weapon in state['weapons']:
            #weapon.wielder.weapon = weapon # repair possibly broken reflinks
            self.all_weapons.add(weapon)

        self.all_projectiles.add(iter(state['projectiles']))

        self.all_entities.add(
            iter(self.all_voices),
            iter(self.all_weapons),
            iter(self.all_projectiles),
        )

        for tile in state['tiles']:
            self.all_tiles.add(tile)

            if tile.is_wall:
                self.all_walls.add(tile)

        for sprite in self.all_entities.sprites():
            sprite.game = self


    def screen_center(self):
        if self.__screen_center is None:
            return self.player.pos
        else:
            return self.__screen_center

    def set_screen_center(self, center=None):
        self.__screen_center = center

    def voices_alive(self):
        n = 0
        for voice in self.all_voices.sprites():
            if voice.alive():
                n += 1
        return n

    def get_winning_voice(self):
        if self.voices_alive() != 1:
            return None

        if self.force_combat_winner is not None:
            return self.force_combat_winner

        for voice in self.all_voices.sprites():
            if voice.alive():
                return voice.id

    def voice_by_id(self, id):
        if id == 'calm' or id == 'player':
            return self.player
        elif id == 'surv' or id == 'survivor':
            return self.survivor
        elif id == 'pyro':
            return self.pyro
        elif id == 'artist':
            return self.artist
        else:
            raise IndexError("No such voice with id: "+str(id))

    def update(self, dt):
        if dt > (1.0 / 10.0):
            return

        self.all_entities.update(dt)

        for entity in self.all_entities.sprites():
            entity.set_render_viewpoint()

        for voice, walls in pygame.sprite.groupcollide(self.all_voices, self.all_walls, False, False).items():
            for wall in walls:
                mvt = voice.check_collision(wall)
                if mvt is not None:
                    voice.pos[0] += mvt[0]
                    voice.pos[1] += mvt[1]

        for voice, colliding_voices in pygame.sprite.groupcollide(self.all_voices, self.all_voices, False, False).items():
            for colliding_voice in colliding_voices:
                if voice.alive() and colliding_voice.alive() and voice.surf_alpha > 16 and colliding_voice.surf_alpha > 16 and voice != colliding_voice:
                    mvt = voice.check_collision(colliding_voice)
                    if mvt is not None:
                        voice.pos[0] += mvt[0]
                        voice.pos[1] += mvt[1]

        for voice, weapons in pygame.sprite.groupcollide(self.all_voices, self.all_weapons, False, False).items():
            for weapon in weapons:
                if voice != weapon.wielder and voice.alive() and self.combat_in_progress and weapon.active and weapon.can_damage and weapon.is_melee:
                    if voice.check_collision(weapon) is not None:
                        weapon.deal_damage(voice)


class ControlGameDisplay(renpy.Displayable):
    def __init__(self, **kwargs):
        global game_screen, game

        super(ControlGameDisplay, self).__init__(**kwargs)

        game_screen = self
        game_data.game_screen = self

        self.primary_surf = None
        self.bg_surf = None

        self.last_st = 0
        self.screen_sz = None

    def __getstate__(self):
        d = renpy.Displayable.__getstate__(self)
        d.update({
            'last_st': self.last_st,
            'screen_sz': self.screen_sz
        })

        if 'primary_surf' in d:
            del d['primary_surf']

        if 'bg_surf' in d:
            del d['bg_surf']

        print("CtrlGameDisplay state keys: "+str(d.keys()))

        return d

    def __setstate__(self, state):
        renpy.Displayable.__setstate__(self, state)

        self.last_st = state['last_st']
        self.screen_sz = state['screen_sz']

        self.primary_surf = None
        self.bg_surf = None

    def event(self, ev, x, y, st):
        global game

        if (ev.type == pygame.MOUSEMOTION or abs(game.player.vel[0]) + abs(game.player.vel[1]) > 0) and self.screen_sz is not None:
            # convert mouse pos to field coordinates:
            ctr = game.screen_center()

            m_pos = [
                (
                    (ctr[0] - (game_data.gameplay_screen_size[0] / 2))
                    + (x * game_data.gameplay_screen_size[0] / self.screen_sz[0])
                ),
                (
                    (ctr[1] - (game_data.gameplay_screen_size[1] / 2))
                    + (y * game_data.gameplay_screen_size[1] / self.screen_sz[1])
                )
            ]

            game.player.mouse_update(m_pos)

        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            game.player.weapon.fire()

        if game.combat_in_progress and (game.voices_alive() == 1):
            return True

    def update_tiles(self, center):
        global game

        if self.bg_surf is None:
            self.bg_surf = pygame.Surface(game_data.field_size).convert()
            game.all_tiles.draw(self.bg_surf)

        r = pygame.Rect((0, 0), game_data.gameplay_screen_size)

        r.centerx = center[0]
        r.centery = center[1]

        if r.x < 0:
            r.x = 0
        elif r.x > game_data.field_size[0] - game_data.gameplay_screen_size[0]:
            r.x = game_data.field_size[0] - game_data.gameplay_screen_size[0]

        if r.y < 0:
            r.y = 0
        elif r.y > game_data.field_size[1] - game_data.gameplay_screen_size[1]:
            r.y = game_data.field_size[1] - game_data.gameplay_screen_size[1]

        offset = (r.centerx - center[0], r.centery - center[1])

        return self.bg_surf.subsurface(r), offset

    def render(self, width, height, st, at):
        global game

        render = renpy.Render(width, height)

        self.screen_sz = (width, height)

        # update game state
        dt = st - self.last_st
        self.last_st = st

        game.update(dt)

        surf = render.canvas().get_surface()
        surf.fill((0, 0, 0))

        ctr = game.screen_center()

        tiles_surf, offset = self.update_tiles(ctr)

        if self.primary_surf is None:
            self.primary_surf = pygame.Surface(game_data.gameplay_screen_size).convert()

        self.primary_surf.fill((0, 0, 0, 0))
        self.primary_surf.blit(tiles_surf, offset)

        for entity in game.all_entities.sprites():
            entity.set_render_viewpoint(ctr)

        game.all_entities.draw(self.primary_surf)

        pygame.transform.scale(
            self.primary_surf, self.screen_sz, surf
        )

        renpy.redraw(self, 1/60)
        return render
