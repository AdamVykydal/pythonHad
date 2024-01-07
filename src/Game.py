from os import path
import pygame
from sys import exit
from Render import Render
from GameEvents import GameEvents
from SnakeBody import SnakeHead
from Snake import Snake
from Collisions import Collisions
from Fruit import Fruit
from Score import Score
from Fruits import Fruits
from definitions import IMG_DIR
from Client import Client

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.snakeTexture = pygame.image.load(path.join(IMG_DIR, "snakeBody.png"))
        self.fruitTexture = pygame.image.load(path.join(IMG_DIR, "redApple.png"))
        self.snakeRect = self.snakeTexture.get_rect(topleft=(500, 500))
        self.snakeBodyRender = Render()
        self.fruits = Fruits()
        self.score = Score()
        self.snakeHead = SnakeHead(self.snakeRect)
        self.snake = Snake(self.snakeHead)
        self.gameEvents = GameEvents(self.snakeHead) 
        self.collisions = Collisions(self.snakeHead, self.snake, self.fruits, self.score, self)
        self.fruits.newFruit()
        self.snakeParts = self.snake.getSnakeParts()       
    
    def connectToGameServer(self):
        self.client = Client("localhost", 11111)
        self.client.connectToServer() 
    
    def MultiplayergameLoop(self):
        while self.running == True:
            self.screen.fill((0, 0, 0))
            
            self.networking()
            
            self.handle_events()

            self.update()

            self.multiplayerRenderer()

            pygame.display.update()

            self.clock.tick(10)
    
    def SinglplayergameLoop(self):
        while self.running == True:
            self.screen.fill((0, 0, 0))
            
            self.handle_events()

            self.update()

            self.singlplayerRenderer()

            pygame.display.update()

            self.clock.tick(10)
    
    def networking(self):
        self.client.PrepareDataForSend(self.snakeParts)
        self.client.sendData()
        self.enemySnake = self.client.reciveData()
        
    def handle_events(self):
        self.gameEvents.keyEvents()
        self.collisions.snakeAndFruit()
        self.collisions.snakeAndTail()
        
    def update(self):
        self.snake.snakeMove()
        self.snakeHead.moveSnakeHead()
        self.snakeParts = self.snake.getSnakeParts()
        self.collisions.snakeAndWall()

    def singlplayerRenderer(self):
        self.snakeBodyRender.renderObjects(self.screen, self.fruitTexture, self.fruits.fruitBasket)
        self.snakeBodyRender.renderObjects(self.screen, self.snakeTexture, self.snakeParts)
    
    def multiplayerRenderer(self):
        self.snakeBodyRender.renderObjects(self.screen, self.fruitTexture, self.fruits.fruitBasket)
        self.snakeBodyRender.renderObjects(self.screen, self.snakeTexture, self.snakeParts)
        self.snakeBodyRender.renderEnemySnake(self.screen, self.snakeTexture, self.enemySnake)