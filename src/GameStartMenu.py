import sys
import pygame
from Text import Text


class GameStartMenu:
    def __init__(self, screen):
        self.buttonsFont = pygame.font.SysFont("arialBlack", 40)
        self.hFont = pygame.font.SysFont("arialBlack", 80, bold=True)
        self.primarTextColor = (255, 255, 255)
        self.secondTextColor = (50, 0, 205)
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.menu = True
        self.objectsUpdate = ()
        self.menuTitle = Text(1920 / 2, 1080 - 850, "menuTitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, "SNAKE", self.screen)
        self.singleplayerButton = Text(1920 / 2, 1080 - 700, "singleplayerButton",
                                       self.buttonsFont, self.primarTextColor, self.secondTextColor, "Singleplayer", self.screen)
        self.multiplayerButton = Text(1920 / 2, 1080 - 600, "multiplayerButton",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Multiplayer", self.screen)
        self.settingsButton = Text(1920 / 2, 1080 - 500, "settingsButton",
                                   self.buttonsFont, self.primarTextColor, self.secondTextColor, "Settings", self.screen)
        self.endButton = Text(1920 / 2, 1080 - 300, "endButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "End", self.screen)

        self.allMenuButtons = (
            self.singleplayerButton, self.multiplayerButton, self.settingsButton, self.endButton)

    def createMenu(self):

        self.screen.fill((0, 0, 0))
        
        for menuButton in self.allMenuButtons:
            menuButton.renderText()
        
        while True:
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))

            self.menuTitle.renderText()

            mousePosition = pygame.mouse.get_pos()

            for menuButton in self.allMenuButtons:
                if menuButton.textRectangle.collidepoint(mousePosition):
                    menuButton.renderSecondColorText()
                else:
                    menuButton.renderText()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for menuButton in self.allMenuButtons:
                        if menuButton.textRectangle.collidepoint(mousePosition):
                            return menuButton.name
        
            pygame.display.update()
            
