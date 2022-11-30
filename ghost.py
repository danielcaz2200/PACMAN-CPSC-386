import pygame as pg
import game_functions as gf
from vector import Vector as Vec
from pygame.sprite import Sprite
from timer import Timer
from menus import GameController


class Ghost(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.img = pg.image.load('images/blinky_0.png')
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        self.draw()


class Blinky(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/blinky_0.png')


class Pinky(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/pinky_0.png')


class Inky(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/inky_0.png')


class Clyde(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/clyde_0.png')
