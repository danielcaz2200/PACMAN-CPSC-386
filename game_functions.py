import sys
import pygame as pg
from random import randint
from vector import Vector as Vec

validMoves = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]

directions = {
    'L': Vec(-1, 0),
    'R': Vec(1, 0),
    'U': Vec(0, -1),
    'D': Vec(0, 1),
    'STOP': Vec(0, 0)
}


# def check_keyup_events(game, pacman, event, settings):
#     key = event.key
#     if key in validMoves:
#         print('stop')
#         pacman.dir = 'STOP'


def check_keydown_events(game, pacman, event, settings):
    key = event.key  # Access key
    if key in validMoves:
        if key == pg.K_LEFT:
            pacman.dir = 'L'
        elif key == pg.K_RIGHT:
            pacman.dir = 'R'
        elif key == pg.K_UP:
            pacman.dir = 'U'
        elif key == pg.K_DOWN:
            pacman.dir = 'D'


def check_events(game, pacman, settings):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(game=game, pacman=pacman,
                                 event=event, settings=settings)
        # elif event.type == pg.KEYUP:
        #     check_keyup_events(game=game, pacman=pacman,
        #                        event=event, settings=settings)
