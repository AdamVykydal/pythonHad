class ServerScore:
    def __init__ (self):
        self.score = [0,0]
    def addScore(self, threadId, points):
        self.score[threadId] += points
    def subtractScore(self, threadId, points):
        self.score[threadId] -= points