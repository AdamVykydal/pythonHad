class Renderer:
    def renderObjects(self, screen, texture, objectsList):
        for objectForRender in objectsList:
            rectangle = texture.get_rect(topleft=(objectForRender.coords.x, objectForRender.coords.y))
            screen.blit(texture, rectangle)
    
    def renderFruits(self, screen, texture1, texture2, objectsList):
        for fruitForRender in objectsList:
            rectangle = texture1.get_rect(topleft=(fruitForRender.coords.x, fruitForRender.coords.y))
            if fruitForRender.textureType == "redApple":
                screen.blit(texture1, rectangle)
            elif fruitForRender.textureType == "greenApple":
                screen.blit(texture2, rectangle)

    def renderServerObject(self, screen, texture, coordsList):
        for coords in coordsList:
            rectangle = texture.get_rect(topleft=coords)
            screen.blit(texture, rectangle)
