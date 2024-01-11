from os import path
import pygame
from Renderer import Renderer
from GameEvents import GameEvents
from SnakeBody import SnakeHead
from Snake import Snake
from Collisions import Collisions
from Score import Score
from Fruits import Fruits
from definitions import IMG_DIR
from Client import Client
from Coords import Coords
from GameStartMenu import GameStartMenu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))  # pygame.FULLSCREEN
        self.running = True
        self.clock = pygame.time.Clock()
        self.snakeTexture = pygame.image.load(
            path.join(IMG_DIR, "snakeBody.png"))
        self.fruitTexture = pygame.image.load(
            path.join(IMG_DIR, "redApple.png"))
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

    def run(self):
        
        gameStartMenu = GameStartMenu(self.screen)

        gameMode = gameStartMenu.createMenu()

        if gameMode == "singleplayer":
            self.singlplayergameLoop()
        elif gameMode == "mutilplayer":
            self.connectToGameServer()
            self.multiplayergameLoop()

        pygame.quit()

    def connectToGameServer(self):
        self.client = Client("localhost", 11111)
        self.client.connectToServer()

    def multiplayergameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.networking()

            self.handleEvents()

            self.update()

            self.multiplayerRenderer()

            pygame.display.update()

            self.clock.tick(120)

    def singlplayergameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEvents()

            self.update()

            self.singlplayerRenderer()

            pygame.display.update()

            self.clock.tick(10)

    def networking(self):
        self.client.prepareDataForSend(self.snakeParts)
        self.client.sendData()
        self.enemySnakeParts = self.client.reciveData()

    def handleEvents(self):
        self.gameEvents.keyEvents()
        self.collisions.snakeAndFruit()
        self.collisions.snakeAndTail()

    def update(self):
        self.snake.snakeMove()
        self.snakeHead.moveSnakeHead()
        self.snakeParts = self.snake.getSnakeParts()
        self.collisions.snakeAndWall()

    def singlplayerRenderer(self):
        self.renderer.renderObjects(
            self.screen, self.fruitTexture, self.fruits.fruitBasket
        )
        self.renderer.renderObjects(
            self.screen, self.snakeTexture, self.snakeParts
        )

    def multiplayerRenderer(self):
        self.renderer.renderObjects(
            self.screen, self.fruitTexture, self.fruits.fruitBasket
        )
        self.renderer.renderObjects(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.renderer.renderEnemySnake(
            self.screen, self.snakeTexture, self.enemySnakeParts
        )
