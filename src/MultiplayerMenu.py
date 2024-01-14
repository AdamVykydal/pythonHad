import sys
import pygame
from Text import Text
from InputBox import InputBox


class MutiplayerMenu:
    def __init__(self, screen):
        self.buttonsFont = pygame.font.SysFont("arialBlack", 40)
        self.hFont = pygame.font.SysFont("arialBlack", 80, bold=True)
        self.primarTextColor = (255, 255, 255)
        self.secondTextColor = (50, 0, 205)
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.menu = True
        self.userText = ""
        self.ipBoxActive = False
        self.menuTitle = Text(1920 / 2, 1080 - 850, "multiplayerMenuTitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, "MULTIPLAYER", self.screen)
        self.ipBoxTitle = Text(1920 / 2, 1080 - 600, "IpBoxTitle",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Enter server ip Adress:", self.screen)
        self.play = Text(1920 / 2 - 300, 1080 - 200, "playButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Connect to server", self.screen)
        self.back = Text(1920 / 2 + 300, 1080 - 200, "backButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Back", self.screen)
        self.ipBox = InputBox(1920 / 2, 1080 - 500, "Ip",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, self.screen, 10, 10)
        
        self.allMenuButtons = (self.play, self.back)

    def createMenu(self):

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
                            return menuButton.name

                if event.type == pygame.KEYDOWN and self.ipBoxActive:
                        
                    keys = pygame.key.get_pressed()

                        
                    if keys[pygame.K_BACKSPACE]:
                            
                        self.userText = self.userText[:-1]

                    else:
                        self.userText += event.unicode
                        
            
            pygame.display.update()
