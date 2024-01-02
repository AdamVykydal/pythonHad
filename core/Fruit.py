import random

class Fruit:
    def __init__(self, rectangle):
        self.rectangle = rectangle
    def generateFruit(self):
        self.rectangle.x = random.randrange(0, 1920, 20)
        self.rectangle.y= random.randrange(0, 1080, 20)
    
