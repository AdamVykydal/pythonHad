import pygame

class GameEvents:
    def __init__(self, snakeHead, keySettings):
        self.speed = 20
        self.direction = (self.speed, 0)
        self.snakeHead = snakeHead
        self.keySettings = keySettings

    def keyEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:        
                if event.key == self.keySettings["up"]:
                    self.snakeHead.setDirectionUp()
                    return
                elif event.key == self.keySettings["left"]:
                    self.snakeHead.setDirectionLeft()
                    return
                elif event.key == self.keySettings["down"]:
                    self.snakeHead.setDirectionDown()
                    return
                elif event.key == self.keySettings["right"]:
                    self.snakeHead.setDirectionRight()
                    return
    
   