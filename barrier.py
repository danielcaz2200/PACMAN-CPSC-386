import pygame
from pygame.sprite import Sprite


class Barrier(Sprite):
    def __init__(self, screen, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 50, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)
