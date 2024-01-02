import pygame
from sys import exit
from Render import Render
from GameEvents import GameEvents
from SnakeBody import SnakeHead
from Snake import Snake
from Collisions import Collisions
from Fruit import Fruit
from Score import Score

class Game:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.snakeTexture = pygame.image.load("souces\img\snakeBody.png")
        self.fruitTexture = pygame.image.load("souces/img/redApple.png")
        self.snakeRect = self.snakeTexture.get_rect(topleft=(500, 500))
        self.fruitRect = self.snakeTexture.get_rect(topleft=(1000, 500))
        self.snakeBodyRender = Render()
        self.fruit = Fruit(self.fruitRect)
        self.score = Score()
        self.snakeHead = SnakeHead(self.snakeRect)
        self.snake = Snake(self.snakeHead)
        self.gameEvents = GameEvents(self.snakeHead) 
        self.collisions = Collisions(self.snakeHead, self.snake, self.fruit, self.score, self)
    
    def gameLoop(self):
        while self.running == True:
            self.screen.fill((0, 0, 0))

            self.handle_events()

            self.update()

            self.renderer()

            pygame.display.update()

            self.clock.tick(10)

    def handle_events(self):
        self.gameEvents.keyEvents()
        self.collisions.snakeAndFruit()
        self.collisions.snakeAndTail()
        

    def update(self):
        self.snake.snakeMove()
        self.snakeHead.moveSnakeHead()
        self.snakeParts = self.snake.getSnakeParts()
        self.collisions.snakeAndWall()

    def renderer(self):
        self.snakeBodyRender.renderObject(self.screen, self.fruitTexture, self.fruitRect)
        self.snakeBodyRender.renderSnake(self.screen, self.snakeTexture, self.snakeParts)