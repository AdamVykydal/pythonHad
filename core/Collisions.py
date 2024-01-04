from Fruits import Fruits
class Collisions:
    def __init__(self, snakeHead, snake, fruits, score ,game):
        self.snakeHead = snakeHead
        self.snake = snake
        self.score = score
        self.game = game
        self.fruits = fruits

    def snakeAndWall(self):
        if self.snakeHead.rectangle.x > 1900:
            self.snakeHead.rectangle.x = 0
            return
        elif self.snakeHead.rectangle.x < 0:
            self.snakeHead.rectangle.x = 1900
            return
        elif self.snakeHead.rectangle.y > 1060:
            self.snakeHead.rectangle.y = 0
            return
        elif self.snakeHead.rectangle.y < 0:
            self.snakeHead.rectangle.y = 1060
            return

    def snakeAndTail(self):
        for snakePart in self.snake.snakeParts[2:]:
            if self.snakeHead.rectangle == snakePart.getRectangle():
                print("you lost with:", self.score.points, "points")
                self.game.running = False

    def snakeAndFruit(self):
        for fruit in self.fruits.fruitBasket:
            if self.snakeHead.rectangle == fruit.getRectangle():
                self.snake.addSnakePart()
                self.score.addPoints()
                self.score.printPoints()
                fruit.generateFruit()
                self.fruits.newFruit()
            

