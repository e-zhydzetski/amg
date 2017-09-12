from tkinter import *
import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'").format(self.__class__, type(other))

    def __truediv__(self, other):
        if isinstance(other, int):
            return Point(self.x / other, self.y / other)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'").format(self.__class__, type(other))


class Polygon:
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.display = None
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

    def paint(self, canvas):
        if self.display is not None:
            self.canvas.delete()

        paintable_vertexes = []
        for vertex_point in self.vertexes:
            paintable_vertexes.append(vertex_point.x)
            paintable_vertexes.append(vertex_point.y)

        self.canvas = canvas
        self.display = self.canvas.create_polygon(paintable_vertexes, fill='white', outline="red")

    def clear(self):
        if self.display is not None:
            self.canvas.delete(self.display)
        self.display = None
        self.canvas = None


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
        self.current_step_idx = -1

        max_vertex_count = max(len(start.vertexes), len(finish.vertexes))

        self.start_vertexes = []
        self.finish_vertexes = []

        for i in range(0, max_vertex_count):
            start_idx = i % len(start.vertexes)
            self.start_vertexes.append(start.vertexes[start_idx])
            finish_idx = i % len(finish.vertexes)
            self.finish_vertexes.append(finish.vertexes[-finish_idx])

        self.aligned_start = Polygon(self.start_vertexes)

        deltas = []
        for i in range(0, max_vertex_count):
            deltas.append((self.finish_vertexes[i] - self.start_vertexes[i]) / step_count)
        self.delta = Polygon(deltas)

        self.steps.append(self.aligned_start)
        for i in range(1, step_count+1):
            self.steps.append(self.steps[i - 1] + self.delta)

    def finished(self):
        return self.current_step_idx == len(self.steps) - 1

    def next_step(self):
        if not self.finished():
            self.current_step_idx += 1
        return self.steps[self.current_step_idx]

    def paint(self, canvas):
        for i in range(0, len(self.start_vertexes)):
            s = self.start_vertexes[i]
            f = self.finish_vertexes[i]
            canvas.create_line(s.x, s.y, f.x, f.y)
            d = s + self.delta.vertexes[i]
            canvas.create_line(s.x, s.y, d.x, d.y, fill="red")

        for step in self.steps:
            step.paint(canvas)


c = Canvas(width=900, height=900, bg='grey80')
c.pack()

p_from = PolygonFactory.create_random(250, 250, 200, 5)
p_from.paint(c)

p_to = PolygonFactory.create_random(650, 650, 200, 6)
p_to.paint(c)

route = Route(p_from, p_to, 200)

# route.paint(c)

prev_polygon = None

shadow = False


def paint_move(route, canvas):
    global prev_polygon
    global shadow
    if not route.finished():
        if prev_polygon is not None and not shadow:
            prev_polygon.clear()
        prev_polygon = route.next_step()
        prev_polygon.paint(canvas)
        canvas.after(20, paint_move, route, canvas)


c.after(500, paint_move, route, c)
mainloop()
