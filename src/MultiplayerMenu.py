import sys
import pygame
from Text import Text
from InputBox import InputBox


class MutiplayerMenu:
    def __init__(self, screen, screenSize):
        self.buttonsFont = pygame.font.SysFont("arialBlack", 40)
        self.hFont = pygame.font.SysFont("arialBlack", 80, bold=True)
        self.primarTextColor = (255, 255, 255)
        self.secondTextColor = (50, 0, 205)
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.screenSize = screenSize
        self.menu = True
        self.userText = ""
        self.ipBoxActive = False
        self.menuTitle = Text(screenSize.width / 2, screenSize.height - 850, "multiplayerMenuTitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, "MULTIPLAYER", self.screen)
        self.ipBoxTitle = Text(screenSize.width / 2, screenSize.height - 600, "IpBoxTitle",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Enter server ip Adress:", self.screen)
        self.connectingText = Text(screenSize.width / 2, screenSize.height - 400, "ConnectingText",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Trying to contact server...", self.screen)
        self.play = Text(screenSize.width / 2 - 300, screenSize.height - 200, "connectButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Connect to server", self.screen)
        self.back = Text(screenSize.width / 2 + 300, screenSize.height - 200, "backButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Back", self.screen)
        self.ipBox = InputBox(screenSize.width / 2, screenSize.height - 500, "Ip",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, self.screen, 10, 10)
        
        self.allMenuButtons = (self.play, self.back)

    def goMenu(self):

        for menuButton in self.allMenuButtons:
            menuButton.renderText()
        
        self.ipBox.renderInputBox(self.userText)
        
        while True:
            self.screen.fill((0, 0, 0))
            
            self.clock.tick(30)

            self.menuTitle.renderText()
            self.ipBoxTitle.renderText()

            mousePosition = pygame.mouse.get_pos()

            for menuButton in self.allMenuButtons:
                if menuButton.textRectangle.collidepoint(mousePosition):
                    menuButton.renderSecondColorText()
                else:
                    menuButton.renderText()
            if self.ipBoxActive:
                self.ipBox.renderSecondColorInputBox(self.userText)
            else:
                 self.ipBox.renderInputBox(self.userText)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
        
                    if self.ipBox.boxRectangle.collidepoint(mousePosition):
                        self.ipBoxActive = True
                    else:
                        self.ipBoxActive = False
            
                    for menuButton in self.allMenuButtons:
                        if menuButton.textRectangle.collidepoint(mousePosition):
                            if menuButton.name == "connectButton" and self.userText != "":
                                self.connectingText.renderText()
                                pygame.display.update()
                            
                            return menuButton.name

                if event.type == pygame.KEYDOWN and self.ipBoxActive:
                        
                    keys = pygame.key.get_pressed()

                        
                    if keys[pygame.K_BACKSPACE]:
                            
                        self.userText = self.userText[:-1]

                    else:
                        self.userText += event.unicode
                        
            
            pygame.display.update()
