import time

class Stopwatch:
    def __init__(self):
        self.startTime = 0
        self.menuTimeStart = 0
        self.endMenuTime = 0
        self.time = 0

    def start(self):
        self.startTime = time.time()

    def startMenuTime(self):
        self.menuTimeStart += time.time()

    def stopMenuTime(self):
        self.endMenuTime += time.time()

    def check(self):
        currentTime = time.time()
        elapsedTime = (currentTime - self.startTime) - (self.endMenuTime - self.menuTimeStart)

        self.time = elapsedTime
        self.time = round(self.time)
