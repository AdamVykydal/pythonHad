class Score:
    def __init__(self):
        self.points = 0

    def addScore(self, points):
        self.points += points
    
    def subtractScore(self,  points):
        self.points -= points
    
    def checkScore(self, gameOptions):
        if self.points >= gameOptions[1] or self.points <= gameOptions[2]:
           return False
        return True
