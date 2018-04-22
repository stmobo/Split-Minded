import renpy.exports as renpy
import pygame
import math
import game_data

all_tiles = None
all_walls = None

tilemap = []
tile_sprites = []

tilemap_ctrlpanel = 2
tilemap_wall = 1
tilemap_empty = 0
tilemap_skip = -1

control_panel_sprite = pygame.image.load(renpy.file('tiles/control_panel.png'))

floor_tile_sprites = {
    'normal': pygame.image.load(renpy.file('tiles/floor_tiles/basic.png')),
    'vent': [
        pygame.image.load(renpy.file('tiles/floor_tiles/vent_1.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/vent_2.png')),
    ],
    'panel': [
        pygame.image.load(renpy.file('tiles/floor_tiles/panel_1.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/panel_2.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/panel_3.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/panel_4.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/panel_5.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/panel_6.png')),
    ],
    'wiring': [
        pygame.image.load(renpy.file('tiles/floor_tiles/wiring_1.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/wiring_2.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/wiring_3.png')),
        pygame.image.load(renpy.file('tiles/floor_tiles/wiring_4.png')),
    ]
}

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
    'cap': [
        pygame.image.load(renpy.file('tiles/cap_wall_tiles/0.png')),
        pygame.image.load(renpy.file('tiles/cap_wall_tiles/90.png')),
        pygame.image.load(renpy.file('tiles/cap_wall_tiles/180.png')),
        pygame.image.load(renpy.file('tiles/cap_wall_tiles/270.png')),
    ],
    'cross': pygame.image.load(renpy.file('tiles/wall_tile_cross.png')),
    'single': pygame.image.load(renpy.file('tiles/wall_tile_single.png')),
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
        rand = renpy.random.random()
        if rand < .90:
            Tile.__init__(self, pos, floor_tile_sprites['normal'])
        elif rand < .97:
            Tile.__init__(self, pos, renpy.random.choice(floor_tile_sprites['panel']))
        elif rand < .993:
            Tile.__init__(self, pos, renpy.random.choice((floor_tile_sprites['vent'])))
        else:
            Tile.__init__(self, pos, renpy.random.choice(floor_tile_sprites['wiring']))

class ControlPanel(Tile):
    def __init__(self, pos):
        Tile.__init__(self, pos, control_panel_sprite)
        all_walls.add(self)

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

        if n_neighbors == 0:
            base_image = wall_tile_sprites['single']
        elif n_neighbors == 1:
            if neighbor_up:
                base_image = wall_tile_sprites['cap'][0]
            elif neighbor_right:
                base_image = wall_tile_sprites['cap'][1]
            elif neighbor_down:
                base_image = wall_tile_sprites['cap'][2]
            else:
                base_image = wall_tile_sprites['cap'][3]
        elif n_neighbors == 2:
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
            s = None
            if tile_char == tilemap_wall:
                s = WallTile(pos)
            elif tile_char == tilemap_ctrlpanel:
                s = ControlPanel(pos)
            elif tile_char == tilemap_empty:
                s = FloorTile(pos)

            sprite_row.append(s)

        tile_sprites.append(sprite_row)

    all_tiles.draw(tile_surface)

def load_map_image(file):
    surf = pygame.image.load(file).convert(32)

    free_value = surf.get_at((0, 0))
    wall_value = surf.get_at((1, 0))
    skip_value = surf.get_at((2, 0))
    ctrl_panel_value = surf.get_at((3, 0))

    map = []

    for x in range(game_data.field_sz_tiles[0]):
        row = []
        for y in range(game_data.field_sz_tiles[1]):
            c = surf.get_at((x, y+1))
            if c == wall_value:
                row.append(tilemap_wall)
            elif c == free_value:
                row.append(tilemap_empty)
            elif c == ctrl_panel_value:
                row.append(tilemap_ctrlpanel)
            else:
                row.append(tilemap_skip)

        map.append(row)

    return map

def init():
    global tilemap, all_tiles, all_walls

    if all_tiles is not None:
        all_tiles.empty()

    if all_walls is not None:
        all_walls.empty()

    all_tiles = pygame.sprite.Group()
    all_walls = pygame.sprite.Group()

    tilemap = load_map_image(renpy.file('map.png'))
    read_tilemap()
