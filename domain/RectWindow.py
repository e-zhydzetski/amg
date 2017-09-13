import domain


class RectWindow:
    def __init__(self, tl, br):
        self.left = tl.x
        self.top = tl.y
        self.right = br.x
        self.bottom = br.y

    def __contains__(self, item):
        if isinstance(item, domain.Point):
            return self.left <= item.x <= self.right and self.top <= item.y <= self.bottom
        else:
            raise TypeError("unsupported operand type for in, should be Point")

    def paint(self, canvas):
        canvas.create_rectangle(self.left, self.top, self.right, self.bottom, fill="", outline="gray")
