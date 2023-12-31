import pygame


class Render:
    def __init__(self):
        None
    
    def renderObject(self, screen, texture, rectangle):
        screen.blit(texture, rectangle)
    