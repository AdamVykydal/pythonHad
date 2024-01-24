import copy
from SnakeBody import SnakeBody

class Snake():
    def __init__(self, snakeHead):
        self.snakeParts = []
        self.snakeParts.append(snakeHead)
        self.snakePartIndex = None

    def addSnakePart(self):
        newBodyCoords = copy.deepcopy(self.snakeParts[-1].coords)
        self.snakeParts.append(SnakeBody(newBodyCoords))

    def snakeMove(self):
        self.snakePartIndex = len(self.snakeParts) - 1

        for snakePart in reversed(self.snakeParts[1:]):

            self.snakePartIndex -= 1

            snakePart.coords = copy.deepcopy((self.snakeParts[self.snakePartIndex]).coords)

    def getSnakeParts(self):
        return self.snakeParts
    def restartSnake(self, snakeHead):
        self.snakeParts = []
        self.snakeParts.append(snakeHead)
        self.snakePartIndex = None