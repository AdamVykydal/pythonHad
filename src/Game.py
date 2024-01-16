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
from Counter import Counter
from LoadResources import LoadResources


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.running = True
        self.clock = pygame.time.Clock()
        self.loadResources = LoadResources()
        self.snakeTexture = self.loadResources.loadImage("snakeBody.png")
        self.enemySnakeTexture = self.loadResources.loadImage("enemySnakeBody.png")
        self.fruitTexture1 = self.loadResources.loadImage("redApple.png")
        self.fruitTexture2 = self.loadResources.loadImage("greenApple.png")
        self.snakeCoords = Coords(500, 500)
        self.renderer = Renderer()
        self.fruits = Fruits()
        self.score = Score()
        self.snakeHead = SnakeHead(self.snakeCoords)
        self.snake = Snake(self.snakeHead)
        self.gameEvents = GameEvents(self.snakeHead)
        self.collisions = Collisions(
            self.snakeHead, self.snake, self.fruits, self.score, self)
        self.fruits.newFruit()
        self.snakeParts = self.snake.getSnakeParts()
        self.client = None
        self.enemySnakeParts = None
        self.recievedData = None
        self.fruitbasket = None
        self.gameStartMenu = GameStartMenu(self.screen)
        self.multiplayerMenu = MutiplayerMenu(self.screen)
        self.counter = Counter(self.screen)
        self.collisionsInfoFromServer = [0,0,0]
        self.multiplayerScore = [0,0]

    def run(self):

        pressedButton = self.gameStartMenu.createMenu()

        if pressedButton == "singleplayerButton":
            self.singlplayergameLoop()
        elif pressedButton == "multiplayerButton":
            while True:
                pressedButton = self.multiplayerMenu.createMenu()
                if pressedButton == "connectButton":
                    
                    serverConected = self.connectToGameServer(self.multiplayerMenu.userText)
                    if serverConected:
                        self.multiplayergameLoop()
                    
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
    
    def multiplayergameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsMultiplayer()

            self.update()

            self.networking()

            self.multiplayerRenderer()

            pygame.display.update()

            self.clock.tick(10)

    def singlplayergameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsSingleplayer()

            self.update()

            self.singlplayerRenderer()

            pygame.display.update()

            self.clock.tick(10)

    def networking(self):
        self.client.prepareDataForSend(self.snakeParts)
        self.client.sendData()
        self.collisionsInfoFromServer, self.multiplayerScore, self.enemySnakeParts, self.fruitbasket = self.client.reciveData()

    def handleEventsSingleplayer(self):
        self.gameEvents.keyEvents()
        self.collisions.snakeAndFruit()
        self.collisions.snakeAndTail()

    def handleEventsMultiplayer(self):
        self.gameEvents.keyEvents()
        self.collisions.snakeAndServerFruit(self.collisionsInfoFromServer[0])

    def update(self):
        self.snake.snakeMove()
        self.snakeHead.moveSnakeHead()
        self.snakeParts = self.snake.getSnakeParts()
        self.collisions.snakeAndWall()

    def singlplayerRenderer(self):
        self.renderer.renderFruits(
            self.screen, self.fruitTexture1, self.fruitTexture2, self.fruits.fruitBasket
        )
        self.renderer.renderObjects(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.counter.renderCounter(str(self.score.points))

    def multiplayerRenderer(self):
        self.renderer.renderServerObject(
            self.screen, self.fruitTexture1, self.fruitbasket
        )
        self.renderer.renderObjects(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.renderer.renderServerObject(
            self.screen, self.enemySnakeTexture, self.enemySnakeParts
        )
        self.counter.renderMultiplayerCouter(self.multiplayerScore)
