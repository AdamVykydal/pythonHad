import sys
import pygame
from menuObjects.Text import Text
from menu.MenuConst import MenuConst


class GameRoomMenu:
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
        self.playersReady = [0,0]
        self.playerNames = ["",""]
        self.gameOptionsChanges = [0, 0, 0]
        self.playerId = None

        self.gameOptions = [100, 0, 0]
        
        self.roomTitle = Text(self.screenSize.width / 2, self.screenSize.height - 850, "roomtitle",
                              self.hFont, self.primarTextColor, self.secondTextColor,"", self.screen)
        self.snakeText1  = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 700, "SnakeButton1",
                                       self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.snakeText2 = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 600, "SnakeButton2",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.leaveButton = Text(self.screenSize.width / 2 + 300, self.screenSize.height - 200, "leaveLobbyButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Leave lobby", self.screen)
        self.readyButton = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 200, "readyButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Ready", self.screen)
        self.gameSettingsText = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 800, "gameSettings",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Play options:", self.screen)
        
        self.playTimeHeader = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 700, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Play time:", self.screen)
        self.playTimeText = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 650, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.playTimePlusButton = Text(self.screenSize.width / 2 + 800, self.screenSize.height - 650, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "+", self.screen)
        self.playTimeMinusButton = Text(self.screenSize.width / 2 + 600, self.screenSize.height - 650, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "-", self.screen)
        
        self.winConditionHeader = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 550, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "Win condition:", self.screen)
        self.winConditionText = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 500, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.winConditionPlusButton = Text(self.screenSize.width / 2 + 800, self.screenSize.height - 500, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "+", self.screen)
        self.winConditioneMinusButton = Text(self.screenSize.width / 2 + 600, self.screenSize.height - 500, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "-", self.screen)
        
        self.lossConditionHeader = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 400, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "loss condition:", self.screen)
        self.lossConditionText = Text(self.screenSize.width / 2 + 700, self.screenSize.height - 350, "",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.lossConditionPlusButton = Text(self.screenSize.width / 2 + 800, self.screenSize.height - 350, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "+", self.screen)
        self.lossConditionMinusButton = Text(self.screenSize.width / 2 + 600, self.screenSize.height - 350, "",
                                      self.plusMinusFont, self.primarTextColor, self.secondTextColor, "-", self.screen)
        
        
        self.twoColorMenuButtons = (self.leaveButton, self.playTimePlusButton, self.playTimeMinusButton, self.winConditioneMinusButton, self.winConditionPlusButton, self.lossConditionMinusButton, self.lossConditionPlusButton)
        self.staticText =(self.roomTitle, self.playTimeHeader, self.winConditionHeader, self.lossConditionHeader, self.gameSettingsText)

    def goMenu(self, client, playerName, roomName):
        self.screen.fill((0, 0, 0))
        
        self.readyButton.pressed = 0

        for button in self.twoColorMenuButtons:
            button.renderText()
    
        while True:
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
            
            self.roomTitle.renderDynamicText(roomName)

            self.playTimeText.renderDynamicText(self.gameOptions[0])
            
            #pygame.draw.rect(self.screen, self.primarTextColor, (1400, 325, 500, 500), 2)
            
            
            for text in self.staticText:
                text.renderText()
            
            if self.playersReady[0] == 1:
                self.snakeText1.renderDynamicText((str(self.playerNames[0]) + ": Ready"))
            else:
                self.snakeText1.renderDynamicText((str(self.playerNames[0]) +":"))
            
            if self.playersReady[1] == 1:
                self.snakeText2.renderDynamicText((str(self.playerNames[1]) + ": Ready"))
            else:
                self.snakeText2.renderDynamicText((str(self.playerNames[1]) +":"))
            
            mousePosition = pygame.mouse.get_pos()

            for button in self.twoColorMenuButtons:
                if button.rectangle.collidepoint(mousePosition):
                    button.renderSecondColorText()
                else:
                    button.renderText()
           
            if self.readyButton.pressed:
                self.readyButton.renderSecondColorText()
            else:
                self.readyButton.renderText()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.leaveButton.rectangle.collidepoint(mousePosition):
                        return self.leaveButton.name
                    
                    if self.readyButton.rectangle.collidepoint(mousePosition) and self.readyButton.pressed:
                        self.readyButton.pressed = 0
                        
                    elif self.readyButton.rectangle.collidepoint(mousePosition) and not self.readyButton.pressed :
                        self.readyButton.pressed = 1
                       
                    elif self.playTimePlusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[0] < 600:
                            self.gameOptionsChanges[0] = 1
                    
                    elif self.playTimeMinusButton.rectangle.collidepoint(mousePosition):
                        if self.gameOptions[0] > 10:
                            self.gameOptionsChanges[0] = -1
            
            client.sendMenuData([self.readyButton.pressed, playerName, self.gameOptionsChanges])
            self.playerId, self.playersReady, self.playerNames, self.gameOptions= client.reciveMenuData()
            
            self.gameOptionsChanges = [0, 0, 0]
        
            if self.playersReady == [1, 1]:
                return "start"
           
            pygame.display.update()
            