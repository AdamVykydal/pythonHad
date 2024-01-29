import time

class GameTime:
    def __init__(self, gameOptions):
        self.startTime = 0
        self.playTime = int(gameOptions[0])
        self.timeBeforeStop = 0
        self.menuTimeStart = 0
        self.endMenuTime = 0
    
    def start(self):
        self.startTime = time.time()
    
    def startMenuTime(self):
        self.menuTimeStart += time.time()
        
    def stopMenuTime(self):
        self.endMenuTime += time.time()
        
    
    def check(self):
        currentTime = time.time()
        elapsedTime = (currentTime - self.startTime) - (self.endMenuTime - self.menuTimeStart)
    
        if elapsedTime >= self.playTime:
            print("ajaj")
            return True, 0 
        else:
            remainingTime = self.playTime - elapsedTime
            print(remainingTime)
            return False, round(remainingTime)