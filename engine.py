import pygame
from constants import DISPLAY_SIZE, FPS
from game import Game
from menu import Menu
from gameStateManager import game_state_manager
from scripts.utils import Text

class Engine:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('geometry dash')
        self.display = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.game = Game(self.display)
        self.menu = Menu(self.display)

        self.state = {'game': self.game, 'menu': self.menu}

    def run(self):
        while True:
            self.state[game_state_manager.getState()].run()

            # blit fps counter
            fps = str(int(self.clock.get_fps()))
            fpsTXT = Text(fps, (50, 50))
            fpsTXT.blit(self.display)

            pygame.display.update() 
            self.clock.tick(FPS)


if __name__ == '__main__':
    Engine().run()
