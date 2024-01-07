# pylint: disable=invalid-name
import time
import pygame
from Game import Game
from GameStartMenu import GameStartMenu


pygame.init()

screen = pygame.display.set_mode((1920, 1080))  # pygame.FULLSCREEN

gameStartMenu = GameStartMenu(screen)

gameMode = gameStartMenu.createMenu()

game = Game(screen)

if gameMode == "singleplayer":
    game.singlplayergameLoop()
elif gameMode == "mutilplayer":
    game.connectToGameServer()
    game.multiplayergameLoop()

time.sleep(5)

pygame.quit()
