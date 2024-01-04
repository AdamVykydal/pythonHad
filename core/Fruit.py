import random
import pygame

class Fruit:
    def __init__(self):
        self.fruitTexture = pygame.image.load("souces/img/redApple.png")
        self.rectangle = self.fruitTexture.get_rect(topleft=(1000, 500))
        self.generateFruit()
    def generateFruit(self):
        self.rectangle.x = random.randrange(0, 1920, 20)
        self.rectangle.y= random.randrange(0, 1080, 20)
    def getRectangle(self):
        return self.rectangle
    
