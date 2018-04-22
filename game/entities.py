import math
import renpy.exports as renpy
import pygame
import game_data

all_entities = pygame.sprite.Group()
all_voices = pygame.sprite.Group()
all_projectiles = pygame.sprite.Group()


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

    def update(self, dt, acc):
        self.vel[0] += acc[0] * dt
        self.vel[1] += acc[1] * dt

        self.last_pos = [self.pos[0], self.pos[1]]

        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt

        i = 0
        while i < len(self.update_hooks):
            v = self.update_hooks[i](self, dt, acc)  # call hook
            if not v: # if v is False or None then remove the hook
                self.update_hooks.pop(i)
            else:
                i += 1

        self.image = pygame.transform.rotate(self.base_image, -math.degrees(self.rot))
        if self.surf_alpha is not None:
            alpha_img = pygame.Surface(self.image.get_rect().size, pygame.SRCALPHA)
            alpha_img.fill((255, 255, 255, self.surf_alpha))
            self.image.blit(alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


class Voice(Entity):
    def __init__(self, pos, image_folder, char_id):
        self.id = char_id

        self.char_images = {
            'default': pygame.image.load(renpy.file(image_folder+'/default.png')),
            'with_weapon': pygame.image.load(renpy.file(image_folder+'/with_weapon.png')),
        }

        self.base_image = self.char_images['default']

        Entity.__init__(self, pos)
        all_voices.add(self)

    def turn_to(self, point):
        self.rot = math.atan2(point[1] - self.pos[1], point[0] - self.pos[0]) + (math.pi / 2)


class Pyromaniac(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice2', 'pyro')

    def update(self, dt):
        Voice.update(self, dt, (0, 0))


class Survivor(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice3', 'surv')

    def update(self, dt):
        Voice.update(self, dt, (0, 0))


class Artist(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice4', 'artist')

    def update(self, dt):
        Voice.update(self, dt, (0, 0))


class Player(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice1', 'calm')
        self.movement_allowed = False

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
