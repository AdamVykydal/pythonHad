class Renderer:
    def renderObjects(self, screen, texture, objectsList):
        for objectForRender in objectsList:
            rectangle = texture.get_rect(topleft=(objectForRender.coords.x, objectForRender.coords.y))
            screen.blit(texture, rectangle)

    def renderServerObject(self, screen, texture, coordsList):
        for coords in coordsList:
            rectangle = texture.get_rect(topleft=coords)
            screen.blit(texture, rectangle)
