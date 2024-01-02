import pygame
import copy


class SnakeBody:
    def __init__(self, rectangle):
        self.rectangle = rectangle
    def setRectangle(self, rectangle):
        self.rectangle = rectangle
    def getRectangle(self):
        return self.rectangle
    def getRectangleCopy(self):
        return self.rectangle.copy()
    
class SnakeHead(SnakeBody):
    def __init__(self, rectangle):
        super().__init__(rectangle)
        self.speed = 20
        self.direction = (self.speed, 0)
        self.directionUp = (0, -self.speed)
        self.directionLeft = (-self.speed, 0)
        self.directionDown = (0, self.speed)
        self.directionRight = (self.speed, 0)

    def getRectangle(self):
        return super().getRectangle()
    def getRectangleCopy(self):
        return super().getRectangleCopy()

    def setDirectionUp(self):
        if(self.direction != self.directionDown):
            self.direction = self.directionUp

    def setDirectionLeft(self):
        if(self.direction != self.directionRight):
            self.direction = self.directionLeft

    def setDirectionDown(self):
        if(self.direction != self.directionUp):
            self.direction = self.directionDown

    def setDirectionRight(self):
        if(self.direction != self.directionLeft):
            self.direction = self.directionRight

    def moveSnakeHead(self):
        #print("-------head after move:", self.rectangle)
        self.rectangle.move_ip(self.direction[0], self.direction[1])
        #print("-------head before move:", self.rectangle)
    
