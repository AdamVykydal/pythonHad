import time
import datetime

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
   
    def getFormatedTime(self):
        timeDelta = datetime.timedelta(seconds=self.time)
        hours = 0
        minutes = 0
        seconds = 0
        
        if self.time >= 3600:
            hours = timeDelta.seconds // 3600
        if self.time >= 60:
            minutes = (timeDelta.seconds % 3600) // 60

        seconds = timeDelta.seconds % 60

        return(hours, minutes, seconds)
        
        

