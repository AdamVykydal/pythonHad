import time

class GameTime:
    def __init__(self, gameOptions):
        self.startTime = None
        self.playTime = int(gameOptions[0])
    
    def start(self):
        self.startTime = time.time()

    def check(self):
        currentTime = time.time()
        elapsedTime = currentTime - self.startTime

        if elapsedTime >= self.playTime:
            return True, 0 
        else:
            remainingTime = self.playTime - elapsedTime
            return False, round(remainingTime)