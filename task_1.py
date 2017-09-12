from tkinter import *
import math
import random


class Polygon:
    def __init__(self, center_x, center_y, radius, vertex_count):
        self.__vertex_count = vertex_count
        self.__xs = []
        self.__ys = []
        seg = math.pi * 2 / vertex_count / 10
        for i in range(0, self.__vertex_count):
            rand = random.randint(0, 9)
            dir = seg * (10 * i + rand)

            self.__xs.append(center_x + radius * math.cos(dir))
            self.__ys.append(center_y + radius * math.sin(dir))

    def paint(self, canvas):
        vertexes = []
        for i in range(0, self.__vertex_count):
            vertexes.append(self.__xs[i])
            vertexes.append(self.__ys[i])
        canvas.create_polygon(vertexes, fill='white', outline="red")


c = Canvas(width=800, height=600, bg='grey80')
c.pack()

p_from = Polygon(150, 150, 100, 6)
p_from.paint(c)

p_to = Polygon(650, 450, 100, 5)
p_to.paint(c)

mainloop()
