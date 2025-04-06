import sys

import pygame

from scripts.utils import *
from scripts.player import Player
from scripts.tilemap import tile_map
from scripts.clouds import Clouds
from scripts.constants import *

class Game:
    def __init__(self, display):

        self.display = display
        
        self.input = {'w': False, 'space': False, 'up_arrow': False, 'mouse': False}
        self.up = False

        self.buttons = []
        #add menu button here

        self.assets = load_assets()
        tile_map.assets = self.assets
        for gamemode in GAMEMODES:
            IMG_scale = PLAYERS_IMAGE_SIZE[gamemode]
            base_path = 'player/' + gamemode
            self.assets[base_path + '/run'] = Animation(load_images(base_path + '/run', scale=IMG_scale), img_dur=4)
            self.assets[base_path + '/death'] = Animation(load_images(base_path + '/death', scale=IMG_scale), loop=False)
            if gamemode in GRAVITY_GAMEMODES:
                self.assets[base_path + '/jump'] = Animation(load_images(base_path + '/jump', scale=IMG_scale))
        
        self.clouds = Clouds(self.assets['clouds'], count=16)
        
        self.player = Player(self)
        
        self.scroll = [0, 0]

    def reset(self):
        self.scroll = [0, 0]
        self.up = False
        self.player.reset()

    def blitMenu(self):
        rect_width, rect_height = DISPLAY_SIZE[0]//2, DISPLAY_SIZE[1]//2 # size of the black rectangle
        black_rect = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)  # enable per-pixel alpha
        black_rect.fill((0, 0, 0, 128))  # RGBA, 128 = 50% opacity

        # Position the rectangle in the center of the screen
        x = (DISPLAY_SIZE[0] - rect_width) // 2
        y = (DISPLAY_SIZE[1] - rect_height) // 2

        self.display.blit(black_rect, (x, y))



    def run(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.input['up_arrow'] = True
                if event.key == pygame.K_w:
                    self.input['w'] = True
                if event.key == pygame.K_SPACE:
                    self.input['space'] = True  
                if event.key == pygame.K_r:
                    self.reset()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.input['up_arrow'] = False
                if event.key == pygame.K_w:
                    self.input['w'] = False
                if event.key == pygame.K_SPACE:
                    self.input['space'] = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.input['mouse'] = True     
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.input['mouse'] = False     

        self.up = self.input['space'] or self.input['w'] or self.input['up_arrow'] or self.input['mouse']

        self.display.blit(self.assets['background'], (0, 0))
            
        self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 3 - self.scroll[0]) / 20
        self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 20
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
        self.clouds.update()
        self.clouds.render(self.display, offset=render_scroll)
            
        tile_map.render(self.display, offset=render_scroll)
            
        self.player.update(tile_map, self.up)
        self.player.render(self.display, offset=render_scroll)
        if (self.player.finishLevel): self.blitMenu()

        # check if the player death animation has ended
        if self.player.respawn: self.reset()
