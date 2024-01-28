import pygame
from LoadResources import LoadResources


class Image:
    def __init__(self, x, y, xScale, yScale, name, pngName, secondaryPngName, screen ):
        self.x = x
        self.y = y
        self.xScale = xScale
        self.yScale = yScale
        self.name = name
        self.screen = screen
        self.textRectangle = None
        self.pressed = 0
        self.loadResources = LoadResources()
        self.png = self.loadResources.loadImage(pngName)
        self.png = pygame.transform.scale(self.png, (xScale, yScale))
        self.rectangle = self.png.get_rect(center=(x, y))
        self.secondaryPng = self.loadResources.loadImage(secondaryPngName)
        self.secondaryPng = pygame.transform.scale(self.secondaryPng, (xScale, yScale))
        self.secondaryRectangle = self.secondaryPng.get_rect(center=(x, y))

    def renderImage(self):
        self.screen.blit(self.png, self.rectangle)
    def renderSecondaryColorImage(self):
        self.screen.blit(self.secondaryPng, self.secondaryRectangle)