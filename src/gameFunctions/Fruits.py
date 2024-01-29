from gameFunctions.Fruit import Fruit

class Fruits:
    def __init__(self):
        self.fruitBasket = []
    
    def emptyFruitBasket(self):
        self.fruitBasket = []
        self.fruitBasket.append(Fruit())
    
    def newFruit(self):
        self.fruitBasket.append(Fruit())
    
    def getFruitsCoords(self):
        fruitsCoords = []
        for fruit in self.fruitBasket:
            fruitsCoords.append((fruit.coords.x, fruit.coords.y))
        
        return fruitsCoords