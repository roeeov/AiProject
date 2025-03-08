import pygame
from constants import SCREEN_SIZE, DISPLAY_SIZE, FPS
from game import Game
from menu import Menu
from gameStateManager import game_state_manager

class Engine:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('geometry dash')
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.display = pygame.Surface(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.game = Game(self.display)
        self.menu = Menu(self.display)

        self.state = {'game': self.game, 'menu': self.menu}

    def run(self):
        while True:
            self.state[game_state_manager.getState()].run()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Engine().run()
