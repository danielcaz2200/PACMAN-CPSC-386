import pygame
from pygame.sprite import Sprite


class Barrier(Sprite):
    def __init__(self, game, x, y, size=32):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 50, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.screen = game.screen

    def draw(self):
        self.screen.blit(self.image, self.rect)
