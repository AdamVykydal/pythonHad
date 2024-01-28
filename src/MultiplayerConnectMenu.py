import sys
import pygame
from Text import Text
from InputBox import InputBox
from MenuConst import MenuConst


class MutiplayerConnectMenu:
    def __init__(self, screen, screenSize):
        self.menuConst = MenuConst()
        self.buttonsFont = self.menuConst.normalFont()
        self.hFont = self.menuConst.bigFont()
        self.primarTextColor = self.menuConst.primaryColour()
        self.secondTextColor = self.menuConst.secondaryColour()
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.screenSize = screenSize
        self.menu = True
        self.menuTitle = Text(screenSize.width / 2, screenSize.height - 850, "multiplayerMenuTitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, "MULTIPLAYER", self.screen)
        self.ipBoxTitle = Text(screenSize.width / 2, screenSize.height - 450, "ipBoxTitle",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Enter server ip Adress:", self.screen)
        self.nameBoxTitle = Text(screenSize.width / 2, screenSize.height - 650, "nameBoxTitle",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Enter name for your snake:", self.screen)
        self.connectingText = Text(screenSize.width / 2, screenSize.height - 100, "ConnectingText",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Trying to contact server...", self.screen)
        self.play = Text(screenSize.width / 2 - 300, screenSize.height - 200, "connectButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Connect to server", self.screen)
        self.back = Text(screenSize.width / 2 + 300, screenSize.height - 200, "backButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Back", self.screen)
        self.ipBox = InputBox(screenSize.width / 2, screenSize.height - 350, "Ip",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, self.screen, 10, 10)
        self.nameBox = InputBox(screenSize.width / 2, screenSize.height - 550, "Ip",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, self.screen, 10, 10)
        
        self.allMenuButtons = (self.play, self.back)
        self.allinputBoxes = (self.ipBox, self.nameBox)

    def goMenu(self):

        for menuButton in self.allMenuButtons:
            menuButton.renderText()
        
        for inputBox in self.allinputBoxes:
            inputBox.renderInputBox()
        
        while True:
            self.screen.fill((0, 0, 0))
            
            self.clock.tick(30)

            self.menuTitle.renderText()
            self.ipBoxTitle.renderText()
            self.nameBoxTitle.renderText()

            mousePosition = pygame.mouse.get_pos()

            for menuButton in self.allMenuButtons:
                if menuButton.rectangle.collidepoint(mousePosition):
                    menuButton.renderSecondColorText()
                else:
                    menuButton.renderText()
            
            for inputBox in self.allinputBoxes:
                if inputBox.active:
                    inputBox.renderSecondColorInputBox()
                else:
                    inputBox.renderInputBox()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
        
                    for inputBox in self.allinputBoxes:
                        if inputBox.boxRectangle.collidepoint(mousePosition):
                            inputBox.active = True
                        else:
                            inputBox.active = False
            
                    for menuButton in self.allMenuButtons:
                        if menuButton.rectangle.collidepoint(mousePosition):
                            if menuButton.name == "connectButton":
                                if self.ipBox.text != "" and self.nameBox.text != "":
                                    self.connectingText.renderText()
                                    pygame.display.update()
                                    return menuButton.name
                            else:
                                return menuButton.name
                            

                for inputBox in self.allinputBoxes:
                    if event.type == pygame.KEYDOWN and inputBox.active:   
                        keys = pygame.key.get_pressed()
                            
                        if keys[pygame.K_BACKSPACE]: 
                            inputBox.text = inputBox.text[:-1]

                        else:
                            inputBox.text += event.unicode
            
            pygame.display.update()
