import pygame
from definitions import SOUNDS_DIR

class Sounds:
    def __init__(self):
        self.nomSound = pygame.mixer.music.load(SOUNDS_DIR + "\\" + "beep.mp3")
    def playNomSound(self):
        pygame.mixer.music.play()
