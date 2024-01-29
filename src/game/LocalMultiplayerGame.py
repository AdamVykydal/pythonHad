import time
import pygame
from gameFunctions.GameInfoBoard import GameInfoBoard
from gameFunctions.Fruits import Fruits
from gameFunctions.GameEvents import GameEvents
from gameFunctions.SnakeHead import SnakeHead
from gameFunctions.Renderer import Renderer
from gameFunctions.Score import Score
from gameFunctions.Snake import Snake
from gameFunctions.CollisionsLocalMultiplayer import CollisionsLocalMultiplayer
from gameFunctions.Coords import Coords
from recources.LoadResources import LoadResources
from gameFunctions.GameTime import GameTime
from menu.EscPauseMenu import EscPauseMenu


class LocalMultiplayerGame:
    def __init__(self, screen, screenSize):
        self.running = True
        self.screen = screen
        self.screenSize = screenSize
        self.clock = pygame.time.Clock()
        self.snakeCoords = Coords(screenSize.width /2 -500, 500)
        self.snakeCoords2 = Coords(screenSize.width /2 +500, 500)
        self.snakeHead = SnakeHead(self.snakeCoords)
        self.snakeHead2 = SnakeHead(self.snakeCoords2)
        self.renderer = Renderer()
        self.fruits = Fruits()
        self.score = Score()
        self.score2 = Score()
        self.snake1 = Snake(self.snakeHead)
        self.snake2 = Snake(self.snakeHead2)
        self.keySettings1 = {'up': pygame.K_w, 'left': pygame.K_a, 'down': pygame.K_s, 'right': pygame.K_d}
        self.keySettings2 = {'up': pygame.K_UP, 'left': pygame.K_LEFT, 'down': pygame.K_DOWN, 'right': pygame.K_RIGHT}
        self.gameEvents = GameEvents(self.snakeHead, self.keySettings1)
        self.gameEvents2 = GameEvents(self.snakeHead2, self.keySettings2)
        self.collisions = CollisionsLocalMultiplayer(
            self.snakeHead, self.snake1, self.snake2, self.fruits, self.score, self, self.screenSize)
        self.collisions2 = CollisionsLocalMultiplayer(
            self.snakeHead2, self.snake2, self.snake1, self.fruits, self.score2, self, self.screenSize)
        self.fruits.newFruit()
        self.snakeParts1 = self.snake1.parts
        self.snakeParts2 = self.snake2.parts
        self.gameInfoBoard = GameInfoBoard(self.screen, self.screenSize)
        self.loadResources = LoadResources()
        self.snakeTexture = self.loadResources.loadImage("snakeBody.png")
        self.snake2Texture = self.loadResources.loadImage("enemySnakeBody.png")
        self.fruitTexture1 = self.loadResources.loadImage("redApple.png")
        self.fruitTexture2 = self.loadResources.loadImage("greenApple.png")
        self.startTime = time.time()
        self.currentTime = 0
        self.events = None
        self.gameTime = GameTime([100, 0, 0])
        self.remainingTime = 0
        self.escPauseMenu = EscPauseMenu(self.screen, self.screenSize, self.gameTime)
        
    def localMultiplayerGameLoop(self):
        self.gameTime.start()
       
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsLocalMultiplayer()

            self.update()

            self.localMultiplayerRenderer()

            pygame.display.update()

            self.clock.tick(60)

    def handleEventsLocalMultiplayer(self):
        self.currentTime = time.time()
        if self.currentTime - self.startTime >= 0.09:
            self.events = pygame.event.get()
            self.gameEvents.keyEvents(self.events)
            self.gameEvents2.keyEvents(self.events)
            self.collisions.snakeAndFruit()
            self.collisions.snakeAndTail()
            self.collisions.snakeAndSnake()
            self.collisions2.snakeAndFruit()
            self.collisions2.snakeAndTail()
            self.collisions2.snakeAndSnake()
            self.running = self.escPauseMenu.checkIfEscIsPressed(self.events)
    
        end, self.remainingTime = self.gameTime.check()
        
        if end:
            self.running = False
    
    def update(self):
        if self.currentTime - self.startTime >= 0.09:
            self.snake1.snakeMove()
            self.snakeHead.moveSnakeHead()
            self.snake2.snakeMove()
            self.snakeHead2.moveSnakeHead()
            self.startTime = time.time()
        
        self.collisions.snakeAndWall()
        self.collisions2.snakeAndWall()

    def localMultiplayerRenderer(self):
        self.renderer.renderFruits(
            self.screen, self.fruitTexture1, self.fruitTexture2, self.fruits.fruitBasket
        )
        self.renderer.renderSnake(
            self.screen, self.snakeTexture, self.snakeParts1
        )
        self.renderer.renderSnake(
            self.screen, self.snake2Texture, self.snakeParts2
        )
        self.gameInfoBoard.renderMultiplayerCouter([self.score.points,self.score2.points])
        self.gameInfoBoard.renderMultiplayerClock(self.remainingTime)
