import pygame
from pygame.sprite import Sprite, Group
from pellet import Pellet
from fruit import Fruit
from barrier import Barrier
from maps import Maps

charMappings = {
    '9': 'barrier',
    '8': 'pellet',
    '7': 'powerpellet',
    '6': 'fruit',
    'P': 'pacman',
    ' ': 'space',
    '\n': 'newline',
    '0': 'ghostspawn',
    'X': 'portal1',
    'Y': 'portal2'
}


class Maze:
    def __init__(self, game, life=0):
        self.game = game
        # Create pygame sprite groups to represent
        # the pellets and barriers
        self.pellets = Group()
        self.barriers = Group()
        self.fruits = Group()
        self.mapChooser = Maps()
        self.currMaze = self.mapChooser.loadMap()
        self.locations = dict()
        self.construct()

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
        elif elt == 'portal1':
            self.locations['portal1'] = (col, row)
            print(self.locations['portal1'])
        elif elt == 'portal2':
            self.locations['portal2'] = (col, row)
            print(self.locations['portal2'])
        elif elt == 'pacman':
            self.locations['pacman'] = (col, row)
            print(self.locations['pacman'])

    def construct(self):
        for row_num in range(len(self.currMaze)):
            strLen = len(self.currMaze[row_num])
            for col_num in range(strLen):
                self.addElement(
                    elt=charMappings[self.currMaze[row_num][col_num]], col=col_num, row=row_num)

    def reset(self):
        self.barriers.empty()
        self.pellets.empty()
        self.currMaze = self.mapChooser.newMap()

    def update(self):
        self.pellets.update()
        self.barriers.update()
        self.fruits.update()
