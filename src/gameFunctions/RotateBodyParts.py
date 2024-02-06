from gameFunctions.SnakeHead import SnakeHead
from gameFunctions.GameFunctionsConst import GameFunctionsConst
from gameFunctions.SnakeTextures import SnakeTextures

class RotateBodyPart:
    def __init__(self) -> None:
        self.gameFunctionsConst = GameFunctionsConst()
    def checkAndRotate(self, part):
        if isinstance(part, SnakeHead):
            if part.direction == self.gameFunctionsConst.RIGHT:
                return self.gameFunctionsConst.RIGHT
            elif part.direction == self.gameFunctionsConst.DOWN:
                return self.gameFunctionsConst.DOWN
            elif part.direction == self.gameFunctionsConst.LEFT:
                return self.gameFunctionsConst.LEFT
            elif part.direction == self.gameFunctionsConst.UP:
                return self.gameFunctionsConst.UP
                    
            


        