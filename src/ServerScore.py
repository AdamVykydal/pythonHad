class ServerScore:
    def __init__ (self):
        self.score = [0, 0]
    def addScore(self, threadId, points):
        self.score[threadId] += points
    def subtractScore(self, threadId, points):
        self.score[threadId] -= points
    def checkScore(self, threadId):
        if self.score[threadId] <= -500:
           return True
        return False
