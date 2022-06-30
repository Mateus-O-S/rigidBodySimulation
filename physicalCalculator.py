import pygame


class physics:
    tags = []

    @staticmethod
    def createGravityTag(object):
        class gravityTag:
            def __init__(self, object):
                self.parent = object
                self.velocity = 0.1

            def calc(self):
                self.parent.y += self.velocity
                for v in self.parent.vertices:
                    v.y += self.velocity
                if self.velocity < 10: self.velocity *= 1.03

        physics.tags.append(gravityTag(object))

    @staticmethod
    def createCollisionTag(object):
        class gravityTag:
            def __init__(self, object):
                self.parent = object
            def calc(self):
                for v in self.parent.vertices:
                    if v.y > pygame.display.get_window_size()[1]:
                        v.y = pygame.display.get_window_size()[1] - 15

        physics.tags.append(gravityTag(object))

    @staticmethod
    def calc():
        for tag in physics.tags:
            tag.calc()
