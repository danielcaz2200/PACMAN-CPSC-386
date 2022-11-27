from pygame.sprite import Sprite
from random import choice
import pygame as pg


class Fruit(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.pts = game.settings.fruitScore
        image = choice(['images/fruit0.png', 'images/fruit1.png'])
        self.img = pg.transform.scale(
            pg.image.load(image), (game.settings.spriteSize))
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        self.draw()
