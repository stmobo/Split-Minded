import math
import renpy.exports as renpy
import renpy.config as config
import collision_detection as cd
import pygame
import game_data
import effects
import utils

class Entity(pygame.sprite.Sprite):
    def __init__(self, game, pos):
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.pos = list(pos)
        self.vel = [0, 0]
        self.rot = 0

        game.all_entities.add(self)

        self.m_pos = pygame.mouse.get_pos()

        self.image = self.base_image
        self.rect = self.image.get_rect()

        self.surf_alpha = None
        self.update_hooks = []

    def __getstate__(self):
        return {
            'pos': self.pos,
            'vel': self.vel,
            'rot': self.rot,
            'surf_alpha': self.surf_alpha
        }

    def __setstate__(self, state):
        self.pos = list(state['pos'])
        self.vel = list(state['vel'])
        self.rot = state['rot']
        self.surf_alpha = state['surf_alpha']
        self.update_hooks = []

        if config.developer and self.base_image is None:
            raise NotImplementedError("base_image not set on unpickle")

        pygame.sprite.Sprite.__init__(self)

    def __new__(cls, *args, **kwargs):
        # set game attribute by default...
        i = super(Entity, cls).__new__(cls, *args, **kwargs)
        i.game = game_data.game

        return i

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
    def __init__(self, game, wielder, image, mount_point=(35, 10), anchor_pt=(5, 40)):
        self.mount_point = mount_point
        self.anchor_pt = anchor_pt
        self.__wielder = wielder

        self.base_image = pygame.image.load(renpy.file(image))

        self.active = True
        self.can_damage = False
        self.is_melee = False
        self.rot_offset = 0
        self.controllable = True

        self.rotate_to_wielder()

        Entity.__init__(self, game, self.pos)

        game.all_weapons.add(self)

    def __getstate__(self):
        d = Entity.__getstate__(self)
        d.update({
            'active': self.active,
            'can_damage': self.can_damage,
            'is_melee': self.is_melee,
            'controllable': self.controllable,
            'rot_offset': self.rot_offset,
            'mount_point': self.mount_point,
            'anchor_pt': self.anchor_pt,
            'wielder_id': self.wielder.id
        })

        return d

    def __setstate__(self, state):
        self.active = state['active']
        self.can_damage = state['can_damage']
        self.is_melee = state['is_melee']
        self.controllable = state['controllable']
        self.rot_offset = state['rot_offset']
        self.mount_point = state['mount_point']
        self.anchor_pt = state['anchor_pt']
        self.__wielder = state['wielder_id']

        Entity.__setstate__(self, state)

    def __getattr__(self, name):
        if name == 'wielder':
            if isinstance(self.__wielder, Voice):
                return self.__wielder
            elif isinstance(self.__wielder, str):
                return self.game.voice_by_id(self.__wielder)
        else:
            raise AttributeError("No attribute '"+str(name)+"' in this object!")

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

        if not self.active or not self.game.combat_in_progress or (self.wielder.surf_alpha is not None and self.wielder.surf_alpha == 0):
            self.set_surface_alpha(0)
        else:
            self.set_surface_alpha(None)

        Entity.update(self, dt, acc)


class Sword(Weapon):
    def __init__(self, game, wielder, damage=35):
        Weapon.__init__(self, game, wielder, 'weapons/sword.png', anchor_pt=(5, 60))

        self.swing_time = .125
        self.arc_angle = math.radians(90)
        self.damage = damage
        self.swing_increment = self.arc_angle / self.swing_time
        self.is_melee = True

        self.swinging = False

    def __getstate__(self):
        d = Weapon.__getstate__(self)
        d.update({
            'swing_time': self.swing_time,
            'arc_angle': self.arc_angle,
            'damage': self.damage,
            'swing_increment': self.swing_increment,
            'swing_time': self.swing_time,
            'swinging': self.swinging,
        })

        return d

    def __setstate__(self, state):
        self.image = self.base_image = pygame.image.load(renpy.file('weapons/sword.png'))

        self.swing_time = state['swing_time']
        self.arc_angle = state['arc_angle']
        self.damage = state['damage']
        self.swing_increment = state['swing_increment']
        self.swing_time = state['swing_time']
        self.swinging = state['swinging']

        Weapon.__setstate__(self, state)

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
    def __init__(self, game, pos, image_folder, char_id):
        self.id = char_id

        self.__image_folder = image_folder
        self.char_images = {
            'default': pygame.image.load(renpy.file(image_folder+'/default.png')),
            'with_weapon': pygame.image.load(renpy.file(image_folder+'/with_weapon.png')),
        }

        self.base_image = self.char_images['default']
        self.collider_scale_factor_x = 0.8
        self.collider_scale_factor_y = 0.6

        self.health = 100
        self.max_health = 100
        self.default_spawn_point = (15 * game_data.tile_size, 15 * game_data.tile_size)
        self.invuln_time = 0.75

        self.weapon = None

        Entity.__init__(self, game, pos)
        game.all_voices.add(self)

    def __getstate__(self):
        img_state = 'default'
        if self.base_image == self.char_images['with_weapon']:
            img_state = 'with_weapon'

        d = Entity.__getstate__(self)
        d.update({
            'id': self.id,
            'image_folder': self.__image_folder,
            'collider_scale_factor_x': self.collider_scale_factor_x,
            'collider_scale_factor_y': self.collider_scale_factor_y,
            'health': self.health,
            'max_health': self.max_health,
            'default_spawn_point': self.default_spawn_point,
            'invuln_time': self.invuln_time,
            'img_state': img_state,
        })

        return d

    def __setstate__(self, state):
        self.id = state['id']
        self.__image_folder = state['image_folder']
        self.collider_scale_factor_x = state['collider_scale_factor_x']
        self.collider_scale_factor_y = state['collider_scale_factor_y']
        self.health = state['health']
        self.max_health = state['max_health']
        self.default_spawn_point = state['default_spawn_point']
        self.invuln_time = state['invuln_time']

        self.char_images = {
            'default': pygame.image.load(renpy.file(self.__image_folder+'/default.png')),
            'with_weapon': pygame.image.load(renpy.file(self.__image_folder+'/with_weapon.png')),
        }

        self.base_image = self.image = self.char_images[state['img_state']]

        Entity.__setstate__(self, state)

    def check_collision(self, other):
        A_sz = cd.Vector2D(self.base_image.get_rect().size)
        B_sz = cd.Vector2D(other.base_image.get_rect().size)

        A_sz[0] *= self.collider_scale_factor_x
        A_sz[1] *= self.collider_scale_factor_y

        if hasattr(other, 'collider_scale_factor_x'):
            B_sz[0] *= other.collider_scale_factor_x

        if hasattr(other, 'collider_scale_factor_y'):
            B_sz[1] *= other.collider_scale_factor_y

        polyA = cd.Rectangle(A_sz)
        polyB = cd.Rectangle(B_sz)

        polyA.rotate(self.rot)
        polyA.translate(self.rect.center)

        if hasattr(other, 'rot'):
            polyB.rotate(other.rot)

        polyB.translate(other.rect.center)

        return cd.check_collision(polyA, polyB)

    def alive(self):
        return self.health > 0

    def set_health(self, health, attacker=None):
        damaged = health < self.health and health >= 0

        if health < self.health and self.invuln_time > 0:
            return

        if health <= 0:
            # make sure there's at least one voice left alive
            if self.game.voices_alive() > 1:
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

    def turn_to(self, point):
        self.rot = math.atan2(point[1] - self.pos[1], point[0] - self.pos[0]) + (math.pi / 2)

    def on_damaged(self, attacker):
        pass

    def update(self, dt, acc=(0, 0)):
        if self.invuln_time > 0:
            self.invuln_time -= dt
        else:
            self.invuln_time = 0

        if self.game.combat_in_progress:
            self.base_image = self.char_images['with_weapon']
        else:
            self.base_image = self.char_images['default']

        Entity.update(self, dt, acc)


class AIVoice(Voice):
    def __init__(self, game, pos, image_folder, id):
        Voice.__init__(self, game, pos, image_folder, id)

        self.__target = None

    def __setattr__(self, name, value):
        if name == 'target':
            self.__target = value # apply name-mangling
            #Voice.__setattr__(self, '__target', value)
        else:
            Voice.__setattr__(self, name, value)

    def __getattr__(self, name):
        if name == 'target':
            if isinstance(self.__target, Voice):
                return self.__target
            elif isinstance(self.__target, str):
                return game_data.game.voice_by_id(self.__target)
            elif self.__target is None:
                return None
        else:
            raise AttributeError("No such attribute '"+str(name)+"' in AIVoice instance")

    def __getstate__(self):
        d = Voice.__getstate__(self)
        if self.target is not None:
            d['target_id'] = self.target.id
        else:
            d['target_id'] = None

        return d

    def __setstate__(self, state):
        self.__target = state['target_id']

        Voice.__setstate__(self, state)

    def update(self, dt, acc=(0, 0)):
        if self.target is not None:
            self.turn_to(self.target.pos)

            if self.game.ai_active:
                self.vel = utils.magn_dir_vec(200, self.target.pos, self.pos)

                if not self.target.alive():
                    live_voices = []

                    for voice in self.game.all_voices.sprites():
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
    def __init__(self, game, pos):
        if hasattr(game, 'pyro') and config.developer:
            raise RuntimeError("Attempted to spawn Pyromaniac twice!")

        game.pyro = self

        AIVoice.__init__(self, game, pos, 'voice2', 'pyro')

        self.weapon = Sword(game, self, 5)
        self.default_spawn_point = (4 * game_data.tile_size, 4 * game_data.tile_size)


class Survivor(AIVoice):
    def __init__(self, game, pos):
        if hasattr(game, 'survivor') and config.developer:
            raise RuntimeError("Attempted to spawn Survivor twice!")

        game.survivor = self

        AIVoice.__init__(self, game, pos, 'voice3', 'surv')

        self.weapon = Sword(game, self, 5)
        self.default_spawn_point = (26 * game_data.tile_size, 4 * game_data.tile_size)


class Artist(AIVoice):
    def __init__(self, game, pos):
        if hasattr(game, 'artist') and config.developer:
            raise RuntimeError("Attempted to spawn Artist twice!")

        game.artist = self

        AIVoice.__init__(self, game, pos, 'voice4', 'artist')

        self.weapon = Sword(game, self, 5)
        self.default_spawn_point = (26 * game_data.tile_size, 27 * game_data.tile_size)


class Player(Voice):
    def __init__(self, game, pos):
        if hasattr(game, 'player') and config.developer:
            raise RuntimeError("Attempted to spawn Player twice!")

        Voice.__init__(self, game, pos, 'voice1', 'calm')
        game.player = self

        self.movement_allowed = False

        self.weapon = Sword(game, self)
        self.default_spawn_point = (3 * game_data.tile_size, 27 * game_data.tile_size)

        self.m_pos = (0, 0)

    def __getstate__(self):
        d = Voice.__getstate__(self)
        d.update({
            'movement_allowed': self.movement_allowed
        })

        return d

    def __setstate__(self, state):
        self.movement_allowed = state['movement_allowed']
        self.m_pos = (0, 0)

        Voice.__setstate__(self, state)

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
