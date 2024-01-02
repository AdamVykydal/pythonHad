import pygame


class GameEvents:
    def __init__(self, snakeHead, snake):
        self.speed = 20
        self.direction = (self.speed, 0)
        self.snakeHead = snakeHead
        self.snake = snake
    
    def keyEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snakeHead.setDirectionUp()
                    self.snake.addSnakePart()
                    return
                elif event.key == pygame.K_a:
                    self.snakeHead.setDirectionLeft()
                    return
                elif event.key == pygame.K_s:
                    self.snakeHead.setDirectionDown()
                    return
                elif event.key == pygame.K_d:
                    self.snakeHead.setDirectionRight()
                    return
    
