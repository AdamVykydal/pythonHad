from Collisions import Collisions
class CollisionsLocalMultiplayer(Collisions):
    def __init__(self, snakeHead, snake, enemySnake, fruits, score, game, screenSize):
        super().__init__(snakeHead, snake, fruits, score, game, screenSize)
        self.enemySnake = enemySnake
    
    def snakeAndWall(self):
        super().snakeAndWall()
    
    def snakeAndTail(self):
        for snakePart in self.snake.parts[2:]:
            if self.snakeHead.coords.x == snakePart.coords.x and self.snakeHead.coords.y == snakePart.coords.y:
                self.score.subtractScore(2)

    def snakeAndFruit(self):
        super().snakeAndFruit()
    
    def snakeAndSnake(self):
        for enemySnakePart in self.enemySnake.parts:
            if enemySnakePart.coords.x == self.snakeHead.coords.x and enemySnakePart.coords.y == self.snakeHead.coords.y: 
                self.score.subtractScore(1)
