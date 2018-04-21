import math
import renpy.exports as renpy
import pygame

# the game runs at 1280x720 by default
# use roughly half of the total screen size for the control game view
field_dims = [1200, 1200]
screen_native_dims = [640, 640]

all_entities = pygame.sprite.Group()
all_voices = pygame.sprite.Group()
all_projectiles = pygame.sprite.Group()

allow_clickfwd = False

game_displayable = None  # a reference to the main MentalControlGame instance

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

    def update(self, dt, acc):
        self.vel[0] += acc[0] * dt
        self.vel[1] += acc[1] * dt

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

        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]


class Voice(Entity):
    def __init__(self, pos, image_folder):
        self.char_images = {
            'default': pygame.image.load(renpy.file(image_folder+'/default.png')),
            'with_weapon': pygame.image.load(renpy.file(image_folder+'/with_weapon.png')),
        }

        self.base_image = self.char_images['default']

        Entity.__init__(self, pos)
        all_voices.add(self)

class Pyromaniac(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice2')

class Survivor(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice3')

class Artist(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice4')

class Player(Voice):
    def __init__(self, pos):
        Voice.__init__(self, pos, 'voice1')
        self.movement_allowed = False

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

        self.rot = math.atan2(self.m_pos[1] - self.pos[1], self.m_pos[0] - self.pos[0]) + (math.pi / 2)

        Voice.update(self, dt, (0, 0))


player = Player((400, 400))
