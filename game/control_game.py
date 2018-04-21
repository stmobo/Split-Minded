import math
import renpy.exports as renpy
import pygame

# the game runs at 1280x720 by default
# use roughly half of the total screen size for the control game view
field_dims = [2000, 2000]
screen_native_dims = [640, 640]

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

    def update(self, dt, acc):
        self.vel[0] += acc[0] * dt
        self.vel[1] += acc[1] * dt

        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt

        self.image = pygame.transform.rotate(self.base_image, -math.degrees(self.rot))
        self.rect = self.image.get_rect()

        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]

class Voice(Entity):
    def __init__(self, pos, image):
        self.base_image = pygame.image.load(image)
        #self.base_image = img.convert_alpha()

        Entity.__init__(self, pos)
        all_voices.add(self)



class Player(Voice):
    def __init__(self, pos):
        # self.base_image = pygame.Surface((20, 10), flags=pygame.SRCALPHA)
        # self.base_image.fill((0, 0, 0, 0))
        # pygame.draw.polygon(
        #     self.base_image, (255, 255, 255, 255),
        #     [(0, 0), (5, 5), (0, 10), (20, 5)]
        # )

        Voice.__init__(self, pos, renpy.file('voice1-holding.png'))

    def mouse_update(self, m_pos):
        self.m_pos = m_pos

    def update(self, dt):
        pressed = pygame.key.get_pressed()

        left = pressed[pygame.K_LEFT] or pressed[pygame.K_a]
        right = pressed[pygame.K_RIGHT] or pressed[pygame.K_d]
        up = pressed[pygame.K_UP] or pressed[pygame.K_w]
        down = pressed[pygame.K_DOWN] or pressed[pygame.K_s]

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
