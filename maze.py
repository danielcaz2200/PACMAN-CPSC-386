import pygame
from pygame.sprite import Sprite, Group
from pellets import Pellet

charMappings = {
    '@': 'wall',
    '.': 'pellet',
    '!': 'powerpellet',
    '%': 'fruit',
    'P': 'pacman',
}


class Maze:
    def __init__(self, game, life=0):
        self.game = game
        # Create pygame sprite groups to represent
        # the pellets and barriers
        self.pellets = Group()
        self.walls = Group()
        self.currLife = life
        self.currMaze = self.initMap(life=self.currLife)

        self.spawnPts = dict()

    def initMap(self, life):
        # Life indicates what life we are on, and what
        # map to switch to
        maze = list()
        with open(f'maze{life}.txt') as fp:
            rows = fp.readlines()
            for currentLine in rows:
                # REMOVE NEWLINES FROM THE LIST
                currentLine.replace('\n', '')
                maze.append(currentLine)
        return maze

    def addElement(self, elt: str):
        pass

    def construct(self):
        for row_num in range(len(self.currMaze)):
            strLen = len(self.currMaze[row_num])
            for col_num in range(strLen):
                self.addElement(charMappings[self.currMaze[row_num][col_num]])
