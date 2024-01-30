class ServerScore:
    def __init__ (self):
        self.score = [0, 0]
    def addScore(self, threadId, points):
        self.score[threadId] += points
    def subtractScore(self, threadId, points):
        self.score[threadId] -= points
    def checkScore(self, threadId, gameOptions):
        if self.score[threadId] >= gameOptions[1] or self.score[threadId] <= gameOptions[2]:
           print("ano")
           return False
        return True
    
