from Fruit import Fruit


class Fruits:
    def __init__(self):
        self.fruitBasket = []

    def newFruit(self):
        self.fruitBasket.append(Fruit())
