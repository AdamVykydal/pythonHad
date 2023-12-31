import pygame


class SnakeBody:
    def __init__(self, rectangle):
        self.rectangle = rectangle
        self.lastRectPos = (0,0)
    def setRectangle(self, rectangle):
        self.rectangle = rectangle
    def getRectangle(self):
        return self.rectangle
    def setlastRectPos(self, lastRectPos):
        self.lastRectPos = lastRectPos
    def getlastRectPos(self):
        return self.lastRectPos
    
    
    
class SnakeHead(SnakeBody):
    def __init__(self, rectangle):
        super().__init__(rectangle)
        self.speed = 20
        self.direction = (self.speed, 0)

    def getRectangle(self):
        return super().getRectangle()
    def getlastRectPos(self):
        return super().getlastRectPos()
    def setlastRectPos(self, lastRectPos):
        super().setlastRectPos(lastRectPos)
    
    def setDirectionUp(self):
        self.direction = (0, -self.speed)

    def setDirectionLeft(self):
        self.direction = (-self.speed, 0)

    def setDirectionDown(self):
        self.direction = (0, self.speed)

    def setDirectionRight(self):
        self.direction = (self.speed, 0)

    def moveSnakeHead(self):
        self.lastRectPos = self.rectangle
        self.rectangle.move_ip(self.direction[0], self.direction[1])
        

    def snakeAndWall(self):
        if self.rectangle.x > 1900:
            self.rectangle.x = 0
            return
        elif self.rectangle.x < 0:
            self.rectangle.x = 1900
            return
        elif self.rectangle.y > 1060:
            self.rectangle.y = 0
            return
        elif self.rectangle.y < 0:
            self.rectangle.y = 1060
            return