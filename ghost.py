import pygame as pg
import game_functions as gf
from vector import Vector as Vec
from pygame.sprite import Sprite
from timer import Timer
from menus import GameController


class Ghost(Sprite):
    def __init__(self, game, location: tuple) -> None:
        super().__init__()
        self.game = game
        self.locations = self.game.locations
        self.settings = game.settings
        self.maze = self.game.maze.currMaze
        self.barriers = self.game.maze.barriers

        self.img = pg.image.load('images/pacman_0.png')
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

        pacman_frames_r = [pg.image.load(
            f'images/pacman_{i}.png') for i in range(3)]
        pacman_frames_l = [pg.transform.flip(pg.image.load(
            f'images/pacman_{i}.png'), flip_x=True, flip_y=False) for i in range(3)]
        pacman_frames_u = [pg.transform.rotate(pg.image.load(
            f'images/pacman_{i}.png'), 90) for i in range(3)]
        pacman_frames_d = [pg.transform.rotate(pg.image.load(
            f'images/pacman_{i}.png'), -90) for i in range(3)]

        timer_left = Timer(frames=pacman_frames_l, looponce=False, wait=250)
        timer_right = Timer(frames=pacman_frames_r, looponce=False, wait=250)
        timer_up = Timer(frames=pacman_frames_u, looponce=False, wait=250)
        timer_down = Timer(frames=pacman_frames_d, looponce=False, wait=250)

        self.timers = {'L': timer_left, 'R': timer_right,
                       'U': timer_up, 'D': timer_down}
        self.timer = self.timers['L']



    def checkCollisions(self): pass

    def update(self): pass

    def draw(self):
        self.screen.blit(self.timer.imagerect(), self.rect)
