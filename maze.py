import pygame
from pygame.sprite import Sprite, Group
from pellet import Pellet
from fruit import Fruit
from barrier import Barrier

charMappings = {
    '@': 'barrier',
    '.': 'pellet',
    '!': 'powerpellet',
    '%': 'fruit',
    'P': 'pacman',
    ' ': 'space',
    '\n': 'newline',
    '-': 'spawn'
}


class Maze:
    def __init__(self, game, life=0):
        self.game = game
        # Create pygame sprite groups to represent
        # the pellets and barriers
        self.pellets = Group()
        self.barriers = Group()
        self.fruits = Group()
        self.currLife = life
        self.currMaze = self.initMap(life=self.currLife)
        self.spawnPts = dict()
        self.construct()

    def initMap(self, life):
        # Life indicates what life we are on, and what
        # map to switch to
        maze = list()
        with open(f'maze{life}.txt') as fp:
            rows = fp.readlines()
            for currentLine in rows:
                # REMOVE NEWLINES FROM THE LIST
                maze.append(currentLine)
        return maze

    def addElement(self, elt: str, col, row):
        if elt == 'barrier':
            self.barriers.add(Barrier(game=self.game, x=col, y=row))
        elif elt == 'pellet':
            self.pellets.add(
                Pellet(game=self.game, x=col, y=row, type=elt))
        elif elt == 'powerpellet':
            self.pellets.add(
                Pellet(game=self.game, x=col, y=row, type=elt))
        elif elt == 'fruit':
            self.fruits.add(Fruit(game=self.game, x=col, y=row))
        else:
            pass

    def construct(self):
        for row_num in range(len(self.currMaze)):
            strLen = len(self.currMaze[row_num])
            for col_num in range(strLen):
                self.addElement(
                    elt=charMappings[self.currMaze[row_num][col_num]], col=col_num, row=row_num)

    def reset(self):
        self.barriers.empty()
        self.pellets.empty()
        self.initMap(life=0)

    def update(self):
        self.pellets.update()
        self.barriers.update()
        self.fruits.update()
