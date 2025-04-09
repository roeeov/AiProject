import sys

import pygame
from scripts.utils import *
from scripts.gameStateManager import game_state_manager
from scripts.mapManager import map_manager
from scripts.constants import *

class myLevels:
    
    def __init__(self, display):

        self.display = display
        self.scroll = 0
        self.reloadButtons()

    def reloadButtons(self):
        self.buttons = []

        prev_text = Text('back', pos = (50, 50), size=UIsize(1.5))
        prev_button = Button(prev_text, (0 ,255, 0), button_type='prev')
        self.buttons.append(prev_button)

        new_map_text = Text('new map', pos = vh(90, 90), size=UIsize(3))
        new_map_button = Button(new_map_text, (0 ,255, 0), button_type='new_map')
        self.buttons.append(new_map_button)

        my_maps_dict = map_manager.getEditorMapsDict()
        for idx, map in enumerate(my_maps_dict.values()):
            map_text = map['info']['name'] + ' '*5 + map['info']['creator'] + ' '*5 + map['info']['difficulty']
            map_text = Text(map_text, pos = (vh(50, -1)[0], (idx+1)*vh(-1, 12)[1] - vh(-1, 3)[1]), size=UIsize(6))
            map_button = Button(map_text, (0 ,255, 0), "map_idx: " + map['info']['id'])
            self.buttons.append(map_button)

        self.max_scroll = -vh(-1, 12)[1] * len(my_maps_dict)

        
    def run(self):

        self.display.fill((242, 54, 245))

        mouse_pressed = False
        mouse_released = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state_manager.returnToPrevState()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pressed = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_released = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if self.scroll < 0:
                    self.scroll += LEVEL_SELECTOR_SCROLL
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                self.scroll -= LEVEL_SELECTOR_SCROLL
                if self.scroll < self.max_scroll:
                    self.scroll = self.max_scroll

        for button in self.buttons:
            if button.type not in {'prev', 'new_map'}: button.set_offset(0, self.scroll)
            button.update(mouse_pressed, mouse_released)
            if button.is_clicked():
                if button.type == 'prev':
                    game_state_manager.returnToPrevState()
                elif button.type == 'new_map':
                    map_manager.createNewMap()
                    game_state_manager.setState('my_level_page')
                    self.reloadButtons()
                else:
                        map_id = button.type.split()[-1]
                        map_manager.setMap(map_id)
                        game_state_manager.setState('my_level_page')

            button.blit(self.display)

class myLevelPage:

    def __init__(self, display):
        self.display = display
        self.buttons = []

        play_text = Text('play', pos = vh(60, 60), size=UIsize(6))
        play_button = Button(play_text, (0 ,255, 0), button_type='play')
        self.buttons.append(play_button)

        edit_text = Text('edit', pos = vh(40, 60), size=UIsize(6))
        edit_button = Button(edit_text, (0 ,255, 0), button_type='edit')
        self.buttons.append(edit_button)

        prev_text = Text('back', pos = (50, 50), size=UIsize(1.5))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state_manager.returnToPrevState()
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
                    map_manager.loadMap()
                    game_state_manager.setState('edit')
            button.blit(self.display)

        

