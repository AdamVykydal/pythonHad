class Collisions:
    def __init__(self, snakeHead, snake, fruit, score ,game):
        self.snakeHead = snakeHead
        self.snake = snake
        self.fruit = fruit
        self.score = score
        self.game = game

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
        if self.snakeHead.rectangle == self.fruit.rectangle:
            self.snake.addSnakePart()
            self.score.addPoints()
            self.score.printPoints()
            self.fruit.generateFruit()
