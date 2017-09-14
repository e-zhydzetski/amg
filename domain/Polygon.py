import math
import random

import domain


class Polygon(object):
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.displayed_figure_id = None
        self.canvas = None

    def __len__(self):
        return len(self.vertexes)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if len(other) != len(self):
                raise AttributeError("different length of polygons for +")
            new_vertexes = []
            for i in range(0, len(self.vertexes)):
                new_vertexes.append(self.vertexes[i] + other.vertexes[i])
            return Polygon(new_vertexes)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

    def paint(self, canvas, visible=True):
        if self.displayed_figure_id is not None:
            self.canvas.delete()

        paintable_vertexes = []
        for vertex_point in self.vertexes:
            paintable_vertexes.append(vertex_point.x)
            paintable_vertexes.append(vertex_point.y)

        outline_clr = 'gray'
        fill_clr = ''
        if visible:
            outline_clr = ''
            fill_clr = 'red'

        self.canvas = canvas
        self.displayed_figure_id = self.canvas.create_polygon(paintable_vertexes, fill=fill_clr, outline=outline_clr)

    def clear(self):
        if self.displayed_figure_id is not None:
            self.canvas.delete(self.displayed_figure_id)
        self.displayed_figure_id = None
        self.canvas = None


class PolygonFactory(object):
    @staticmethod
    def create_random(center_x, center_y, radius, vertex_count):
        vertexes = []
        segment = math.pi * 2 / vertex_count / 10
        for i in range(0, vertex_count):
            rand = random.randint(0, 9)
            direction = segment * (10 * i + rand)

            vertexes.append(domain.Point(
                center_x + radius * math.cos(direction),
                center_y + radius * math.sin(direction))
            )
        return Polygon(vertexes)
