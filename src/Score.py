class Score:
    def __init__(self):
        self.points = 0

    def addScore(self, points):
        self.points += points
    
    def subtractScore(self,  points):
        self.points -= points
    
    def checkScore(self):
        if self.points <= -500:
           return True
        return False
