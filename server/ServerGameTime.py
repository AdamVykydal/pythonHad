import pygame

class ServerGameTime:
    def __init__(self):
        pygame.init()
        self.timerEvent = pygame.USEREVENT+1
        pygame.time.set_timer(self.timerEvent, 1000)
        self.playTime = 100

    def check(self):
        for event in pygame.event.get():
            if event.type == self.timerEvent:
                self.playTime -= 1
                if self.playTime == 0:
                    return True ,self.playTime

        return False, self.playTime
            