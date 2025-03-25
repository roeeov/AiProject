
DISPLAY_SIZE = (1280, 720)
FPS = 60

TILE_SIZE = 48

PLAYER_SPEED = 10.4 * TILE_SIZE / FPS
GRAVITY = 1.06    # Downward acceleration per frame


PLAYER_POS = [50, 50]

# Needs to be changed for every new gamemode added
GAMEMODES= {'cube', 'wave', 'ball'}
GRAVITY_GAMEMODES = {'cube', 'ball'}
PLAYERS_SIZE = {'cube': (TILE_SIZE, TILE_SIZE), 'wave': (TILE_SIZE*0.6, TILE_SIZE*0.6), 'ball': (TILE_SIZE, TILE_SIZE)}
PLAYERS_IMAGE_SIZE = {
        'cube': PLAYERS_SIZE['cube'],
        'wave': (PLAYERS_SIZE['wave'][0]*1.2, PLAYERS_SIZE['wave'][1]*1.2),
        'ball': PLAYERS_SIZE['ball'],
    }
PLAYER_VELOCITY = {'cube': 16, 'wave': PLAYER_SPEED, 'ball': 1.8}
MAX_VELOCITY = {'cube': 16, 'ball': 12}

PHYSICS_TILES = {'grass', 'stone'}
AUTOTILE_TYPES = {'grass', 'stone'}

FONT = None

EDITOR_SCROLL = 8