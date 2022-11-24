import sys
import pygame as pg
from random import randint

validMoves = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]


def check_keydown_events(game, event, settings):
    key = event.key  # Access key
    if key in validMoves:
        pass


def check_events(game, settings):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(game=game, event=event, settings=settings)
