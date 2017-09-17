class Segment(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    @property
    def normal(self):
        return (self.p2 - self.p1).normal
