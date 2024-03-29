import time
import pygame
from gameFunctions.GameInfoBoard import GameInfoBoard
from gameFunctions.Fruits import Fruits
from gameFunctions.GameEvents import GameEvents
from gameFunctions.SnakeHead import SnakeHead
from gameFunctions.Renderer import Renderer
from gameFunctions.Score import Score
from gameFunctions.Snake import Snake
from gameFunctions.Collisions import Collisions
from gameFunctions.Coords import Coords
from recources.LoadResources import LoadResources


class MultiplayerGame:
    def __init__(self, screen, screenSize, playerId, playerNames):
        self.running = True
        self.screen = screen
        self.screenSize = screenSize
        self.clock = pygame.time.Clock()
        self.playerId = playerId
        if self.playerId == 0:
            self.snakeCoords = Coords(1920 / 2 + 500, 500)
        else:
            self.snakeCoords = Coords(1920 / 2 - 500, 500)
        
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
        self.enemySnakeTexture = self.loadResources.loadImage("enemySnakeBody.png")
        self.snakeCoords = Coords(500, 500)
        self.startTime = time.time()
        self.currentTime = 0
        self.client = None
        self.enemySnakeParts = None
        self.recievedData = None
        self.fruitbasket = None
        self.collisionsInfoFromServer = [0,0,0]
        self.multiplayerScore = [0,0]
        self.playTime = 0
        self.events = None
        self.snake1Statistics = None
        self.snake2Statistics = None
        self.playerNames = playerNames
        
    def multiplayergameLoop(self, client):
        self.client = client
        
        while self.running:
            self.screen.fill((0, 0, 0))

            self.handleEventsMultiplayer()

            self.update()

            self.networking()

            self.multiplayerRenderer()

            pygame.display.update()

            self.clock.tick(60)

        return(self.findWinnerAndGameStats())
    
    def handleEventsMultiplayer(self):
        self.currentTime = time.time()
        if self.currentTime - self.startTime >= 0.09:
            self.events = pygame.event.get()
            self.gameEvents.keyEvents(self.events)
        self.collisions.snakeAndServerFruit(self.collisionsInfoFromServer[0])
    
    def update(self):
        if self.currentTime - self.startTime >= 0.09:
            self.snake.snakeMove()
            self.snakeHead.moveSnakeHead()
            self.startTime = time.time()
        
        self.collisions.snakeAndWall()
    
    def networking(self):
        self.client.prepareDataForSend(self.snakeParts)
        self.client.sendSnakeData()
        self.running, self.collisionsInfoFromServer, self.playTime, self.multiplayerScore, self.enemySnakeParts, self.fruitbasket = self.client.reciveGameData()

    def multiplayerRenderer(self):
        self.renderer.renderServerObject(
            self.screen, self.fruitTexture1, self.fruitbasket
        )
        self.renderer.renderSnake(
            self.screen, self.snakeTexture, self.snakeParts
        )
        self.renderer.renderServerObject(
            self.screen, self.enemySnakeTexture, self.enemySnakeParts
        )
        self.gameInfoBoard.renderMultiplayerCouter(self.multiplayerScore)
        self.gameInfoBoard.renderMultiplayerClock(self.playTime)
    
    def findWinnerAndGameStats(self):
        
        if self.playerId == 0:
            snake1Lenght = len(self.snake.parts)
            snake2Lenght = len(self.enemySnakeParts)
            self.snake1Statistics = {"name":self.playerNames[0], "points":self.multiplayerScore[0], "lenght":snake1Lenght, "fruits":0}
            self.snake2Statistics = {"name":self.playerNames[1], "points":self.multiplayerScore[1], "lenght":snake2Lenght, "fruits":0}
            if self.multiplayerScore[0] > self.multiplayerScore[1]:
                return(1, self.snake1Statistics, self.snake2Statistics)
            elif self.multiplayerScore[0] < self.multiplayerScore[1]:
                return(2, self.snake1Statistics, self.snake2Statistics)
            else:
                return("draw", self.snake1Statistics, self.snake2Statistics)
        else:
            snake1Lenght = len(self.enemySnakeParts)
            snake2Lenght = len(self.snake.parts)
            self.snake1Statistics = {"name":self.playerNames[0], "points":self.multiplayerScore[1], "lenght":snake1Lenght, "fruits":0}
            self.snake2Statistics = {"name":self.playerNames[1], "points":self.multiplayerScore[0], "lenght":snake2Lenght, "fruits":0}
            if self.multiplayerScore[0] > self.multiplayerScore[1]:
                return(2, self.snake1Statistics, self.snake2Statistics)
            elif self.multiplayerScore[0] < self.multiplayerScore[1]:
                return(1, self.snake1Statistics, self.snake2Statistics)
            else:
                return("draw", self.snake1Statistics, self.snake2Statistics)
    
        