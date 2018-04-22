import renpy.exports as renpy
import pygame
import math
import game_data

all_tiles = pygame.sprite.Group()
all_walls = pygame.sprite.Group()

tilemap = []
tile_sprites = []

tilemap_wall = b'#'
tilemap_empty = b' '

floor_tile_sprite = pygame.image.load(renpy.file('tiles/basic_tile.png'))
vent_tile_sprite = pygame.image.load(renpy.file('tiles/vent_tile.png'))

wall_tile_sprites = {
    'line': [
        pygame.image.load(renpy.file('tiles/line_wall_tiles/vert.png')),
        pygame.image.load(renpy.file('tiles/line_wall_tiles/horiz.png')),
    ],
    'junction': [
        pygame.image.load(renpy.file('tiles/junction_wall_tiles/0.png')),
        pygame.image.load(renpy.file('tiles/junction_wall_tiles/90.png')),
        pygame.image.load(renpy.file('tiles/junction_wall_tiles/180.png')),
        pygame.image.load(renpy.file('tiles/junction_wall_tiles/270.png')),
    ],
    'bend': [
        pygame.image.load(renpy.file('tiles/bend_wall_tiles/0.png')),
        pygame.image.load(renpy.file('tiles/bend_wall_tiles/90.png')),
        pygame.image.load(renpy.file('tiles/bend_wall_tiles/180.png')),
        pygame.image.load(renpy.file('tiles/bend_wall_tiles/270.png')),
    ],
    'cross': pygame.image.load(renpy.file('tiles/wall_tile_cross.png')),
}

tile_surface = pygame.Surface(game_data.field_size)
tile_surface.fill((0, 0, 0))

def update_tiles(center):
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

    return tile_surface.subsurface(r), offset

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_pos, base_image):
        pygame.sprite.Sprite.__init__(self)

        all_tiles.add(self)

        self.pos = tile_pos
        self.image = base_image

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pixel_pos()

    def pixel_pos(self):
        return (
            int(self.pos[0] * game_data.tile_size),
            int(self.pos[1] * game_data.tile_size)
        )

class FloorTile(Tile):
    def __init__(self, pos):
        Tile.__init__(self, pos, floor_tile_sprite)

class WallTile(Tile):
    def __init__(self, pos):
        n_neighbors = 0

        if pos[0] > 0 and tilemap[pos[0]-1][pos[1]] == tilemap_wall:
            neighbor_left = True
            n_neighbors += 1
        else:
            neighbor_left = False

        if pos[0] < game_data.field_sz_tiles[0]-1 and tilemap[pos[0]+1][pos[1]] == tilemap_wall:
            neighbor_right = True
            n_neighbors += 1
        else:
            neighbor_right = False


        if pos[1] > 0 and tilemap[pos[0]][pos[1]-1] == tilemap_wall:
            neighbor_up = True
            n_neighbors += 1
        else:
            neighbor_up = False

        if pos[1] < game_data.field_sz_tiles[1]-1 and tilemap[pos[0]][pos[1]+1] == tilemap_wall:
            neighbor_down = True
            n_neighbors += 1
        else:
            neighbor_down = False

        if n_neighbors == 2:
            if neighbor_up and neighbor_down:
                base_image = wall_tile_sprites['line'][0]
            elif neighbor_left and neighbor_right:
                base_image = wall_tile_sprites['line'][1]
            else:
                if neighbor_up and neighbor_left:
                    base_image = wall_tile_sprites['bend'][2]
                elif neighbor_up and neighbor_right:
                    base_image = wall_tile_sprites['bend'][3]
                elif neighbor_down and neighbor_left:
                    base_image = wall_tile_sprites['bend'][1]
                elif neighbor_down and neighbor_right:
                    base_image = wall_tile_sprites['bend'][0]
        elif n_neighbors == 3:
            if not neighbor_left:
                base_image = wall_tile_sprites['junction'][0]
            elif not neighbor_up:
                base_image = wall_tile_sprites['junction'][1]
            elif not neighbor_right:
                base_image = wall_tile_sprites['junction'][2]
            elif not neighbor_down:
                base_image = wall_tile_sprites['junction'][3]
        elif n_neighbors == 4:
            base_image = wall_tile_sprites['cross']

        Tile.__init__(self, pos, base_image)
        all_walls.add(self)

def read_tilemap():
    tile_sprites = []
    all_tiles.empty()
    tile_surface.fill((0, 0, 0))

    for x, row in enumerate(tilemap):
        sprite_row = []

        for y, tile_char in enumerate(row):
            pos = (x, y)
            if tile_char == tilemap_wall:
                s = WallTile(pos)
            else:  # use floortiles by default
                s = FloorTile(pos)
            sprite_row.append(s)

        tile_sprites.append(sprite_row)

    all_tiles.draw(tile_surface)

# tilemap testing:
for x in range(game_data.field_sz_tiles[0]):
    if x == 0 or x == game_data.field_sz_tiles[0]-1:
        row = ['#'] * game_data.field_sz_tiles[1]
    else:
        row = ['#'] + ([' '] * (game_data.field_sz_tiles[0]-2)) + ['#']

    tilemap.append(row)


read_tilemap()
