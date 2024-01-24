import sys
import pygame
from Renderer import Renderer
from GameEvents import GameEvents
from SnakeHead import SnakeHead
from Snake import Snake
from Collisions import Collisions
from Score import Score
from Fruits import Fruits
from definitions import IMG_DIR
from Client import Client
from Coords import Coords
from GameStartMenu import GameStartMenu
from MultiplayerMenu import MutiplayerMenu
from InfoBoard import GameInfoBoard
from LoadResources import LoadResources
from ScreenSize import ScreenSize
from GameRoomMenu import GameRoomMenu
import time


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screenWidth, self.screenHeight = self.screen.get_size()
        self.screenSize = ScreenSize(self.screenWidth, self.screenHeight)
        self.running = True
        self.clock = pygame.time.Clock()
        self.loadResources = LoadResources()
        self.snakeTexture = self.loadResources.loadImage("snakeBody.png")
        self.enemySnakeTexture = self.loadResources.loadImage("enemySnakeBody.png")
        self.fruitTexture1 = self.loadResources.loadImage("redApple.png")
        self.fruitTexture2 = self.loadResources.loadImage("greenApple.png")
        self.snakeCoords = Coords(500, 500)
        self.snakeHead = SnakeHead(self.snakeCoords)
        self.renderer = Renderer()
        self.fruits = Fruits()
        self.score = Score()
        self.snake = Snake(self.snakeHead)
        self.gameEvents = GameEvents(self.snakeHead)
        self.collisions = Collisions(
            self.snakeHead, self.snake, self.fruits, self.score, self, self.screenSize)
        self.fruits.newFruit()
        self.snakeParts = self.snake.getSnakeParts()
        self.client = None
        self.enemySnakeParts = None
        self.recievedData = None
        self.fruitbasket = None
        self.gameStartMenu = GameStartMenu(self.screen, self.screenSize)
        self.multiplayerMenu = MutiplayerMenu(self.screen, self.screenSize)
        self.gameRoomMenu = GameRoomMenu(self.screen, self.screenSize)
        self.gameInfoBoard = GameInfoBoard(self.screen, self.screenSize)
        self.collisionsInfoFromServer = [0,0,0]
        self.multiplayerScore = [0,0]
        self.startTime = time.time()
        self.currentTime = 0
        self.snake.addSnakePart()
        self.running = False
        self.playTime = 0
        
    def run(self):

        pressedButton = self.gameStartMenu.goMenu()

        if pressedButton == "singleplayerButton":
            self.singlplayergameLoop()
        elif pressedButton == "multiplayerButton":
            while True:
                pressedButton = self.multiplayerMenu.goMenu()
                if pressedButton == "connectButton":
                    serverConected = self.connectToGameServer(self.multiplayerMenu.userText)
                    print(serverConected, self.client)
                    if serverConected:
                        while True:
                            pressedButton = self.gameRoomMenu.goMenu(self.client)
                            if pressedButton == "start":
                                self.running = True
                                self.clearMultiplayer()
                                self.multiplayergameLoop()
                            elif pressedButton == "leaveLobbyButton":
                                #disconnect
                                break

                    
                elif pressedButton == "backButton":
                    break
        elif pressedButton == "endButton":
            self.running = False
            pygame.quit()
            sys.exit()

    def connectToGameServer(self, serverIp):
        self.client = Client(serverIp, 11111)
        serverConected = self.client.connectToServer()
        return serverConected
    
    def clearMultiplayer(self):
        self.snakeHead.coords = Coords(500,500)
        self.snakeHead.direction = self.snakeHead.directionRight
        self.snake.restartSnake(self.snakeHead)
        self.fruits.emptyFruitBasket()
        
    def multiplayergameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsMultiplayer()

            self.update()

            self.networking()

            self.multiplayerRenderer()

            pygame.display.update()

            self.clock.tick(60)

    def singlplayergameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsSingleplayer()

            self.update()

            self.singlplayerRenderer()

            pygame.display.update()
            
            self.clock.tick(60)

    def networking(self):
        self.client.prepareDataForSend(self.snakeParts)
        self.client.sendSnakeData()
        self.running, self.collisionsInfoFromServer, self.playTime, self.multiplayerScore, self.enemySnakeParts, self.fruitbasket = self.client.reciveGameData()
        
    
    def handleEventsSingleplayer(self):
        self.currentTime = time.time()
        if self.currentTime - self.startTime >= 0.09:
            self.gameEvents.keyEvents()
            self.collisions.snakeAndFruit()
            self.collisions.snakeAndTail()

    def handleEventsMultiplayer(self):
        self.currentTime = time.time()
        if self.currentTime - self.startTime >= 0.09:
            self.gameEvents.keyEvents()
        self.collisions.snakeAndServerFruit(self.collisionsInfoFromServer[0])

    def update(self):
        if self.currentTime - self.startTime >= 0.09:
            self.snake.snakeMove()
            self.snakeHead.moveSnakeHead()
            self.startTime = time.time()
        
        self.snakeParts = self.snake.getSnakeParts()
        self.collisions.snakeAndWall()

    def singlplayerRenderer(self):
        self.renderer.renderFruits(
            self.screen, self.fruitTexture1, self.fruitTexture2, self.fruits.fruitBasket
        )
        self.renderer.renderSnake(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.gameInfoBoard.renderCounter(str(self.score.points))

    def multiplayerRenderer(self):
        self.renderer.renderServerObject(
            self.screen, self.fruitTexture1, self.fruitbasket
        )
        self.renderer.renderSnake(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.renderer.renderServerObject(
            self.screen, self.enemySnakeTexture, self.enemySnakeParts
        )
        self.gameInfoBoard.renderMultiplayerCouter(self.multiplayerScore)
        self.gameInfoBoard.renderMultiplayerClock(self.playTime)
