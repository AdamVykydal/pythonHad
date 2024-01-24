
import sys
from ServerCollisions import ServerCollisions
from ServerGameTime import ServerGameTime

sys.path.append("src")
from Fruits import Fruits

class ServerGameLogick:
    def __init__(self, clientsSnakes, serverScore):
        
        self.fruits = Fruits()
        self.fruits.newFruit()
        self.serverScore = serverScore
        self.gameFinished = False
        self.serverGameTime = ServerGameTime()
        self.playTime = 0
        
        self.serverCollisions = ServerCollisions(clientsSnakes, self.fruits, self.serverScore)
    
    def process(self, threadId):
        self.gameFinished = False
        self.gameFinished = self.serverScore.checkScore(threadId)
        self.gameFinished, self.playTime = self.serverGameTime.check()
       
        if self.gameFinished:
            self.restartgame()
        
        collistionsInfo = [0,0,0]
        collistionsInfo[0] = self.serverCollisions.snakeAndFruit(threadId)
        collistionsInfo[1] = self.serverCollisions.snakeAndTail(threadId)
        collistionsInfo[2] = self.serverCollisions.snakeAndSnake(threadId)
        
        return self.gameFinished, collistionsInfo, self.playTime, self.fruits.getFruitsCoords()
    
    def restartgame(self):
        self.serverScore.score = [0,0]
        self.fruits.emptyFruitBasket()