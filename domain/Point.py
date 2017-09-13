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
