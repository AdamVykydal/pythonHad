import pygame


class Render:
    def __init__(self):
        None
    
    def renderObject(self, screen, texture, rectangle):
        screen.blit(texture, rectangle)
    def renderSnake(self, screen, texture, rectangles):
        
        for rectangle in rectangles:

            rectangle = rectangle.getRectangle()
            screen.blit(texture, rectangle)