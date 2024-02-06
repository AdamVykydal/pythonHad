from gameFunctions.RotateBodyParts import RotateBodyPart
class Renderer:
    def __init__(self) -> None:
        self.renderBodyParts = RotateBodyPart()
    def renderSnake(self, screen, texture, objectsList):
        for objectForRender in objectsList:
            rectangle = texture.get_rect(topleft=(objectForRender.coords.x, objectForRender.coords.y))
            self.renderBodyParts.checkAndRotate(objectForRender)
            screen.blit(texture, rectangle)
    
    def renderFruits(self, screen, texture1, texture2, objectsList):
        for fruitForRender in objectsList:
            rectangle = texture1.get_rect(topleft=(fruitForRender.coords.x, fruitForRender.coords.y))
            if fruitForRender.textureType == "redApple":
                screen.blit(texture1, rectangle)
            elif fruitForRender.textureType == "greenApple":
                screen.blit(texture2, rectangle)

    
    