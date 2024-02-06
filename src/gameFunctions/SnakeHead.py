from gameFunctions.SnakeBody import SnakeBody
from gameFunctions.GameFunctionsConst import GameFunctionsConst

class SnakeHead(SnakeBody):
    def __init__(self, coords):
        super().__init__(coords)
        
        self.gameFunctionsConst = GameFunctionsConst()
        self.direction = self.gameFunctionsConst.RIGHT_DIRECTION

    def setDirectionUp(self):
        if self.direction != self.gameFunctionsConst.DOWN_DIRECTION:
            self.direction = self.gameFunctionsConst.UP_DIRECTION

    def setDirectionLeft(self):
        if self.direction != self.gameFunctionsConst.RIGHT_DIRECTION:
            self.direction = self.gameFunctionsConst.LEFT_DIRECTION

    def setDirectionDown(self):
        if self.direction != self.gameFunctionsConst.UP_DIRECTION:
            self.direction = self.gameFunctionsConst.DOWN_DIRECTION

    def setDirectionRight(self):
        if self.direction != self.gameFunctionsConst.LEFT_DIRECTION:
            self.direction = self.gameFunctionsConst.RIGHT_DIRECTION

    def moveSnakeHead(self):
        self.coords.x += self.direction[0]
        self.coords.y += self.direction[1]
