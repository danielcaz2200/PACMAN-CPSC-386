from pygame.sprite import Sprite
import pygame as pg


class Fruit(Sprite):
    def __init__(self, game, x, y):
        super().__init__(self)
        self.screen = game.screen
        self.pts = game.settings.fruitScore
        self.img = pg.image.load('images/fruit.png')
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height

    def draw(self):
        self.screen.blit(self.img, self.rect)
