from Sounds import Sounds

class Collisions:
    def __init__(self, snakeHead, snake, fruits, score, game, screenSize):
        self.snakeHead = snakeHead
        self.snake = snake
        self.score = score
        self.game = game
        self.fruits = fruits
        self.screenSize = screenSize
        self.sounds = Sounds()

    def snakeAndWall(self):
        if self.snakeHead.coords.x > self.screenSize.width - 20:
            self.snakeHead.coords.x = 0
            return
        elif self.snakeHead.coords.x < 0:
            self.snakeHead.coords.x = self.screenSize.width - 20
            return
        elif self.snakeHead.coords.y > self.screenSize.height - 20:
            self.snakeHead.coords.y = 0
            return
        elif self.snakeHead.coords.y < 0:
            self.snakeHead.coords.y = self.screenSize.height - 20
            return

    def snakeAndTail(self):
        for snakePart in self.snake.parts[2:]:
            if self.snakeHead.coords.x == snakePart.coords.x and self.snakeHead.coords.y == snakePart.coords.y:
                self.game.running = False

    def snakeAndFruit(self):
        for fruit in self.fruits.fruitBasket:
            if self.snakeHead.coords.x == fruit.coords.x and self.snakeHead.coords.y == fruit.coords.y:
                self.sounds.playNomSound()
                self.snake.addSnakePart()
                self.score.addScore(1)
                fruit.generateFruit()
                self.fruits.newFruit()

    
    def snakeAndServerFruit(self, foodTouch):
        if foodTouch == 1:
            self.sounds.playNomSound()
            self.snake.addSnakePart()
            self.score.addScore(1)
