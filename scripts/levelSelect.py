import sys

import pygame
from scripts.utils import Text, Button, vh
from scripts.gameStateManager import game_state_manager
from scripts.mapManager import map_manager
from scripts.constants import *

class LevelSelect:
    
    def __init__(self, display):

        self.display = display
        self.scroll = 0
        self.buttons = []

        prev_text = Text('back', pos = (50, 50), size=30)
        prev_button = Button(prev_text, (0 ,255, 0), button_type='prev')
        self.buttons.append(prev_button)

        for idx, map in enumerate(map_manager.getMapDict().values()):
            map_text = map['info']['name'] + ' '*5 + map['info']['creator'] + ' '*5 + map['info']['difficulty']
            map_text = Text(map_text, pos = (vh(50, -1)[0], (idx)*120 + 80), size=80)
            map_button = Button(map_text, (0 ,255, 0), "map_idx: " + map['info']['id'])
            self.buttons.append(map_button)

        self.max_scroll = LEVEL_SELECTOR_SCROLL * (-3 * len(map_manager.getMapDict()) + 1)
        
    def run(self):

        self.display.fill((242, 54, 245))

        mouse_pressed = False
        mouse_released = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pressed = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if self.scroll < 0:
                    self.scroll += LEVEL_SELECTOR_SCROLL
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if self.scroll > self.max_scroll:
                    self.scroll -= LEVEL_SELECTOR_SCROLL
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_released = True

        for button in self.buttons:
            if button.type != 'prev': button.set_offset(0, self.scroll)
            button.update(mouse_pressed, mouse_released)
            if button.is_clicked():
                if button.type == 'prev':
                    game_state_manager.returnToPrevState()
                else:
                    map_id = button.type.split()[-1]
                    map_manager.setMap(map_id)
                    game_state_manager.setState('level_page')

            button.blit(self.display)

class LevelPage:

    def __init__(self, display):
        self.display = display
        self.buttons = []

        play_text = Text('play', pos = vh(67, 60), size=80)
        play_button = Button(play_text, (0 ,255, 0), button_type='play')
        self.buttons.append(play_button)

        edit_text = Text('edit', pos = vh(33, 60), size=80)
        edit_button = Button(edit_text, (0 ,255, 0), button_type='edit')
        self.buttons.append(edit_button)

        prev_text = Text('back', pos = (50, 50), size=30)
        prev_button = Button(prev_text, (0 ,255, 0), button_type='prev')
        self.buttons.append(prev_button)

    def run(self):

        self.display.fill((245, 137, 49))

        map_name = map_manager.getMapInfo(map_manager.current_map_id)["name"]
        map_name_text = Text(map_name, pos = vh(50, 25), size=120, color=(255, 255, 255))
        map_name_text.blit(display=self.display)

        map_creator = map_manager.getMapInfo(map_manager.current_map_id)["creator"]
        map_creator_text = Text("creator: " + map_creator, pos = vh(35, 40), size=40, color=(255, 255, 255))
        map_creator_text.blit(display=self.display)

        map_difficulty = map_manager.getMapInfo(map_manager.current_map_id)["difficulty"]
        map_difficulty_text = Text("difficulty: " + map_difficulty, pos =vh(65, 40), size=40, color=(255, 255, 255))
        map_difficulty_text.blit(display=self.display)

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
                if button.type == 'prev':
                    game_state_manager.returnToPrevState()
                elif button.type == 'play':
                    map_manager.loadMap()
                    game_state_manager.setState('game')
                elif button.type == 'edit':
                    print('edit')
            button.blit(self.display)

        

