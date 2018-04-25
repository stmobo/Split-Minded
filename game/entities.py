import math
import renpy.exports as renpy
import renpy.config as config
import collision_detection as cd
import pygame
import game_data
import effects
import utils

all_entities = None
all_voices = None
all_projectiles = None
all_weapons = None

pyro_spawned = False
survivor_spawned = False
player_spawned = False
artist_spawned = False


def init():
    global all_entities, all_voices, all_projectiles, all_weapons

    for group in [all_entities, all_voices, all_projectiles, all_weapons]:
        if group is not None:
            group.empty()

    all_entities = pygame.sprite.Group()
    all_voices = pygame.sprite.Group()
    all_projectiles = pygame.sprite.Group()
    all_weapons = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.pos = list(pos)
        self.vel = [0, 0]
        self.rot = 0

        all_entities.add(self)

        self.m_pos = pygame.mouse.get_pos()

        self.image = self.base_image
        self.rect = self.image.get_rect()

        self.surf_alpha = None
        self.update_hooks = []

    def add_effect(self, effect):
        self.update_hooks.append(effect)

    def set_surface_alpha(self, alpha):
        if alpha is None:
            self.surf_alpha = None
        else:
            alpha = int(alpha)
            if alpha > 255:
                self.surf_alpha = 255
            elif alpha < 0:
                self.surf_alpha = 0
            else:
                self.surf_alpha = alpha

    def set_render_viewpoint(self, center=None):
        self.rect = self.image.get_rect()

        if center is None:
            self.rect.centerx = self.pos[0]
            self.rect.centery = self.pos[1]
        else:
            self.rect.centerx = int(
                (game_data.gameplay_screen_size[0] / 2)
                + self.pos[0]
                - center[0]
            )

            self.rect.centery = int(
                (game_data.gameplay_screen_size[1] / 2)
                + self.pos[1]
                - center[1]
            )

    def turn_to(self, point):
        self.rot = math.atan2(point[1] - self.pos[1], point[0] - self.pos[0])

    def update(self, dt, acc=(0, 0)):
        if type(self.vel) == tuple:
            self.vel = list(self.vel)

        self.vel[0] += acc[0] * dt
        self.vel[1] += acc[1] * dt

        self.last_pos = [self.pos[0], self.pos[1]]

        if type(self.pos) == tuple:
            self.pos = list(self.pos)

        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt

        i = 0
        while i < len(self.update_hooks):
            v = self.update_hooks[i](self, dt, acc)  # call hook
            if not v: # if v is False or None then remove the hook
                del self.update_hooks[i]
            else:
                i += 1

        self.image = pygame.transform.rotate(self.base_image, -math.degrees(self.rot))
        if self.surf_alpha is not None:
            alpha_img = pygame.Surface(self.image.get_rect().size, pygame.SRCALPHA)
            alpha_img.fill((255, 255, 255, self.surf_alpha))
            self.image.blit(alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


class Weapon(Entity):
    def __init__(self, wielder, image, mount_point=(35, 10), anchor_pt=(5, 40)):
        self.mount_point = mount_point
        self.anchor_pt = anchor_pt
        self.wielder = wielder

        self.base_image = pygame.image.load(renpy.file(image))

        self.active = True
        self.can_damage = False
        self.is_melee = False
        self.rot_offset = 0

        self.rotate_to_wielder()

        Entity.__init__(self, self.pos)

        all_weapons.add(self)

    def rotate_to_wielder(self):
        actual_anchor_pt = [
            (self.anchor_pt[0] * math.cos(self.rot_offset)) - (self.anchor_pt[1] * math.sin(self.rot_offset)),
            (self.anchor_pt[0] * math.sin(self.rot_offset)) + (self.anchor_pt[1] * math.cos(self.rot_offset)),
        ]

        offset = [
            float(self.mount_point[0] - actual_anchor_pt[0]),
            float(self.mount_point[1] - actual_anchor_pt[1])
        ]

        self.rot = self.wielder.rot + self.rot_offset
        rotated_offset = [
            (offset[0] * math.cos(self.wielder.rot)) - (offset[1] * math.sin(self.wielder.rot)),
            (offset[0] * math.sin(self.wielder.rot)) + (offset[1] * math.cos(self.wielder.rot)),
        ]

        self.pos = [
            self.wielder.pos[0] + rotated_offset[0],
            self.wielder.pos[1] + rotated_offset[1]
        ]

    def set_render_viewpoint(self, center=None):
        self.rotate_to_wielder()
        Entity.set_render_viewpoint(self, center)

    def fire(self):
        pass

    def deal_damage(self, victim):
        pass

    def update(self, dt, acc=(0, 0)):
        self.vel = [0, 0]
        self.rotate_to_wielder()

        if not self.active or not game_data.combat_in_progress or (self.wielder.surf_alpha is not None and self.wielder.surf_alpha == 0):
            self.set_surface_alpha(0)
        else:
            self.set_surface_alpha(None)

        Entity.update(self, dt, acc)


class Sword(Weapon):
    def __init__(self, wielder, damage=35):
        Weapon.__init__(self, wielder, 'weapons/sword.png', anchor_pt=(5, 60))

        self.swing_time = .125
        self.arc_angle = math.radians(90)
        self.damage = damage
        self.swing_increment = self.arc_angle / self.swing_time
        self.is_melee = True

        self.swinging = False
        self.controllable = True

    def fire(self):
        if not self.swinging and self.controllable:
            self.swinging = True
            self.can_damage = True
            self.rot_offset = -(self.arc_angle / 2)

    def deal_damage(self, victim):
        victim.set_health(victim.health - self.damage, self.wielder)
        self.can_damage = False

        victim.add_effect(effects.PushbackEffect(victim, self, .75, 250))

    def update(self, dt, acc=(0, 0)):
        if self.swinging:
            self.rot_offset += dt * self.swing_increment

            if self.rot_offset >= self.arc_angle / 2:
                self.rot_offset = 0
                self.swinging = False
                self.can_damage = False

        Weapon.update(self, dt, acc)


class Voice(Entity):
    def __init__(self, pos, image_folder, char_id):
        self.id = char_id

        self.char_images = {
            'default': pygame.image.load(renpy.file(image_folder+'/default.png')),
            'with_weapon': pygame.image.load(renpy.file(image_folder+'/with_weapon.png')),
        }

        self.base_image = self.char_images['default']

        self.health = 100
        self.max_health = 100
        self.default_spawn_point = (15 * game_data.tile_size, 15 * game_data.tile_size)
        self.invuln_time = 0.75

        Entity.__init__(self, pos)
        all_voices.add(self)

    def check_collision(self, other):
        polyA = cd.Rectangle(self.base_image.get_rect())
        polyB = cd.Rectangle(other.base_image.get_rect())

        polyA.rotate(self.rot)
        polyA.translate(self.pos)

        if other.rot is not None:
            polyB.rotate(other.rot)

        polyB.translate(other.pos)

        return cd.check_collision(polyA, polyB)

    def alive(self):
        return self.health > 0

    def set_health(self, health, attacker=None):
        damaged = health < self.health and health >= 0

        if health < self.health and self.invuln_time > 0:
            return

        if health <= 0:
            # make sure there's at least one voice left alive
            n_live_voices = 0

            for voice in all_voices.sprites():
                if voice.alive():
                    n_live_voices += 1

            if n_live_voices > 1:
                self.health = 0
                self.set_surface_alpha(0)
                #self.add_effect(effects.FadeEffect(self, 0.1, 255, 0))
        elif health > self.max_health:
            self.health = self.max_health
        else:
            self.health = health
            self.surf_alpha = None

        if damaged:
            self.invuln_time = 0.75
            self.add_effect(effects.BlinkEffect(self, 0.75, 128))
            self.on_damaged(attacker)

        #print("{} health now at {}".format(self.id, self.health))

    def turn_to(self, point):
        self.rot = math.atan2(point[1] - self.pos[1], point[0] - self.pos[0]) + (math.pi / 2)

    def on_damaged(self, attacker):
        pass

    def update(self, dt, acc=(0, 0)):
        if self.invuln_time > 0:
            self.invuln_time -= dt
        else:
            self.invuln_time = 0

        if game_data.combat_in_progress:
            self.base_image = self.char_images['with_weapon']
        else:
            self.base_image = self.char_images['default']

        Entity.update(self, dt, acc)


class AIVoice(Voice):
    def __init__(self, pos, image_folder, id):
        Voice.__init__(self, pos, image_folder, id)

        self.target = None

    def update(self, dt, acc=(0, 0)):
        if self.target is not None:
            self.turn_to(self.target.pos)

            if game_data.ai_active:
                self.vel = utils.magn_dir_vec(200, self.target.pos, self.pos)

                if not self.target.alive():
                    live_voices = []

                    for voice in all_voices.sprites():
                        if voice != self and voice.alive():
                            live_voices.append(voice)

                    if len(live_voices) == 0:
                        self.target = None
                    elif len(live_voices) == 1:
                        self.target = live_voices[0]
                    else:
                        self.target = renpy.random.choice(live_voices)
                else:
                    if utils.dist(self.pos, self.target.pos) < 50:
                        self.weapon.fire()

        Voice.update(self, dt, acc)


class Pyromaniac(AIVoice):
    def __init__(self, pos):
        global pyro_spawned

        if pyro_spawned and config.developer:
            raise RuntimeError("Attempted to spawn Pyromaniac twice!")
        pyro_spawned = True

        AIVoice.__init__(self, pos, 'voice2', 'pyro')

        self.weapon = Sword(self, 5)
        self.default_spawn_point = (4 * game_data.tile_size, 4 * game_data.tile_size)


class Survivor(AIVoice):
    def __init__(self, pos):
        global survivor_spawned

        if survivor_spawned and config.developer:
            raise RuntimeError("Attempted to spawn Survivor twice!")
        survivor_spawned = True

        AIVoice.__init__(self, pos, 'voice3', 'surv')

        self.weapon = Sword(self, 5)
        self.default_spawn_point = (26 * game_data.tile_size, 4 * game_data.tile_size)


class Artist(AIVoice):
    def __init__(self, pos):
        global artist_spawned

        if artist_spawned and config.developer:
            raise RuntimeError("Attempted to spawn Artist twice!")
        artist_spawned = True

        AIVoice.__init__(self, pos, 'voice4', 'artist')

        self.weapon = Sword(self, 5)
        self.default_spawn_point = (26 * game_data.tile_size, 27 * game_data.tile_size)


class Player(Voice):
    def __init__(self, pos):
        global player_spawned

        if player_spawned and config.developer:
            raise RuntimeError("Attempted to spawn Player twice!")
        player_spawned = True

        Voice.__init__(self, pos, 'voice1', 'calm')
        self.movement_allowed = False

        self.weapon = Sword(self)
        self.default_spawn_point = (3 * game_data.tile_size, 27 * game_data.tile_size)

        self.m_pos = (0, 0)

    def mouse_update(self, m_pos):
        self.m_pos = m_pos

    def update(self, dt):
        pressed = pygame.key.get_pressed()

        if self.movement_allowed:
            left = pressed[pygame.K_LEFT] or pressed[pygame.K_a]
            right = pressed[pygame.K_RIGHT] or pressed[pygame.K_d]
            up = pressed[pygame.K_UP] or pressed[pygame.K_w]
            down = pressed[pygame.K_DOWN] or pressed[pygame.K_s]
        else:
            left = right = up = down = False

        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            movement_magnitude = 120
        else:
            movement_magnitude = 300

        if left == right:
            self.vel[0] = 0
        elif left:
            self.vel[0] = -movement_magnitude
        elif right:
            self.vel[0] = movement_magnitude

        if up == down:
            self.vel[1] = 0
        elif up:
            self.vel[1] = -movement_magnitude
        elif down:
            self.vel[1] = movement_magnitude

        self.turn_to(self.m_pos)

        Voice.update(self, dt, (0, 0))
