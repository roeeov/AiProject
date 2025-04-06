import sys

import pygame
from scripts.utils import *
from scripts.gameStateManager import game_state_manager
from scripts.constants import DISPLAY_SIZE

class Menu:
    
    def __init__(self, display):

        self.display = display

        start_text = Text('level select', pos = (DISPLAY_SIZE[0]//2, DISPLAY_SIZE[1]//2), size=30)
        start_button = Button(start_text, (59, 189, 30), 'level_select')

        select_level_text = Text('create map', pos = (DISPLAY_SIZE[0]//2, DISPLAY_SIZE[1]//3 * 2), size=30)
        select_level_button = Button(select_level_text, (29, 53, 207), 'create_map')

        self.buttons = [start_button, select_level_button]

    def run(self):

        self.display.fill((39, 178, 242))

        mouse_pressed = False
        mouse_released = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pressed = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_released = True

        for button in self.buttons:
            button.update(mouse_pressed, mouse_released)
            if button.is_clicked():
                if button.type == 'create_map':
                    pass
                if button.type == 'level_select':
                    game_state_manager.setState('level_select')
            button.blit(self.display)
