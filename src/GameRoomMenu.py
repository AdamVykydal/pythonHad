import pygame
from Text import Text
import sys

class GameRoomMenu:
    def __init__(self, screen, screenSize):
        self.screenSize = screenSize
        self.buttonsFont = pygame.font.SysFont("arialBlack", 40)
        self.hFont = pygame.font.SysFont("arialBlack", 80, bold=True)
        self.primarTextColor = (255, 255, 255)
        self.secondTextColor = (50, 0, 205)
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.lobbyName = "ahoj"
        self.playersReady = [0,0]
        
        self.roomTitle = Text(self.screenSize.width / 2, self.screenSize.height - 850, "roomtitle",
                              self.hFont, self.primarTextColor, self.secondTextColor, self.lobbyName, self.screen)
        self.snakeText1  = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 700, "SnakeButton1",
                                       self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.snakeText2 = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 600, "SnakeButton2",
                                      self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.leaveButton = Text(self.screenSize.width / 2 + 300, self.screenSize.height - 200, "leaveLobbyButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Leave lobby", self.screen)
        self.readyButton = Text(self.screenSize.width / 2 - 300, self.screenSize.height - 200, "readyButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "Ready", self.screen)

        self.leaveButton

    def goMenu(self, client):
        self.screen.fill((0, 0, 0))
        
        self.readyButton.pressed = 0

        self.leaveButton.renderText()
    
        self.readyButton.renderText()
        
        while True:
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
            
            self.roomTitle.renderText()

            if self.playersReady[0] == 1:
                self.snakeText1.renderDynamicText(("Snake1:" + "Ready"))
            else:
                self.snakeText1.renderDynamicText(("Snake1:"))
            
            if self.playersReady[1] == 1:
                self.snakeText2.renderDynamicText(("Snake2:" + "Ready"))
            else:
                self.snakeText2.renderDynamicText(("Snake2:"))
            
            mousePosition = pygame.mouse.get_pos()

            if self.readyButton.pressed:
                self.readyButton.renderSecondColorText()
            else:
                self.readyButton.renderText()
            
            
            if self.leaveButton.textRectangle.collidepoint(mousePosition):
                self.leaveButton.renderSecondColorText()
            else:
                self.leaveButton.renderText()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if self.leaveButton.textRectangle.collidepoint(mousePosition):
                        return self.leaveButton.name
                    
                    if self.readyButton.textRectangle.collidepoint(mousePosition) and self.readyButton.pressed:
                        self.readyButton.pressed = 0
                        #return self.readyButton.name, self.readyButton.pressed
                    elif self.readyButton.textRectangle.collidepoint(mousePosition) and not self.readyButton.pressed :
                        self.readyButton.pressed = 1
                        #return self.readyButton.name, self.readyButton.pressed
            
            client.sendMenuData(self.readyButton.pressed)
            self.playersReady = client.reciveMenuData()
            
            if self.playersReady == [1, 1]:
                return "start"
           
            pygame.display.update()
            