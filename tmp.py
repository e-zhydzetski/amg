mult = lambda a, b: a.x * b.x + a.y * b.y


class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(" + str(self.x) + ";" + str(self.y) + ")"


class Line(object):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    @property
    def direction(self):
        return Point(self.end.x - self.begin.x, self.end.y - self.begin.y)

    @property
    def normal(self):
        return Point(self.end.y - self.begin.y, self.begin.x - self.end.x)

    def __str__(self):
        return "[" + str(self.begin) + ", " + str(self.end) + "]"


class Polygon(object):
    def __init__(self, points):
        self.count = len(points)
        self.edges = []
        for i in range(self.count - 1):
            self.edges.append(Line(points[i], points[i + 1]))

        self.edges.append(Line(points[-1], points[0]))

    # Реализаця алгоритма!
    def cyruse_beck(self, l):
        t_begin = 0.0
        t_end = 1.0
        dirL = l.direction
        for edge in self.edges:
            dir_edg = edge.direction
            Q = Point(l.begin.x - dir_edg.x, l.begin.y - dir_edg.y)
            N = edge.normal
            Pn = mult(dirL, N)
            Qn = mult(Q, N)
            if Pn == 0:
                pass
            else:
                t = -Qn / Pn
                if Pn > 0:
                    if t < t_begin:
                        return False
                    t_end = min(t_end, t)
                else:
                    if t > t_end:
                        return False
                    t_begin = max(t_begin, t)

        if t_end > t_begin:
            if t_begin > 0:
                l.begin = Point(l.begin.x + t_begin * dirL.x, l.begin.y + t_begin * dirL.y)
            if t_end < 1:
                l.end = Point(l.begin.x + t_end * dirL.x, l.begin.y + t_end * dirL.y)
        else:
            return False
        return True


p = Polygon([Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)])
l = Line(Point(-0.5, -0.5), Point(2.5, 2.5))
print(p.cyruse_beck(l))
print("Line: %s" % l)
l = Line(Point(-0.5, -0.5), Point(2.5, -0.5))
print(p.cyruse_beck(l))
l = Line(Point(0, -1), Point(3, 2))
print(p.cyruse_beck(l))
print("Line: %s" % l)
