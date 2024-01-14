
class ServerCollisions:
    def __init__(self, clientsSnakesCoords, fruits, serverScore):
        self.clientsSnakesCoords = clientsSnakesCoords
        self.fruits = fruits
        self.serverScore = serverScore

    def snakeAndFruit(self, threadId):
        snakeHeadCoords = self.clientsSnakesCoords[threadId]
        snakeHeadX, snakeHeadY = snakeHeadCoords[0]

        for fruit in self.fruits.fruitBasket:

            if snakeHeadX == fruit.coords.x and snakeHeadY == fruit.coords.y:
                fruit.generateFruit()
                self.fruits.newFruit()
                self.serverScore.addScore(threadId, 1)
                return 1
        return 0

    def snakeAndSnake(self, threadId):
        snakeHeadCoords = self.clientsSnakesCoords[threadId]

        if threadId == 0:
            enemyThreadId = 1
        else:
            enemyThreadId = 0

        for enemySnakePart in self.clientsSnakesCoords[enemyThreadId]:

            if snakeHeadCoords[0] == enemySnakePart:
                self.serverScore.subtractScore(threadId, 10)
                return 1
        return 0

    def snakeAndTail(self, threadId):
        snakeHeadCoords = self.clientsSnakesCoords[threadId]

        snakeCoords =self.clientsSnakesCoords[threadId]
        for snakePart in snakeCoords[1:]:

            if snakeHeadCoords[0] == snakePart:
                self.serverScore.subtractScore(threadId, 5)
                return 1
        return 0
    
    def snakeAndWall(self):
        pass
