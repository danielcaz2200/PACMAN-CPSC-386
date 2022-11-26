import pygame as pg
import game_functions as gf
from vector import Vector as Vec
from pygame.sprite import Sprite
from timer import Timer


class Pacman(Sprite):
    def __init__(self, game, location: tuple) -> None:
        super().__init__()
        self.game = game
        self.locations = self.game.locations
        self.settings = game.settings
        self.maze = self.game.maze.currMaze
        self.barriers = self.game.maze.barriers

        self.img = pg.image.load('images/pacman_0.png')
        self.rect = self.img.get_rect()
        # self.startx = location[0]
        # self.starty = location[1]
        self.pos = Vec(location[0], location[1])
        # self.x = location[0]
        # self.y = location[1]
        self.dir = 'STOP'
        self.screen = game.screen
        self.speed = self.settings.playerSpeed
        self.rect.left = self.pos.x * self.rect.width
        self.rect.top = self.pos.y * self.rect.height
        self.last = pg.time.get_ticks()
        self.delay = 200

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

    def isValidMove(self):
        currX, currY = self.pos.x, self.pos.y
        if self.dir == 'L' and self.maze[currY][currX-1] != '@':
            self.timer = self.timers['L']
            return True
        elif self.dir == 'R' and self.maze[currY][currX+1] != '@':
            self.timer = self.timers['R']
            return True
        elif self.dir == 'U' and self.maze[currY-1][currX] != '@':
            self.timer = self.timers['U']
            return True
        elif self.dir == 'D' and self.maze[currY+1][currX] != '@':
            self.timer = self.timers['D']
            return True
        else:
            return False

    def canMove(self):
        now = pg.time.get_ticks()
        if now - self.last >= self.delay:
            self.last = now
            return True
        return False

    def checkCollisions(self):
        pelletCollisions = pg.sprite.spritecollide(
            self, self.game.maze.pellets, True)

        if pelletCollisions:
            self.game.score += self.settings.pelletScore
            self.game.sound.play_munch_pellet()

        fruitCollision = pg.sprite.spritecollide(
            self, self.game.maze.fruits, True)

        if fruitCollision:
            self.game.score += self.settings.fruitScore
            self.game.sound.play_munch_pellet()

        print(self.game.score)

    def update(self):
        if self.pos.x == self.locations['portal1'][0] - 1 and self.dir == 'L':
            self.pos.x = self.locations['portal2'][0]
        elif self.pos.x == self.locations['portal2'][0] + 1 and self.dir == 'R':
            self.pos.x = self.locations['portal1'][0]
        elif self.canMove() and self.isValidMove():
            self.pos += gf.directions[self.dir]
            self.checkCollisions()
        self.rect.left = self.pos.x * self.rect.width
        self.rect.top = self.pos.y * self.rect.height
        self.draw()

    # def checkWallCollisions(self, prev):
    #     collision = pg.sprite.spritecollideany(self, self.barriers)
    #     if collision:
    #         if self.dir == 'L':
    #             self.pos = prev + Vec(0.5, 0)
    #         elif self.dir == 'R':
    #             self.pos = prev - Vec(0.5, 0)
    #         elif self.dir == 'U':
    #             self.pos = prev + Vec(0, 0.5)
    #         elif self.dir == 'D':
    #             self.pos = prev - Vec(0, 0.5)
    #         self.rect.left = self.pos.x * self.rect.width
    #         self.rect.top = self.pos.y * self.rect.height

    def draw(self):
        self.screen.blit(self.timer.imagerect(), self.rect)
