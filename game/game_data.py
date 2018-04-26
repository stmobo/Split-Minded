import renpy.exports as renpy

# the game runs at 1280x720 by default
# use roughly half of the total screen size for the control game view
tile_size = 50 # px square
field_sz_tiles = [30, 30]
field_size = [field_sz_tiles[0]*tile_size, field_sz_tiles[1]*tile_size]
screen_total_size = [1280, 720]
gameplay_screen_size = [640, 640]

screen_center = None

combat_in_progress = False
ai_active = False

# dev purposes only:
force_combat_winner = None
skip_combat = False
