
class Text:
    def __init__(self, x, y, name, font, primarTextColor, secondTextColor, text, screen):
        self.x = x
        self.y = y
        self.name = name
        self.font = font
        self.primarTextColor = primarTextColor
        self.secondTextColor = secondTextColor
        self.text = text
        self.screen = screen
        self.textRectangle = None
        self.pressed = 0

    def renderText(self):
        img = self.font.render(self.text, True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(self.x, self.y))
        self.screen.blit(img, self.textRectangle)

    def renderSecondColorText(self):
        img = self.font.render(self.text, True, self.secondTextColor)
        self.textRectangle = img.get_rect(center=(self.x, self.y))
        self.screen.blit(img, self.textRectangle)
   
    def renderDynamicText(self, text):
        img = self.font.render(text, True, self.primarTextColor)
        self.textRectangle = img.get_rect(center=(self.x, self.y))
        self.screen.blit(img, self.textRectangle)
