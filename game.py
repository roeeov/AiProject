import sys

import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from constants import TILE_SIZE, PLAYER_SPEED, PLAYER_POS, PLAYERS_SIZE, JUMP_HEIGHT, DISPLAY_SIZE

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
            'player': load_image('entities/player.png'),
            'background': load_image('background.png', scale=DISPLAY_SIZE),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }
        
        self.clouds = Clouds(self.assets['clouds'], count=16)
        
        self.player = Player(self, PLAYER_POS, PLAYERS_SIZE)
        
        self.scroll = [0, 0]

    def run(self):
        
        self.display.blit(self.assets['background'], (0, 0))
            
        self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
        self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
        self.clouds.update()
        self.clouds.render(self.display, offset=render_scroll)
            
        self.tilemap.render(self.display, offset=render_scroll)
            
        self.player.update(self.tilemap, (PLAYER_SPEED, 0))
        self.player.render(self.display, offset=render_scroll)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = False

        if self.up and self.player.grounded:
            self.player.Yvelocity = -JUMP_HEIGHT
