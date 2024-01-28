
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
        self.rectangle = None
        self.pressed = 0

    def renderText(self):
        img = self.font.render(self.text, True, self.primarTextColor)
        self.rectangle = img.get_rect(center=(self.x, self.y))
        self.screen.blit(img, self.rectangle)

    def renderSecondColorText(self):
        img = self.font.render(self.text, True, self.secondTextColor)
        self.rectangle = img.get_rect(center=(self.x, self.y))
        self.screen.blit(img, self.rectangle)
   
    def renderDynamicText(self, text):
        text = str(text)
        img = self.font.render(text, True, self.primarTextColor)
        self.rectangle = img.get_rect(center=(self.x, self.y))
        self.screen.blit(img, self.rectangle)
