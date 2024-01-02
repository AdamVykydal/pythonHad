import pygame
from sys import exit
from Render import Render
from GameEvents import GameEvents
from SnakeBody import SnakeBody, SnakeHead
from Snake import Snake

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.snakeTexture = pygame.image.load("souces\img\snakeBody.png")
        self.snakeRect = self.snakeTexture.get_rect(topleft=(500, 500))
        self.snakeBodyRender = Render()
        self.snakeHead = SnakeHead(self.snakeRect)
        self.snake = Snake(self.snakeHead)
        self.gameEvents = GameEvents(self.snakeHead, self.snake) 

    def gameLoop(self):
        while True:
            self.screen.fill((0, 0, 0))

            self.handle_events()

            self.update()

            self.renderer()

            pygame.display.update()

            self.clock.tick(10)

    def handle_events(self):
        self.gameEvents.keyEvents()

    def update(self):
        self.snake.snakeMove()
        self.snakeHead.moveSnakeHead()
        self.snakeHead.snakeAndWall()
        self.snakeParts = self.snake.getSnakeParts()
        

        
        

    def renderer(self):
        #self.snakeBodyRender.renderObject(self.screen, self.snakeTexture, self.snakeRect)
        self.snakeBodyRender.renderSnake(self.screen, self.snakeTexture, self.snakeParts)