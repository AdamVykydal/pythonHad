import copy
from gameFunctions.SnakeBody import SnakeBody

class Snake():
    def __init__(self, snakeHead):
        self.parts = []
        self.parts.append(snakeHead)
        self.snakePartIndex = None

    def addSnakePart(self):
        newBodyCoords = copy.deepcopy(self.parts[-1].coords)
        self.parts.append(SnakeBody(newBodyCoords))

    def snakeMove(self):
        self.snakePartIndex = len(self.parts) - 1

        for snakePart in reversed(self.parts[1:]):

            self.snakePartIndex -= 1

            snakePart.coords = copy.deepcopy((self.parts[self.snakePartIndex]).coords)

    def restartSnake(self, snakeHead):
        self.parts = []
        self.parts.append(snakeHead)
        self.snakePartIndex = None