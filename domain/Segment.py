import domain


class Segment(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __contains__(self, point):
        if isinstance(point, domain.Point):
            return abs((point.x - self.p1.x) * (self.p2.y - self.p1.y) - (self.p2.x - self.p1.x) * (point.y - self.p1.y)) < 1 \
                   and min(self.p1.x, self.p2.x) <= point.x <= max(self.p1.x, self.p2.x)
        else:
            raise TypeError("unsupported operand type for in, should be Point")

    @property
    def normal(self):
        return (self.p2 - self.p1).normal
