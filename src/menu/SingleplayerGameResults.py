import sys
import pygame
from menu.MenuConst import MenuConst
from menuObjects.Text import Text


class SingleplayerGameResults:
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
                              self.hFont, self.primarTextColor, self.secondTextColor,"Game over", self.screen)
        self.okButton = Text(self.screenSize.width / 2 , self.screenSize.height - 200, "okButton",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "OK", self.screen)
        self.gameLenghtText = Text(self.screenSize.width / 2 , self.screenSize.height - 700, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        self.pointsText = Text(self.screenSize.width / 2 , self.screenSize.height - 600, "",
                              self.buttonsFont, self.primarTextColor, self.secondTextColor, "", self.screen)
        
    def goMenu(self, points, stopwatch):
        
        hours, minutes, seconds = stopwatch.getFormatedTime()
        self.okButton.renderText()
        
        while True:
            
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
            
            self.gameResultTitle.renderText()

            self.gameLenghtText.renderDynamicText("Play Time: " + str(hours) + ":" + str(minutes) + ":" + str(seconds))
            
            self.pointsText.renderDynamicText("Score: " + str(points))
            
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