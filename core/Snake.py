from SnakeBody import SnakeBody
class Snake():
    def __init__(self, snakeHead):
       self.snakeParts = []
       self.snakeParts.append(snakeHead)
    
    def addSnakePart(self):
        self.newBodyRectangle = self.snakeParts[-1].getRectangle()
        self.snakeParts.append(SnakeBody(self.newBodyRectangle))
    def snakeMove(self):
        self.partOrder = 0
        for self.snakePart in reversed(self.snakeParts[:-1]):
            self.partOrder += 1
            
            self.snakePart.setRectangle((self.snakeParts[self.partOrder]).getRectangle())

    def getSnakeParts(self):
        return self.snakeParts
    