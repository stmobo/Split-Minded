import renpy.exports as renpy
import pygame
import math
import game_data

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

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_pos, base_image):
        pygame.sprite.Sprite.__init__(self)

        self.pos = tile_pos
        self.base_image = base_image  # for compat with Entities
        self.image = base_image
        self.is_wall = False

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pixel_pos()

    def __getstate__(self):
        return { 'pos': self.pos, 'is_wall': self.is_wall }

    def __setstate__(self, state):
        pygame.sprite.Sprite.__init__(self)
        self.is_wall = state['is_wall']

    def pixel_pos(self):
        return (
            int(self.pos[0] * game_data.tile_size),
            int(self.pos[1] * game_data.tile_size)
        )

class FloorTile(Tile):
    def __init__(self, pos, visual=None):
        if visual is None:
            self.visual = renpy.random.random()
        else:
            self.visual = visual

        if self.visual < .90:
            Tile.__init__(self, pos, floor_tile_sprites['normal'])
        elif self.visual < .97:
            Tile.__init__(self, pos, renpy.random.choice(floor_tile_sprites['panel']))
        elif self.visual < .993:
            Tile.__init__(self, pos, renpy.random.choice((floor_tile_sprites['vent'])))
        else:
            Tile.__init__(self, pos, renpy.random.choice(floor_tile_sprites['wiring']))

    def __getstate__(self):
        d = Tile.__getstate__(self)
        d['visual'] = self.visual

        return d

    def __setstate__(self, state):
        FloorTile.__init__(self, state['pos'], state['visual'])


class ControlPanel(Tile):
    def __init__(self, pos):
        self.is_wall = True

        Tile.__init__(self, pos, control_panel_sprite)

    def __setstate__(self, state):
        ControlPanel.__init__(self, state['pos'])


class WallTile(Tile):
    def __init__(self, pos, tilemap):
        self.is_wall = True

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

        base_image = self.determine_base_image(n_neighbors, neighbor_left, neighbor_right, neighbor_down, neighbor_up)

        self.neighbors = {
            'n': n_neighbors,
            'left': neighbor_left,
            'right': neighbor_right,
            'down': neighbor_down,
            'up': neighbor_up,
        }

        Tile.__init__(self, pos, base_image)

    def __getstate__(self):
        d = Tile.__getstate__(self)
        d['neighbors'] = self.neighbors

        return d

    def __setstate__(self, state):
        n = state['neighbors']

        base_image = self.determine_base_image(
            n['n'],
            n['left'],
            n['right'],
            n['down'],
            n['up'],
        )

        self.neighbors = state['neighbors']

        Tile.__init__(self, state['pos'], base_image)
        self.is_wall = True

    def determine_base_image(self, n_neighbors, neighbor_left, neighbor_right, neighbor_down, neighbor_up):
        if n_neighbors == 0:
            return wall_tile_sprites['single']
        elif n_neighbors == 1:
            if neighbor_up:
                return wall_tile_sprites['cap'][0]
            elif neighbor_right:
                return wall_tile_sprites['cap'][1]
            elif neighbor_down:
                return wall_tile_sprites['cap'][2]
            else:
                return wall_tile_sprites['cap'][3]
        elif n_neighbors == 2:
            if neighbor_up and neighbor_down:
                return wall_tile_sprites['line'][0]
            elif neighbor_left and neighbor_right:
                return wall_tile_sprites['line'][1]
            else:
                if neighbor_up and neighbor_left:
                    return wall_tile_sprites['bend'][2]
                elif neighbor_up and neighbor_right:
                    return wall_tile_sprites['bend'][3]
                elif neighbor_down and neighbor_left:
                    return wall_tile_sprites['bend'][1]
                elif neighbor_down and neighbor_right:
                    return wall_tile_sprites['bend'][0]
        elif n_neighbors == 3:
            if not neighbor_left:
                return wall_tile_sprites['junction'][0]
            elif not neighbor_up:
                return wall_tile_sprites['junction'][1]
            elif not neighbor_right:
                return wall_tile_sprites['junction'][2]
            elif not neighbor_down:
                return wall_tile_sprites['junction'][3]
        elif n_neighbors == 4:
            return wall_tile_sprites['cross']

def load_map_image(file='map.png'):
    surf = pygame.image.load(renpy.file(file)).convert(32)

    free_value = surf.get_at((0, 0))
    wall_value = surf.get_at((1, 0))
    skip_value = surf.get_at((2, 0))
    ctrl_panel_value = surf.get_at((3, 0))

    tilemap = []

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

        tilemap.append(row)


    all_tiles = pygame.sprite.Group()
    all_walls = pygame.sprite.Group()

    tile_surface = pygame.Surface(game_data.field_size)
    tile_surface.fill((0, 0, 0))

    for x, row in enumerate(tilemap):
        for y, tile_char in enumerate(row):
            pos = (x, y)
            s = None

            if tile_char == tilemap_wall:
                s = WallTile(pos, tilemap)
                all_walls.add(s)
            elif tile_char == tilemap_ctrlpanel:
                s = ControlPanel(pos)
                all_walls.add(s)
            elif tile_char == tilemap_empty:
                s = FloorTile(pos)

            if s is not None:
                all_tiles.add(s)

    return all_tiles, all_walls
