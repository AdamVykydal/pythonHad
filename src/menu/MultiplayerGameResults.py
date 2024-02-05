import sys
import pygame
from menu.MenuConst import MenuConst
from menuObjects.Text import Text


class MultiplayerGameResults:
    def __init__(self, screen, screenSize):
        self.screenSize = screenSize
        self.menuConst = MenuConst()
        self.buttonsFont = self.menuConst.normalFont()
        self.hFont = self.menuConst.bigFont()
        self.plusMinusFont = self.menuConst.plusMinusFont()
        self.primarTextColor = self.menuConst.primaryColour()
        self.secondTextColor = self.menuConst.secondaryColour()
        self.screen = screen
        self.winner = None
        self.resultText = ""
        self.clock = pygame.time.Clock()
        
        
        self.gameResultTitle = Text(self.screenSize.width / 2, self.screenSize.height - 850, "",
                              self.hFont, self.primarTextColor, self.secondTextColor,"", self.screen)
        self.okButton = Text(self.screenSize.width / 2 , self.screenSize.height - 200, "okButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "OK", self.screen)
        self.snake1Text = Text(self.screenSize.width / 2 - 250 , self.screenSize.height - 700, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.snake2Text = Text(self.screenSize.width / 2 + 250, self.screenSize.height - 700, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        
        self.pointsText = Text(self.screenSize.width / 2 , self.screenSize.height - 600, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, ": Points :", self.screen)
        self.snake1PointsText = Text(self.screenSize.width / 2 - 250 , self.screenSize.height - 600, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.snake2PointsText = Text(self.screenSize.width / 2 + 250, self.screenSize.height - 600, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        
        self.lenghtText = Text(self.screenSize.width / 2 , self.screenSize.height - 500, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, ": Lenght :", self.screen)
        self.snake1LenghtText = Text(self.screenSize.width / 2 - 250 , self.screenSize.height - 500, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.snake2LenghtText = Text(self.screenSize.width / 2 + 250, self.screenSize.height - 500, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        
        self.fruitsText = Text(self.screenSize.width / 2 , self.screenSize.height - 400, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, ": Fruits :", self.screen)
        self.snake1FruitsText = Text(self.screenSize.width / 2 - 250 , self.screenSize.height - 400, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.snake2FruitsText = Text(self.screenSize.width / 2 + 250, self.screenSize.height - 400, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
    
    def chooseResultText(self, snake1Statistics, snake2Statistics):
        if self.winner == 1:
            self.resultText = (snake1Statistics["name"]," is Winner!")
        elif self.winner == 2:
            self.resultText = (snake2Statistics["name"]," is Winner!")
        else:
            self.resultText = "The match ended in a draw"
    
    def goMenu(self, winner, snake1Statistics ,snake2Statistics):
        
        self.winner = winner
        
        self.chooseResultText(snake1Statistics, snake2Statistics)
        
        self.okButton.renderText()
        
        while True:
            
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
            
            self.gameResultTitle.renderDynamicText(self.resultText)
            
            self.snake1Text.renderDynamicText(snake1Statistics["name"])
            self.snake2Text.renderDynamicText(snake2Statistics["name"])
            
            self.pointsText.renderText()
            
            self.snake1PointsText.renderDynamicText(snake1Statistics["points"])
            self.snake2PointsText.renderDynamicText(snake2Statistics["points"])

            self.lenghtText.renderText()
            
            self.snake1LenghtText.renderDynamicText(snake1Statistics["lenght"])
            self.snake2LenghtText.renderDynamicText(snake2Statistics["lenght"])
            
            self.fruitsText.renderText()
            
            self.snake1FruitsText.renderDynamicText(snake1Statistics["fruits"])
            self.snake2FruitsText.renderDynamicText(snake2Statistics["fruits"])
            
            
            mousePosition = pygame.mouse.get_pos()
            
            if self.okButton.rectangle.collidepoint(mousePosition):
                self.okButton.renderSecondColorText()
            else:
                self.okButton.renderText()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.okButton.rectangle.collidepoint(mousePosition):
                        return self.okButton.name
            
            pygame.display.update()
            


