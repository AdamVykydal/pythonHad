import sys
import pygame
from menuObjects.Text import Text
from menu.MenuConst import MenuConst


class LocalGameRoomMenu:
    def __init__(self, screen, screenSize):
        self.screenSize = screenSize
        self.menuConst = MenuConst()
        self.buttonsFont = self.menuConst.normalFont()
        self.hFont = self.menuConst.bigFont()
        self.plusMinusFont = self.menuConst.plusMinusFont()
        self.primarTextColor = self.menuConst.primaryColour()
        self.secondTextColor = self.menuConst.secondaryColour()
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.gameOptions = [100, 50, -5]
        
        self.roomTitle = Text(self.screenSize.width / 2, self.screenSize.height - 850, "roomtitle",
                              self.hFont, self.primarTextColor, self.secondTextColor,"Local game for two", self.screen)
        self.backButton = Text(self.screenSize.width / 2 + 300, self.screenSize.height - 200, "backButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Back", self.screen)
        self.playButton = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 200, "playButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Play toghether!", self.screen)
        
        self.playTimeHeader = Text(self.screenSize.width / 2, self.screenSize.height - 700, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Play time:", self.screen)
        self.playTimeText = Text(self.screenSize.width / 2, self.screenSize.height - 650, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.playTimePlusButton = Text(self.screenSize.width / 2 + 100, self.screenSize.height - 650, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "+", self.screen)
        self.playTimeMinusButton = Text(self.screenSize.width / 2 - 100, self.screenSize.height - 650, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "-", self.screen)
        
        self.winConditionHeader = Text(self.screenSize.width / 2, self.screenSize.height - 550, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Win condition:", self.screen)
        self.winConditionText = Text(self.screenSize.width / 2, self.screenSize.height - 500, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.winConditionPlusButton = Text(self.screenSize.width / 2 + 100, self.screenSize.height - 500, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "+", self.screen)
        self.winConditioneMinusButton = Text(self.screenSize.width / 2 - 100, self.screenSize.height - 500, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "-", self.screen)
        
        self.lossConditionHeader = Text(self.screenSize.width / 2, self.screenSize.height - 400, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "loss condition:", self.screen)
        self.lossConditionText = Text(self.screenSize.width / 2, self.screenSize.height - 350, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.lossConditionPlusButton = Text(self.screenSize.width / 2 + 100, self.screenSize.height - 350, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "+", self.screen)
        self.lossConditionMinusButton = Text(self.screenSize.width / 2 - 100, self.screenSize.height - 350, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "-", self.screen)
        
        
        self.twoColorMenuButtons = (self.backButton, self.playTimePlusButton, self.playTimeMinusButton, self.winConditioneMinusButton,
                                     self.winConditionPlusButton, self.lossConditionMinusButton, self.lossConditionPlusButton, self.playButton)
        self.staticText =(self.roomTitle, self.playTimeHeader, self.winConditionHeader, self.lossConditionHeader, self.playButton,)

    def goMenu(self):
        self.screen.fill((0, 0, 0))

        for button in self.twoColorMenuButtons:
            button.renderText()
    
        while True:
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
            
            self.roomTitle.renderText()
            
            self.playTimeText.renderDynamicText(self.gameOptions[0])
            self.winConditionText.renderDynamicText(self.gameOptions[1])
            self.lossConditionText.renderDynamicText(self.gameOptions[2])
            
            for text in self.staticText:
                text.renderText()
            
            mousePosition = pygame.mouse.get_pos()

            for button in self.twoColorMenuButtons:
                if button.rectangle.collidepoint(mousePosition):
                    button.renderSecondColorText()
                else:
                    button.renderText()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.backButton.rectangle.collidepoint(mousePosition):
                        return self.backButton.name
                    elif self.playButton.rectangle.collidepoint(mousePosition):
                        return self.playButton.name
                    
                    elif self.playTimePlusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[0] < 600:
                            self.gameOptions[0] += 1
                    
                    elif self.playTimeMinusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[0] > 10:
                            self.gameOptions[0] -= 1
                    
                    elif self.winConditionPlusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[1] < 500:
                            self.gameOptions[1] += 1
        
                    elif self.winConditioneMinusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[1] > 10:
                            self.gameOptions[1] -= 1
                    
                    elif self.lossConditionPlusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[2] < -1:
                            self.gameOptions[2] += 1
                    
                    elif self.lossConditionMinusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[2] > -100:
                            self.gameOptions[2] -= 1
           
            pygame.display.update()
            