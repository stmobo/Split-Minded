import math
import renpy.exports as renpy
import renpy.config as config
import pygame
import entities
import tiles
import utils
import game_data

allow_clickfwd = False
game_displayable = None  # a reference to the main MentalControlGame instance

player = None
pyro = None
survivor = None
artist = None

initialized = False

def on_load(voice_in_control):
    for voice in entities.all_voices.sprites():
        voice.pos = list(voice.default_spawn_point)
        voice.set_health(voice.max_health)

def init():
    global player, pyro, survivor, artist, initialized

    initialized = True

    entities.init()
    tiles.init()

    player = entities.Player((0, 0))
    pyro = entities.Pyromaniac((50, 50))
    survivor = entities.Survivor((100, 100))
    artist = entities.Artist((150, 150))

def screen_center():
    if game_data.screen_center is None:
        return player.pos
    else:
        return game_data.screen_center

def set_screen_center(center=None):
    game_data.screen_center = center

def voices_alive():
    n = 0
    for voice in entities.all_voices.sprites():
        if voice.alive():
            n += 1
    return n

def get_winning_voice():
    if voices_alive() != 1:
        return None

    if game_data.force_combat_winner is not None:
        return game_data.force_combat_winner

    for voice in entities.all_voices.sprites():
        if voice.alive():
            return voice.id


class MentalControlGame(renpy.Displayable):
    def __init__(self, **kwargs):
        super(MentalControlGame, self).__init__(**kwargs)
        game_displayable = self

        self.last_st = 0
        self.primary_surf = pygame.Surface(game_data.gameplay_screen_size)
        self.screen_sz = None

    def event(self, ev, x, y, st):
        if (ev.type == pygame.MOUSEMOTION or abs(player.vel[0]) + abs(player.vel[1]) > 0) and self.screen_sz is not None:
            # convert mouse pos to field coordinates:
            ctr = screen_center()
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

            player.mouse_update(m_pos)
            #renpy.redraw(self, 0)

        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            player.weapon.fire()

        if game_data.combat_in_progress and game_data.skip_combat and game_data.force_combat_winner is not None:
            return True

        if game_data.combat_in_progress and (voices_alive() == 1):
            return True

    def render(self, width, height, st, at):
        render = renpy.Render(width, height)

        self.screen_sz = (width, height)

        # update game state
        dt = st - self.last_st
        self.last_st = st

        if dt < (1.0 / 10.0):
            entities.all_entities.update(dt)

        for entity in entities.all_entities.sprites():
            entity.set_render_viewpoint()

        #renpy.log("Checking for voice/wall collisions...")
        for voice, walls in pygame.sprite.groupcollide(entities.all_voices, tiles.all_walls, False, False).items():
            #print("potential voice/wall collision detected for {}".format(voice.id))
            #if voice.id != 'calm':
            #    continue

            for wall in walls:
                mvt = voice.check_collision(wall)
                if mvt is not None:
                    #print(mvt)
                    voice.pos[0] += mvt[0]
                    voice.pos[1] += mvt[1]

                    #voice.vel[0] = 0
                    #voice.vel[1] = 0

        #renpy.log("Checking for voice/voice collisions...")
        for voice, colliding_voices in pygame.sprite.groupcollide(entities.all_voices, entities.all_voices, False, False).items():
            for colliding_voice in colliding_voices:
                if voice.alive() and colliding_voice.alive() and voice.surf_alpha > 16 and colliding_voice.surf_alpha > 16 and voice != colliding_voice:
                    mvt = voice.check_collision(colliding_voice)
                    if mvt is not None:
                        voice.pos[0] += mvt[0]
                        voice.pos[1] += mvt[1]

                        #print(mvt)

                        #voice.vel[0] = 0
                        #voice.vel[1] = 0

        #renpy.log("Checking for voice/weapon collisions...")
        for voice, weapons in pygame.sprite.groupcollide(entities.all_voices, entities.all_weapons, False, False).items():
            for weapon in weapons:
                if voice != weapon.wielder and voice.alive() and game_data.combat_in_progress and weapon.active and weapon.can_damage and weapon.is_melee:
                    if voice.check_collision(weapon) is not None:
                        weapon.deal_damage(voice)

        surf = render.canvas().get_surface()
        surf.fill((0, 0, 0))

        ctr = screen_center()

        tiles_surf, offset = tiles.update_tiles(ctr)

        self.primary_surf.fill((0, 0, 0, 0))
        self.primary_surf.blit(tiles_surf, offset)

        for entity in entities.all_entities.sprites():
            entity.set_render_viewpoint(ctr)

        entities.all_entities.draw(self.primary_surf)

        pygame.transform.scale(
            self.primary_surf, self.screen_sz, surf
        )

        renpy.redraw(self, 1/60)
        return render
