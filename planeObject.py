class plane:
    def __init__(self):
        self.objects = []

    def draw(self, screen):
        for o in self.objects:
            o.draw(screen)