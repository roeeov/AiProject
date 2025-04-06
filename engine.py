import pygame
from scripts.constants import DISPLAY_SIZE, FPS, SHOW_FPS_COUNTER
from scripts.game import Game
from scripts.menu import Menu
from scripts.levelSelect import LevelSelect, LevelPage
from scripts.gameStateManager import game_state_manager
from scripts.utils import Text
from editor import Editor

class Engine:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('geometry dash')
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        
        self.clock = pygame.time.Clock()
        self.game = Game(self.display)
        self.menu = Menu(self.display)
        self.level_select = LevelSelect(self.display)
        self.levelPage = LevelPage(self.display)
        self.editor = Editor(self.display)


        self.state = {'game': self.game, 'menu': self.menu, 'level_select': self.level_select, 'level_page': self.levelPage, 'edit': self.editor}

    def run(self):
        while True:
            self.state[game_state_manager.getState()].run()

            # blit fps counter
            if SHOW_FPS_COUNTER:
                fpsTXT = Text(str(int(self.clock.get_fps())), (50, 50))
                fpsTXT.blit(self.display)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Engine().run()
