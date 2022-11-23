import pygame
from settings import Settings
from maze import Maze


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PACMAN - CPSC 386")
        # Initialize basic game settings
        self.settings = Settings()
        self.screenSize = (self.settings.screenWidth,
                           self.settings.screenHeight)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screenRect = self.screen.get_rect()

        # Set up game maze
        self.maze = None
        self.initialize_maze()

    def initialize_maze(self):
        self.maze = Maze(self)

    def play(self):
        while True:
            pygame.display.flip()


if __name__ == '__main__':
    g = Game()
    g.play()
