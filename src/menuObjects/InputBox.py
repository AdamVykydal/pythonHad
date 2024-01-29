import pygame

class InputBox():
    def __init__(self, x, y, name, font, primarTextColor, secondTextColor, screen, w, h):
        self.x = x
        self.y = y
        self.name = name
        self.font = font
        self.primarTextColor = primarTextColor
        self.secondTextColor = secondTextColor
        self.screen = screen
        self.textRectangle = None
        self.boxRectangle = None
        self.w = w
        self.h = h
        self.active = False
        self.text = ""

    def renderInputBox(self):
        img = self.font.render(self.text, True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(self.x, self.y))
        
        
        self.textRectangle.width = max(400,self.textRectangle.width +10)
        
        self.boxRectangle = pygame.draw.rect(self.screen, self.primarTextColor, (1920 /2 - self.textRectangle.width /2, self.textRectangle.y, self.textRectangle.width, self.textRectangle.height ), 2)
        self.screen.blit(img, (self.textRectangle.x, self.textRectangle.y))
        
    
    def renderSecondColorInputBox(self, ):
        img = self.font.render(self.text, True, self.secondTextColor)
        self.textRectangle = img.get_rect(center=(self.x, self.y))
       
        self.textRectangle.width = max(400,self.textRectangle.width +10)
        
        self.boxRectangle =pygame.draw.rect(self.screen, self.secondTextColor, (1920 /2 - self.textRectangle.width /2, self.textRectangle.y, self.textRectangle.width, self.textRectangle.height ), 2)
        
        self.screen.blit(img, (self.textRectangle.x, self.textRectangle.y))
        
        