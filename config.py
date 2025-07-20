# Game Display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60

# Map Settings
TILE_SIZE = 64
MAP_WIDTH = 10
MAP_HEIGHT = 10
TILE_TYPES = ['grass', 'forest', 'mountain', 'water']

TILE_LOOKUP = {
    0: 'grass',
    1: 'forest',
    2: 'mountain',
    3: 'water',
}

# Colors (RGB tuples)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_TEXT = (220, 220, 220)

# Asset Paths
ASSET_PATHS = {
    'tiles': 'assets/tiles/',
    'units': 'assets/units/',
    'ui': 'assets/ui/',
    'fonts': 'assets/fonts/',
    'audio': 'assets/audio/',
    'maps': 'assets/maps/',
}