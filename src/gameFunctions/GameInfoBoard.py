import pygame


class GameInfoBoard:
    def __init__(self, screen, screenSize):
        self.font = pygame.font.SysFont("arialBlack", 40)
        self.primarTextColor = (200, 200, 200)
        self.secondTextColor = (0, 0, 255)
        self.enemyTextColor = ("yellow")
        self.textRectangle = None
        self.screen = screen
        self.screenSize = screenSize
    
    def renderCounter(self, points):
        img = self.font.render(points, True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(self.screenSize.width /2, self.screenSize.height - 50))
        self.screen.blit(img, self.textRectangle)
    
    def renderMultiplayerCouter(self, multiplayerScore):
        img = self.font.render(str(multiplayerScore[0]), True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(self.screenSize.width /2 + 200, self.screenSize.height - 50))
        self.screen.blit(img, self.textRectangle)
        img = self.font.render(str(multiplayerScore[1]), True, self.enemyTextColor)
        self.textRectangle = img.get_rect(center=(self.screenSize.width /2 - 200, self.screenSize.height - 50))
        self.screen.blit(img, self.textRectangle)
    
    def renderMultiplayerClock(self, playTime):
        img = self.font.render(str(playTime), True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(self.screenSize.width /2, self.screenSize.height - 50))
        self.screen.blit(img, self.textRectangle)
