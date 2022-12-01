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
        self.screen.blit(self.timer.imagerect(), self.rect)

    def update(self):
        self.draw()


class Blinky(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/blinky_0.png')
        blinky = [pg.image.load(f'images/blinky_{i}.png') for i in range(2)]
        timer_blinky = Timer(frames=blinky, looponce=False, wait=250)
        self.timer = timer_blinky


class Pinky(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/pinky_0.png')
        pinky = [pg.image.load(f'images/pinky_{i}.png') for i in range(2)]
        timer_pinky = Timer(frames=pinky, looponce=False, wait=250)
        self.timer = timer_pinky

class Inky(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/inky_0.png')
        inky = [pg.image.load(f'images/inky_{i}.png') for i in range(2)]
        timer_inky = Timer(frames=inky, looponce=False, wait=250)
        self.timer = timer_inky


class Clyde(Ghost):
    def __init__(self, game, x, y):
        Ghost.__init__(self, game, x, y)
        self.img = pg.image.load('images/clyde_0.png')
        clyde = [pg.image.load(f'images/clyde_{i}.png') for i in range(2)]
        timer_clyde = Timer(frames=clyde, looponce=False, wait=250)
        self.timer = timer_clyde
