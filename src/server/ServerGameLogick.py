from gameFunctions.GameTime import GameTime
from gameFunctions.Fruits import Fruits
from server.ServerCollisions import ServerCollisions


class ServerGameLogick:
    def __init__(self, clientsSnakes, serverScore, gameOptions):
        
        self.fruits = Fruits()
        self.fruits.newFruit()
        self.serverScore = serverScore
        self.gameFinished = False
        self.gameOptions = gameOptions
        self.serverGameTime = GameTime(self.gameOptions)
        self.serverGameTime.start()
        self.playTime = 0
        self.previousHeadPosition = [0,0]
        self.clientsSnakes = clientsSnakes
        
        self.serverCollisions = ServerCollisions(clientsSnakes, self.fruits, self.serverScore)
    
    def process(self, threadId):
        self.gameFinished = False
        self.gameFinished = self.serverScore.checkScore(threadId)
        
        self.gameFinished, self.playTime = self.serverGameTime.check()
       
        if self.gameFinished:
            self.restartgame()
        
        collistionsInfo = [0,0,0]
        
        snake = self.clientsSnakes[threadId]
        
        if  snake[0] != self.previousHeadPosition[threadId]:
            print("done")
            self.previousHeadPosition[threadId] = snake[0]
            
            collistionsInfo[0] = self.serverCollisions.snakeAndFruit(threadId)
            collistionsInfo[1] = self.serverCollisions.snakeAndTail(threadId)
            collistionsInfo[2] = self.serverCollisions.snakeAndSnake(threadId)

        return self.gameFinished, collistionsInfo, self.playTime, self.fruits.getFruitsCoords()
    
    def restartgame(self):
        self.serverScore.score = [0,0]
        self.fruits.emptyFruitBasket()