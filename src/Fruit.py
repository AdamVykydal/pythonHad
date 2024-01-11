import random
from os import path
import pygame
from definitions import IMG_DIR
from Coords import Coords


class Fruit:
    def __init__(self):
        self.fruitTexture = pygame.image.load(
            path.join(IMG_DIR, "redApple.png"))
        self.coords = Coords(0,0)
        self.generateFruit()

    def generateFruit(self):
        self.coords.x = random.randrange(0, 1920, 20)
        self.coords.y = random.randrange(0, 1080, 20)

    def getRectangle(self):
        return self.coords
