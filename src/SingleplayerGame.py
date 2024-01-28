import time
import pygame
from GameInfoBoard import GameInfoBoard
from Fruits import Fruits
from GameEvents import GameEvents
from SnakeHead import SnakeHead
from Renderer import Renderer
from Score import Score
from Snake import Snake
from Collisions import Collisions
from Coords import Coords
from LoadResources import LoadResources


class SingleplayerGame:
    def __init__(self, screen, screenSize):
        self.running = True
        self.screen = screen
        self.screenSize = screenSize
        self.clock = pygame.time.Clock()
        self.snakeCoords = Coords(500, 500)
        self.snakeHead = SnakeHead(self.snakeCoords)
        self.renderer = Renderer()
        self.fruits = Fruits()
        self.score = Score()
        self.snake = Snake(self.snakeHead)
        self.keySettings1 = {'up': pygame.K_w, 'left': pygame.K_a, 'down': pygame.K_s, 'right': pygame.K_d}
        self.gameEvents = GameEvents(self.snakeHead, self.keySettings1)
        self.collisions = Collisions(
            self.snakeHead, self.snake, self.fruits, self.score, self, self.screenSize)
        self.fruits.newFruit()
        self.snakeParts = self.snake.parts
        self.gameInfoBoard = GameInfoBoard(self.screen, self.screenSize)
        self.loadResources = LoadResources()
        self.snakeTexture = self.loadResources.loadImage("snakeBody.png")
        self.fruitTexture1 = self.loadResources.loadImage("redApple.png")
        self.fruitTexture2 = self.loadResources.loadImage("greenApple.png")
        self.snakeCoords = Coords(500, 500)
        self.startTime = time.time()
        self.currentTime = 0
        self.events = None

    def singlplayerGameLoop(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsSingleplayer()

            self.update()

            self.singlplayerRenderer()

            pygame.display.update()

            self.clock.tick(60)

    def handleEventsSingleplayer(self):
        self.currentTime = time.time()
        if self.currentTime - self.startTime >= 0.09:
            self.events = pygame.event.get()
            self.gameEvents.keyEvents(self.events)
            self.collisions.snakeAndFruit()
            self.collisions.snakeAndTail()

    def update(self):
        if self.currentTime - self.startTime >= 0.09:
            self.snake.snakeMove()
            self.snakeHead.moveSnakeHead()
            self.startTime = time.time()
        
        self.collisions.snakeAndWall()

    def singlplayerRenderer(self):
        self.renderer.renderFruits(
            self.screen, self.fruitTexture1, self.fruitTexture2, self.fruits.fruitBasket
        )
        self.renderer.renderSnake(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.gameInfoBoard.renderCounter(str(self.score.points))