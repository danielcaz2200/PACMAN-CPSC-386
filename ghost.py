import pygame as pg
import game_functions as gf
from vector import Vector as Vec
from pygame.sprite import Sprite
from timer import Timer
from menus import GameController


class Ghosts():
    def __init__(self, game, location: tuple) -> None:
        super().__init__()
        self.game = game
        self.locations = self.game.locations
        self.settings = game.settings
        self.maze = self.game.maze.currMaze
        self.barriers = self.game.maze.barriers

        # self.img = pg.image.load('images/pacman_0.png')
        self.rect = self.img.get_rect()
        self.pos = Vec(location[0], location[1])
        self.dir = 'STOP'
        self.screen = game.screen
        self.speed = self.settings.playerSpeed
        self.rect.left = self.pos.x * self.rect.width
        self.rect.top = self.pos.y * self.rect.height
        self.last = pg.time.get_ticks()
        self.delay = 200
        self.scores = GameController()



    def checkCollisions(self): pass

    def update(self): pass

    def draw(self):
        self.screen.blit(self.timer.imagerect(), self.rect)
