import pygame
from settings import Settings
from maze import Maze
from player import Pacman
from sound import Sound
from menus import GameController
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
        self.keyPress = False
        pacStart = self.maze.locations['pacman']
        self.clock = pygame.time.Clock()
        self.score = 0
        self.pacman = Pacman(game=self, location=pacStart)
        self.sound = Sound()

    def play(self):
        self.sound.play_startup()
        game = GameController()

        while True:
            gf.check_events(game=self, settings=self.settings,
                            pacman=self.pacman)
            if game.menu:
                game.main_menu()
            elif game.highscoremenu:
                game.highscore_menu()
            else:
                self.screen.fill(self.settings.bg)
                self.maze.update()
                self.pacman.update()
                pygame.display.flip()


if __name__ == '__main__':
    g = Game()
    g.play()
