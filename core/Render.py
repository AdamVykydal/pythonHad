import pygame


class Render:
    def __init__(self):
        None
    
    def renderObject(self, screen, texture, rectangle):
        screen.blit(texture, rectangle)
    def renderSnake(self, screen, texture, rectangles):
        print("--------------------------------")
        for rectangle in rectangles:
            print(rectangle, ":", rectangle.getRectangle())
            rectangle = rectangle.getRectangle()
            screen.blit(texture, rectangle)
    