from SnakeBody import SnakeBody

class SnakeHead(SnakeBody):
    def __init__(self, coords):
        super().__init__(coords)
        self.speed = 20
        self.directionUp = (0, -self.speed)
        self.directionLeft = (-self.speed, 0)
        self.directionDown = (0, self.speed)
        self.directionRight = (self.speed, 0)
        self.direction = self.directionRight

    def setDirectionUp(self):
        if self.direction != self.directionDown:
            self.direction = self.directionUp

    def setDirectionLeft(self):
        if self.direction != self.directionRight:
            self.direction = self.directionLeft

    def setDirectionDown(self):
        if self.direction != self.directionUp:
            self.direction = self.directionDown

    def setDirectionRight(self):
        if self.direction != self.directionLeft:
            self.direction = self.directionRight

    def moveSnakeHead(self):
        self.coords.x += self.direction[0]
        self.coords.y += self.direction[1]
