from abc import ABC, abstractmethod
import pygame
import math

class visual(ABC):
    def __init__(self, color:tuple, size:tuple):
        self.color = color
        self.size = size

    @abstractmethod
    def draw(self, screen):
        pass

class oneCentralVisual(visual):
    def  __init__(self, x:float, y:float, color:tuple, size:tuple):
        super().__init__(color, size)
        self.y = y
        self.x = x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size[0], self.size[1]))

class vertex(oneCentralVisual):
    def __init__(self, x:float, y:float, color:tuple, size:int):
        super().__init__(x, y, color, (size, size))

class edge(visual):
    def __init__(self, color:tuple, size:int, start_x:float, start_y:float, end_x:float, end_y:float, quality:int):
        super().__init__(color, (size, size))
        self.distance_x = (start_x - end_x) / quality
        self.distance_y = (start_y - end_y) / quality
        self.vertices = [vertex(start_x - (self.distance_x * v), start_y - (self.distance_y * v), color, size) for v in range(quality)]

    def draw(self, screen):
        for v in self.vertices:
            v.draw(screen)

class square(oneCentralVisual):
    def __init__(self, x:float, y:float, color:tuple, size:tuple, filled:bool=True, resolution:int=1000):
        super().__init__(x, y, color, size)
        self.filled = filled

        self.vertices = [
            vertex(x-size[0]/2, y+size[1]/2, color, 5),
            vertex(x-size[0]/2, y-size[1]/2, color, 5),
            vertex(x+size[0]/2, y+size[1]/2, color, 5),
            vertex(x+size[0]/2, y-size[1]/2, color, 5)
        ]

        self.edges = [
            edge(color, 5, self.vertices[1].x, self.vertices[1].y, self.vertices[3].x, self.vertices[3].y, resolution),
            edge(color, 5, self.vertices[1].x, self.vertices[1].y, self.vertices[0].x, self.vertices[0].y, resolution),
            edge(color, 5, self.vertices[2].x, self.vertices[2].y, self.vertices[0].x, self.vertices[0].y, resolution),
            edge(color, 5, self.vertices[3].x, self.vertices[3].y, self.vertices[2].x, self.vertices[2].y, resolution)
        ]

        self.filling = [
            edge(self.edges[1].color, 5, self.edges[1].vertices[v].x, self.edges[1].vertices[v].y, self.edges[3].vertices[v].x, self.edges[3].vertices[v].y, int(resolution/1.5)) \
                for v in range(len(self.edges[1].vertices)-1)
        ]

    def draw(self, screen):
        if self.filled:
            for e in self.filling:
                e.draw(screen)
        else:
            for e in self.edges:
                e.draw(screen)


class triangle(oneCentralVisual):
    def __init__(self, x:float, y:float, color:tuple, size:tuple, topVertexPosition:int=0, filled:bool=True, resolution:int=1000):
        super().__init__(x, y, color, size)
        self.filled = filled

        self.vertices = [
            vertex(x+size[0]*topVertexPosition, y-size[1], color, 5),
            vertex(x-size[0], y+size[1], color, 5),
            vertex(x+size[0], y+size[1], color, 5),
        ]

        self.edges = [
            edge(color, 5, self.vertices[0].x, self.vertices[0].y, self.vertices[1].x, self.vertices[1].y, resolution),
            edge(color, 5, self.vertices[0].x, self.vertices[0].y, self.vertices[2].x, self.vertices[2].y, resolution),
            edge(color, 5, self.vertices[1].x, self.vertices[1].y, self.vertices[2].x, self.vertices[2].y, resolution),
        ]

        self.filling = [
            edge(self.edges[0].color, 15, self.vertices[0].x, self.vertices[0].y, self.edges[2].vertices[v].x, self.edges[2].vertices[v].y, int(resolution/1.5)) \
                for v in range(len(self.edges[0].vertices) - 1)
        ]

    def draw(self, screen):
        if self.filled:
            for e in self.filling:
                e.draw(screen)
        else:
            for e in self.edges:
                e.draw(screen)

class circle(oneCentralVisual):
    def __init__(self, x:float, y:float, color:tuple, radios:int, Width:int=1):
        super().__init__(x, y, color, (radios, radios))
        self.vertices = []
        for height in range(radios*2+1):
            pixel_y = y + (height - radios)
            for width in range(radios*2+1):
                pixel_x = x - (width - radios)
                if -Width < math.sqrt((abs(x) - abs(pixel_x))**2 + (abs(y) - abs(pixel_y))**2) - radios < 0:
                    self.vertices.append(vertex(pixel_x, pixel_y, color, 5))

    def draw(self, screen):
        for v in self.vertices:
            v.draw(screen)
