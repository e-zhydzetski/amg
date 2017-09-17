class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False

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

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Point(self.x * other, self.y * other)
        else:
            if isinstance(other, self.__class__):
                return self.x * other.x + self.y * other.y
            else:
                raise TypeError("unsupported operand type(s) for *: '{}' and '{}'").format(self.__class__, type(other))

    @property
    def normal(self):
        return Point(-self.y, self.x)
