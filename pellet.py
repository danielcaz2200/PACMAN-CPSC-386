from pygame.sprite import Sprite
import pygame as pg


class Pellet(Sprite):
    def __init__(self, game, x, y, type: str):
        super().__init__()
        self.screen = game.screen
        self.pts = game.settings.pelletScore
        if type == 'pellet':
            self.img = pg.transform.scale(
                pg.image.load('images/pellet.png'), (30, 30))
        elif type == 'powerpellet':
            self.img = pg.transform.scale(
                pg.image.load('images/powerpellet.png'), (30, 30))
        self.rect = self.img.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update(self):
        self.draw()
