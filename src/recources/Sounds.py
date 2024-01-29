import pygame
#from definitions import SOUNDS_DIR
from recources.LoadResources import LoadResources

class Sounds:
    def __init__(self):
        self.loadResources = LoadResources()
        self.nomSound = self.loadResources.loadSound("beep.mp3")#pygame.mixer.music.load("resources\sounds\\beep.mp3")
    def playNomSound(self):
        self.nomSound.play()
