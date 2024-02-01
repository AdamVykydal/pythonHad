from gameFunctions.Collisions import Collisions
class CollisionsLocalMultiplayer(Collisions):
    def __init__(self, snakeHead, snake, enemySnake, fruits, score, game, screenSize):
        super().__init__(snakeHead, snake, fruits, score, game, screenSize)
        self.enemySnake = enemySnake
        self.snakeEatedFruits = 0
    
    def snakeAndWall(self):
        super().snakeAndWall()
    
    def snakeAndTail(self):
        for snakePart in self.snake.parts[2:]:
            if self.snakeHead.coords.x == snakePart.coords.x and self.snakeHead.coords.y == snakePart.coords.y:
                self.score.subtractScore(2)

    def snakeAndFruit(self):
        for fruit in self.fruits.fruitBasket:
            if self.snakeHead.coords.x == fruit.coords.x and self.snakeHead.coords.y == fruit.coords.y:
                self.sounds.playNomSound()
                self.snake.addSnakePart()
                self.score.addScore(1)
                fruit.generateFruit()
                self.fruits.newFruit()
                self.snakeEatedFruits += 1

    
    def snakeAndSnake(self):
        for enemySnakePart in self.enemySnake.parts:
            if enemySnakePart.coords.x == self.snakeHead.coords.x and enemySnakePart.coords.y == self.snakeHead.coords.y: 
                self.score.subtractScore(1)
    

