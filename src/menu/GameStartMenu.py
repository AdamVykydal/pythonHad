import sys
import pygame
from menuObjects.Text import Text
from recources.LoadResources import LoadResources
from menu.MenuConst import MenuConst


class GameStartMenu:
    def __init__(self, screen, screenSize):
        self.screenSize = screenSize
        self.menuConst = MenuConst()
        self.buttonsFont = self.menuConst.normalFont()
        self.hFont = self.menuConst.bigFont()
        self.primarTextColor = self.menuConst.primaryColour()
        self.secondTextColor = self.menuConst.secondaryColour()
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.menu = True
        self.loadResources = LoadResources()   
        
        self.menuTitle = Text(self.screenSize.width / 2, self.screenSize.height - 850, "menuTitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, "SNAKE", self.screen)
        self.singleplayerButton = Text(self.screenSize.width / 2, self.screenSize.height - 700, "singleplayerButton",
                                       self.buttonsFont, self.primarTextColor, self.secondTextColor, "Singleplayer", self.screen)
        self.multiplayerButton = Text(self.screenSize.width / 2, self.screenSize.height - 600, "multiplayerButton",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Multiplayer", self.screen)
        self.settingsButton = Text(self.screenSize.width / 2, self.screenSize.height - 500, "settingsButton",
                                   self.buttonsFont, self.primarTextColor, self.secondTextColor, "Settings", self.screen)
        self.endButton = Text(self.screenSize.width / 2, self.screenSize.height - 400, "endButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "End", self.screen)

        self.allMenuButtons = (
            self.singleplayerButton, self.multiplayerButton, self.settingsButton, self.endButton)

    def goMenu(self):

        self.screen.fill((0, 0, 0))

        for menuButton in self.allMenuButtons:
            menuButton.renderText()

        while True:
            
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
            
            
            self.menuTitle.renderText()

            mousePosition = pygame.mouse.get_pos()   
            
            for menuButton in self.allMenuButtons:
                if menuButton.rectangle.collidepoint(mousePosition):
                    menuButton.renderSecondColorText()
                else:
                    menuButton.renderText()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for menuButton in self.allMenuButtons:
                        if menuButton.rectangle.collidepoint(mousePosition):
                            return menuButton.name

            pygame.display.update()
            

