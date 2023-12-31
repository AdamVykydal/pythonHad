import pygame
from sys import exit
from Render import Render
from GameEvents import GameEvents
from SnakeBody import SnakeBody, SnakeHead
from Snake import Snake

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.snakeTexture = pygame.image.load("souces\img\snakeBody.png")
        self.snakeRect = self.snakeTexture.get_rect(topleft=(500, 500))
        self.snakeBodyRender = Render()
        self.snakeHead = SnakeHead(self.snakeRect)
        self.gameEvents = GameEvents(self.snakeHead)
        self.snake = Snake(self.snakeHead)
        self.rect = self.snakeTexture.get_rect(topleft=(500, 500))
        self.snake.addSnakePart(self.rect)

    def gameLoop(self):
        while True:
            self.screen.fill((0, 0, 0))

            self.handle_events()

            self.update()

            self.renderer()

            pygame.display.update()

            self.clock.tick(5)

    def handle_events(self):
        self.gameEvents.keyEvents()

    def update(self):
        self.snakeHead.moveSnakeHead()
        self.snakeHead.snakeAndWall()

    def renderer(self):
        self.snakeBodyRender.renderObject(self.screen, self.snakeTexture, self.snakeRect)
