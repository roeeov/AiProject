
DISPLAY_SIZE = (1280, 720)
FPS = 60

TILE_SIZE = 48

PLAYER_SPEED = 10.4 * TILE_SIZE / FPS
JUMP_HEIGHT = 12  # Initial upward velocity
WAVE_MOVE = PLAYER_SPEED
GRAVITY = 0.53    # Downward acceleration per frame


PLAYER_POS = (50, 50)

GAMEMODES= {'cube', 'wave'}
GRAVITY_GAMEMODES = {'cube'}

PLAYERS_SIZE = {'cube': (TILE_SIZE, TILE_SIZE), 'wave': (TILE_SIZE*0.5, TILE_SIZE*0.5)}
PLAYERS_IMAGE_SIZE = {
        'cube': PLAYERS_SIZE['cube'],
        'wave': (PLAYERS_SIZE['wave'][0]*1.2, PLAYERS_SIZE['wave'][1]*1.2)
    }

PHYSICS_TILES = {'grass', 'stone'}
AUTOTILE_TYPES = {'grass', 'stone'}

FONT = None

