import pygame


class Render:
    def __init__(self):
        None
    
    def renderObject(self, screen, texture, rectangle):
        screen.blit(texture, rectangle)
    def renderObjects(self, screen, texture, rectangles):   
        for rectangle in rectangles:
            rectangle = rectangle.getRectangle()
            screen.blit(texture, rectangle)
    def renderEnemySnake(self, screen, texture, coordsList):
        for coords in coordsList:
            rectangle = texture.get_rect(topleft=coords)
            screen.blit(texture, rectangle)