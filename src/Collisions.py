from Sounds import Sounds

class Collisions:
    def __init__(self, snakeHead, snake, fruits, score, game):
        self.snakeHead = snakeHead
        self.snake = snake
        self.score = score
        self.game = game
        self.fruits = fruits
        self.sounds = Sounds()

    def snakeAndWall(self):
        if self.snakeHead.coords.x > 1900:
            self.snakeHead.coords.x = 0
            return
        elif self.snakeHead.coords.x < 0:
            self.snakeHead.coords.x = 1900
            return
        elif self.snakeHead.coords.y > 1060:
            self.snakeHead.coords.y = 0
            return
        elif self.snakeHead.coords.y < 0:
            self.snakeHead.coords.y = 1060
            return

    def snakeAndTail(self):
        for snakePart in self.snake.snakeParts[2:]:
            if self.snakeHead.coords.x == snakePart.coords.x and self.snakeHead.coords.y == snakePart.coords.y:
                print("you lost with:", self.score.points, "points")
                self.game.running = False

    def snakeAndFruit(self):
        for fruit in self.fruits.fruitBasket:
            if self.snakeHead.coords.x == fruit.coords.x and self.snakeHead.coords.y == fruit.coords.y:
                self.sounds.playNomSound()
                self.snake.addSnakePart()
                self.score.addPoints()
                self.score.printPoints()
                fruit.generateFruit()
                self.fruits.newFruit()
