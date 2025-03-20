import sys

import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from constants import TILE_SIZE, PLAYER_POS, PLAYERS_SIZE, DISPLAY_SIZE, PLAYERS_IMAGE_SIZE, GAMEMODES, GRAVITY_GAMEMODES

class Game:
    def __init__(self, display):

        self.display = display

        self.up = False
        
        self.tilemap = Tilemap(self, tile_size = TILE_SIZE)
        self.tilemap.load('map.json')
        IMGscale = (self.tilemap.tile_size, self.tilemap.tile_size)

        self.assets = {
            'decor': load_images('tiles/decor', scale=IMGscale),
            'grass': load_images('tiles/grass', scale=IMGscale),
            'stone': load_images('tiles/stone', scale=IMGscale),
            'background': load_image('background.png', scale=DISPLAY_SIZE),
            'clouds': load_images('clouds'),
        }
        for gamemode in GAMEMODES:
            IMG_scale = PLAYERS_IMAGE_SIZE[gamemode]
            base_path = 'player/' + gamemode
            self.assets[base_path + '/run'] = Animation(load_images(base_path + '/run', scale=IMG_scale), img_dur=4)
            self.assets[base_path + '/death'] = Animation(load_images(base_path + '/death', scale=IMG_scale), loop=False)
            if gamemode in GRAVITY_GAMEMODES:
                self.assets[base_path + '/jump'] = Animation(load_images(base_path + '/jump', scale=IMG_scale))
        
        self.clouds = Clouds(self.assets['clouds'], count=16)
        
        self.player = Player(self, PLAYER_POS, PLAYERS_SIZE)
        
        self.scroll = [0, 0]

    def reset(self):
        self.scroll = [0, 0]
        self.up = False
        self.player.reset()

    def run(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_r:
                    self.reset()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = False

        self.display.blit(self.assets['background'], (0, 0))
            
        self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 3 - self.scroll[0]) / 20
        self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 20
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
        self.clouds.update()
        self.clouds.render(self.display, offset=render_scroll)
            
        self.tilemap.render(self.display, offset=render_scroll)
            
        self.player.update(self.tilemap, self.up)
        self.player.render(self.display, offset=render_scroll)    

        # check if the player death animation has ended
        if self.player.respawn: self.reset()
