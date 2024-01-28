import sys
import os
import pygame


class LoadResources:
    def loadImage(self, filename):
        if getattr(sys, 'frozen', False):
            currentDir = os.path.dirname(sys.executable)
        else:
            currentDir = os.path.dirname(os.path.realpath(__file__))

        imgPath = os.path.join(currentDir, "..", "resources", "img", filename)
        return pygame.image.load(imgPath).convert_alpha()

    def loadSound(self, filename):
        if getattr(sys, 'frozen', False):
            currentDir = os.path.dirname(sys.executable)
        else:
            currentDir = os.path.dirname(os.path.realpath(__file__))

        soundPath = os.path.join(
            currentDir, "..", "resources", "sounds", filename)
        return pygame.mixer.Sound(soundPath)
