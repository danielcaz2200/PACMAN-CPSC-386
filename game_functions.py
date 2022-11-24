import sys
import pygame as pg
from random import randint


def check_keydown_events(event):
    pass


def check_events(game, settings):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event=event)
