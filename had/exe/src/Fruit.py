import random
from Coords import Coords

class Fruit:
    def __init__(self):
        self.coords = Coords(0,0)
        self.generateFruit()

    def generateFruit(self):
        self.coords.x = random.randrange(0, 1920, 20)
        self.coords.y = random.randrange(0, 1080, 20)
