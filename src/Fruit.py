import random
from Coords import Coords

class Fruit:
    def __init__(self):
        self.coords = Coords(0,0)
        self.textureType = None
        self.generateTextureType()
        self.generateFruit()

    def generateFruit(self):
        self.coords.x = random.randrange(0, 1920, 20)
        self.coords.y = random.randrange(0, 1080, 20)
    
    def generateTextureType(self):
        randomNum = random.randrange(1, 3)
        print(randomNum)
        if randomNum == 1:
            self.textureType = "redApple"
        elif randomNum == 2:
            self.textureType = "greenApple"