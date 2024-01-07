import pygame
from Game import Game
from GameStartMenu import GameStartMenu
import time

pygame.init()

screen = pygame.display.set_mode((1920, 1080)) #pygame.FULLSCREEN

gameStartMenu = GameStartMenu(screen)

gameStartMenu.createMenu()

game = Game(screen)

game.SinglplayergameLoop()

time.sleep(5)

pygame.quit()