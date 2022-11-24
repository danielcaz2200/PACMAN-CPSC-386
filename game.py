import pygame
from settings import Settings
from maze import Maze
import game_functions as gf


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
        self.maze = Maze(self)

        self.locations = self.maze.locations

    def play(self):
        while True:
            gf.check_events(game=self, settings=self.settings)
            self.screen.fill(self.settings.bg)
            self.maze.update()
            pygame.display.flip()


if __name__ == '__main__':
    g = Game()
    g.play()
