import pygame
import time
import sys


class GameStartMenu:
    def __init__(self, screen):
        self.menu = True
        self.screen = screen

        pygame.display.set_caption("main menu")
        self.font = pygame.font.SysFont("arialblack", 40)
        self.textColor = (255, 255, 255)
        self.clock = pygame.time.Clock()

    def drawText(self, text, font, textColor, x, y):
        img = font.render(text, True, textColor)
        textRectangle = img.get_rect(center=(x, y))
        self.screen.blit(img, textRectangle)
        return textRectangle

    def createMenu(self):
        
        while self.menu:
            self.clock.tick(10)
            self.screen.fill((0, 0, 0))
            self.singlplayerButton = self.drawText("Singlplayer", self.font, self.textColor, 1920 / 2, 1080 / 4)
            self.multiplayerButton = self.drawText("Multiplayer", self.font, self.textColor, 1920 / 2, 1080 / 3)
            self.settingsButton = self.drawText("Settings", self.font, self.textColor, 1920 / 2, 1080 / 2)

            mousePosition = pygame.mouse.get_pos()
            print(mousePosition)
            print(self.singlplayerButton)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("pressed-------------------------------------------------------pres")
                    if self.singlplayerButton.collidepoint(mousePosition):
                        print("------------------------------------------")
                        self.menu = False
                        return
            
            """ if self.singlplayerButton.collidepoint(mousePosition):
                if pygame.mouse.get_pressed()[0] == 1:
                    print("------------------------------------------")
                    self.menu = False
                    return"""
           
           
            pygame.display.update()
            