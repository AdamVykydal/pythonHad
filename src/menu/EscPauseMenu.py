import sys
import pygame
from menu.MenuConst import MenuConst
from menuObjects.Text import Text


class EscPauseMenu:
    def __init__(self, screen, screenSize, playTime):
        self.screenSize = screenSize
        self.menuConst = MenuConst()
        self.normalFont = self.menuConst.normalFont()
        self.smallFont = self.menuConst.smallFont()
        self.primarTextColor = self.menuConst.primaryColour()
        self.secondTextColor = self.menuConst.secondaryColour()
        self.clock = pygame.time.Clock()
        self.playTime = playTime
        self.screen = screen
        self.menu = True
        self.pauseText = Text(screenSize.width / 2, screenSize.height - 850, "pauseText",
                              self.normalFont, self.primarTextColor, self.secondTextColor, "Game is Paused", self.screen)
        self.escInfoText = Text(screenSize.width / 2, screenSize.height - 650, "infoText",
                                self.smallFont, self.primarTextColor, self.secondTextColor, "(Press 'ESC' to continue playing)", self.screen)
        self.exitGameButton = Text(self.screenSize.width / 2, self.screenSize.height - 200, "exitGameButton",
                                   self.normalFont, self.primarTextColor, self.secondTextColor, "Exit Game", self.screen)

        self.allMenuButtons = [self.exitGameButton]

    def go(self):

        self.exitGameButton.renderText()

        while True:
            self.clock.tick(30)

            self.screen.fill((0, 0, 0))
           
            self.pauseText.renderText()
            self.escInfoText.renderText()

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exitGameButton.rectangle.collidepoint(mousePosition):
                        return False

            pygame.display.update()

    def checkIfEscIsPressed(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playTime.startMenuTime()
                    gameIsRunning = self.go()
                    self.playTime.stopMenuTime()
                    return gameIsRunning

        return True
