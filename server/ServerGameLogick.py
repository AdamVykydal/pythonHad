
import sys
sys.path.append("src")
from Fruits import Fruits
from ServerCollisions import ServerCollisions


class ServerGameLogick:
    def __init__(self, clientsSnakes, serverScore):
        self.fruits = Fruits()
        self.fruits.newFruit()
        self.serverScore = serverScore
        
        self.serverCollisions = ServerCollisions(clientsSnakes, self.fruits, self.serverScore)
    def process(self, threadId):
        collistionsInfo = [0,0,0]
        collistionsInfo[0] = self.serverCollisions.snakeAndFruit(threadId)
        collistionsInfo[1] = self.serverCollisions.snakeAndTail(threadId)
        collistionsInfo[2] = self.serverCollisions.snakeAndSnake(threadId)
        return collistionsInfo, self.fruits.getFruitsCoords()