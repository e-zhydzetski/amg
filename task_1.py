from tkinter import *
import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Polygon:
    def __init__(self, vertex_points):
        self.vertex_points = vertex_points

    def paint(self, canvas):
        paintable_vertexes = []
        for vertex_point in self.vertex_points:
            paintable_vertexes.append(vertex_point.x)
            paintable_vertexes.append(vertex_point.y)
        canvas.create_polygon(paintable_vertexes, fill='white', outline="red")


class PolygonFactory:
    @staticmethod
    def create_random(center_x, center_y, radius, vertex_count):
        vertex_points = []
        segment = math.pi * 2 / vertex_count / 10
        for i in range(0, vertex_count):
            rand = random.randint(0, 9)
            direction = segment * (10 * i + rand)

            vertex_points.append(Point(
                center_x + radius * math.cos(direction),
                center_y + radius * math.sin(direction))
            )
        return Polygon(vertex_points)


class Route:
    def __init__(self, start, finish, step_count):
        self.steps = []


c = Canvas(width=800, height=600, bg='grey80')
c.pack()

p_from = PolygonFactory.create_random(150, 150, 100, 5)
p_from.paint(c)

p_to = PolygonFactory.create_random(650, 450, 100, 6)
p_to.paint(c)

mainloop()
