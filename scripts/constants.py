import tkinter as tk
import pygame

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

DISPLAY_SIZE = (screen_width*0.8, screen_height*0.8)
FPS = 60

TILE_SIZE = DISPLAY_SIZE[0] * 3 // 80

PLAYER_SPEED = 10.4 * TILE_SIZE / 60
PLAYER_HITBOX = 0.7 # precent
GRAVITY = (1.06 / 48) * TILE_SIZE    # Downward acceleration per frame


PLAYER_POS = [50, 50]

# Needs to be changed for every new gamemode added
GAMEMODES= {'cube', 'wave', 'ball'}
GRAVITY_GAMEMODES = {'cube', 'ball'}
PLAYERS_SIZE = {'cube': (TILE_SIZE*9.5//10, TILE_SIZE*9.5//10), 'wave': (TILE_SIZE//2, TILE_SIZE//2), 'ball': (TILE_SIZE*9.5//10, TILE_SIZE*9.5//10)}
PLAYERS_IMAGE_SIZE = {
        'cube': PLAYERS_SIZE['cube'],
        'wave': (PLAYERS_SIZE['wave'][0]*1.4, PLAYERS_SIZE['wave'][1]*1.4),
        'ball': PLAYERS_SIZE['ball'],
    }
PLAYER_VELOCITY = {'cube': (16 / 48) * TILE_SIZE, 'wave': PLAYER_SPEED, 'ball': (1.8 / 48) * TILE_SIZE}
MAX_VELOCITY = {'cube': (16 / 48) * TILE_SIZE, 'ball': (12 / 48) * TILE_SIZE}

PHYSICS_TILES = {'grass', 'stone'}
INTERACTIVE_TILES = {'portal', 'spike', 'finish'}
AUTOTILE_TYPES = {'grass', 'stone'}
SPIKE_SIZE = (0.4, 0.6) # precent
FONT = None

EDITOR_SCROLL = (8 / 48) * TILE_SIZE
LEVEL_SELECTOR_SCROLL = DISPLAY_SIZE[0] * 6 // 100 // 3

DIFFICULTIES = ('easy', 'normal', 'hard', 'harder', 'insane', 'demon')


#debugging
DRAW_PLAYER_HITBOX = False
SHOW_BUTTON_HITBOX = False
SHOW_SPIKE_HITBOX = False
SHOW_FPS_COUNTER = False