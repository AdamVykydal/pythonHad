import pygame


class Counter:
    def __init__(self, screen):
        self.font = pygame.font.SysFont("arialBlack", 40)
        self.primarTextColor = (200, 200, 200)
        self.secondTextColor = (50, 0, 205)
        self.enemyTextColor = ("yellow")
        self.textRectangle = None
        self.screen = screen
    
    def renderCounter(self, points):
        img = self.font.render(points, True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(1920 /2, 1030))
        self.screen.blit(img, self.textRectangle)
    
    def renderMultiplayerCouter(self, multiplayerScore):
        img = self.font.render(str(multiplayerScore[0]), True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(1920 /2 + 100, 1030))
        self.screen.blit(img, self.textRectangle)
        img = self.font.render(str(multiplayerScore[1]), True, self.enemyTextColor)
        self.textRectangle = img.get_rect(center=(1920 /2 - 100, 1030))
        self.screen.blit(img, self.textRectangle)
    
