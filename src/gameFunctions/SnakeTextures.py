from recources.LoadResources import LoadResources

class SnakeTextures:
    def __init__(self):
        self.loadResources = LoadResources
        self.snakeHeadTexture = self.loadResources.loadImage("snakeBodyHead.png")
        self.snakeBodyTexture = self.loadResources.loadImage("snakeBody.png")
        self.snakeTailTexture = self.loadResources.loadImage("snakeBodyTail.png")
        