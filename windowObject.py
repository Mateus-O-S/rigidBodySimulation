import planeObject
import pygame
import sys

class window:
    def __init__(self, color:tuple=(255,255,255)):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        self.keyEvents = []
        self.color = color
        self.planes = []

    def createKeyEvent(self, key:str, then):
        class Key:
            def __init__(self, ifPress, thenCall):
                self.then = thenCall
                self.key = ifPress

            def test(self, keyPressed):
                if keyPressed == self.key:
                    self.then()

        self.keyEvents.append(Key(key, then))

    def update(self):
        self.screen.fill(self.color)

        for p in self.planes:
            p.draw(self.screen)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)

            if e.type == pygame.KEYDOWN:
                for key in self.keyEvents:
                    key.test(e.unicode)

        pygame.display.update()
        pygame.time.wait(2)

    def create2dPlane(self):
        newPlane = planeObject.plane()
        self.planes.append(newPlane)
        return newPlane