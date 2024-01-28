import sys
import pygame
from Text import Text
from Image import Image
from MenuConst import MenuConst


class MutiplayerMenu:
    def __init__(self, screen, screenSize):
        self.menuConst = MenuConst()
        self.primarTextColor = self.menuConst.primaryColour()
        self.secondTextColor = self.menuConst.secondaryColour()
        self.buttonsFont = self.menuConst.normalFont()
        self.hFont = self.menuConst.bigFont()
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.screenSize = screenSize
        self.menu = True
        self.userText = ""
        self.ipBoxActive = False
        self.menuTitle = Text(screenSize.width / 2, screenSize.height - 850, "multiplayerMenuTitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, "MULTIPLAYER", self.screen)
        self.startServerMenuButton = Image(screenSize.width / 2 + 400, screenSize.height -500, 300, 300, "startServerMenuButton","server.png", "serverPressed.png", self.screen)
        self.connectToServerMenuButton = Image(screenSize.width / 2, screenSize.height -500, 300, 300, "connectToServerMenuButton", "ConnectToServer.png", "ConnectToServerPressed.png", self.screen)
        self.localGameMenuButton = Image(screenSize.width / 2 - 400, screenSize.height - 500, 300, 300,"localGameMenuButton", "localGame.png", "localGamePressed.png", self.screen)
        self.backButton = Text(screenSize.width / 2 + 300, screenSize.height - 200, "backButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Back", self.screen)
        
        self.allImageMenuButtons = (self.startServerMenuButton, self.connectToServerMenuButton, self.localGameMenuButton)
    
    def goMenu(self):

        self.backButton.renderText()
        
        while True:
            self.screen.fill((0, 0, 0))
            
            self.clock.tick(30)

            self.menuTitle.renderText()
            
            mousePosition = pygame.mouse.get_pos()

            if self.backButton.rectangle.collidepoint(mousePosition):
                self.backButton.renderSecondColorText()
            else:
                self.backButton.renderText()
            
            for imageButton in self.allImageMenuButtons:
                if imageButton.rectangle.collidepoint(mousePosition):
                    imageButton.renderSecondaryColorImage()
                else:
                    imageButton.renderImage()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for imageButton in self.allImageMenuButtons:
                        if imageButton.rectangle.collidepoint(mousePosition):
                            return imageButton.name
                    if self.backButton.rectangle.collidepoint(mousePosition):
                        return self.backButton.name
                        
            pygame.display.update()
