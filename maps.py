from random import randint


class Maps:
    def __init__(self):
        self.choice = randint(0, 1)

    def loadMap(self):
        maze = list()
        with open(f'maps/maze{self.choice}.txt') as fp:
            rows = fp.readlines()
            for currentLine in rows:
                # REMOVE NEWLINES FROM THE LIST
                maze.append(currentLine)
        return maze

    def newMap(self):
        self.choice = randint(0, 2)
        return self.loadMap()
