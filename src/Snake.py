from SnakeBody import SnakeBody


class Snake():
    def __init__(self, snakeHead):
        self.snakeParts = []
        self.snakeParts.append(snakeHead)
        self.newBodyRectangle = None
        self.snakePartIndex = None

    def addSnakePart(self):
        self.newBodyRectangle = self.snakeParts[-1].getRectangleCopy()
        self.snakeParts.append(SnakeBody(self.newBodyRectangle))

    def snakeMove(self):
        self.snakePartIndex = len(self.snakeParts) - 1
        # print(self.snakePartIndex)
        # print(self.snakeParts)

        # print("head is before = ",self.snakeParts[0].getRectangle())
        for snakePart in reversed(self.snakeParts[1:]):
            # print(snakePart, self.snakeParts.index(snakePart))
            # print (snakePart.getRectangle())

            self.snakePartIndex -= 1

            # print("index is:", self.snakePartIndex)

            snakePart.setRectangle(
                (self.snakeParts[self.snakePartIndex]).getRectangleCopy())
            # print (snakePart.getRectangle())
            # print("--------------")
        # print("head is after = ",self.snakeParts[0].getRectangle())

    def getSnakeParts(self):
        return self.snakeParts
