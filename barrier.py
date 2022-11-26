import pygame
from pygame.sprite import Sprite


class Barrier(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.size = 30
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 50, 255))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.left = x * self.rect.width
        self.rect.top = y * self.rect.height
        self.screen = game.screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()
