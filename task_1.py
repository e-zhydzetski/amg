from tkinter import *
import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)


class Polygon:
    def __init__(self, vertexes):
        self.vertexes = vertexes

    def paint(self, canvas):
        paintable_vertexes = []
        for vertex_point in self.vertexes:
            paintable_vertexes.append(vertex_point.x)
            paintable_vertexes.append(vertex_point.y)
        canvas.create_polygon(paintable_vertexes, fill='white', outline="red")


class PolygonFactory:
    @staticmethod
    def create_random(center_x, center_y, radius, vertex_count):
        vertexes = []
        segment = math.pi * 2 / vertex_count / 10
        for i in range(0, vertex_count):
            rand = random.randint(0, 9)
            direction = segment * (10 * i + rand)

            vertexes.append(Point(
                center_x + radius * math.cos(direction),
                center_y + radius * math.sin(direction))
            )
        return Polygon(vertexes)


class Route:
    def __init__(self, start, finish, step_count):
        self.steps = []

        max_vertex_count = max(len(start.vertexes), len(finish.vertexes))
        print(max_vertex_count)

        self.start_vertexes = []
        self.finish_vertexes = []

        for i in range(0, max_vertex_count):
            start_idx = i % len(start.vertexes)
            self.start_vertexes.append(start.vertexes[start_idx])
            finish_idx = i % len(finish.vertexes)
            self.finish_vertexes.append(finish.vertexes[-finish_idx])

        self.deltas = []

        for i in range(0, max_vertex_count):
            self.deltas.append((self.finish_vertexes[i] - self.start_vertexes[i]) / step_count)

        print(self.deltas)

    def paint(self, canvas):
        for i in range(0, len(self.start_vertexes)):
            s = self.start_vertexes[i]
            f = self.finish_vertexes[i]
            canvas.create_line(s.x, s.y, f.x, f.y)
            d = s + self.deltas[i]
            canvas.create_line(s.x, s.y, d.x, d.y, fill="red")


c = Canvas(width=900, height=900, bg='grey80')
c.pack()

p_from = PolygonFactory.create_random(250, 250, 200, 5)
p_from.paint(c)

p_to = PolygonFactory.create_random(650, 650, 200, 6)
p_to.paint(c)

route = Route(p_from, p_to, 20)
route.paint(c)

mainloop()
