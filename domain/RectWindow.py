import domain
import settings


class RectWindow(object):
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
        canvas.create_rectangle(self.left, self.top, self.right, self.bottom, fill=settings.visible_background_color, outline="")

    def __calculate_mark_for_point(self, p):
        mark = 0
        if p.x < self.left:
            mark |= 1
        if p.x > self.right:
            mark |= 2
        if p.y > self.bottom:
            mark |= 4
        if p.y < self.top:
            mark |= 8
        return mark

    @staticmethod
    def __cut_with_vertical_border(x, p1, p2):
        dp = p2 - p1
        dx = x - p1.x
        return domain.Point(x, p1.y + dp.y * (dx / dp.x)), p2

    @staticmethod
    def __cut_with_horizontal_border(y, p1, p2):
        dp = p2 - p1
        dy = y - p1.y
        return domain.Point(p1.x + dp.x * (dy / dp.y), y), p2

    def cut_segment(self, p1, p2):
        mark1 = self.__calculate_mark_for_point(p1)
        mark2 = self.__calculate_mark_for_point(p2)

        if mark1 | mark2 == 0:
            return p1, p2

        if mark1 & mark2:
            return None, None

        mark_diff = mark1 ^ mark2

        if mark_diff & 1:
            if mark1 & 1:
                p1, p2 = self.__cut_with_vertical_border(self.left, p1, p2)
            else:
                p2, p1 = self.__cut_with_vertical_border(self.left, p2, p1)
            return self.cut_segment(p1, p2)

        if mark_diff & 2:
            if mark1 & 2:
                p1, p2 = self.__cut_with_vertical_border(self.right, p1, p2)
            else:
                p2, p1 = self.__cut_with_vertical_border(self.right, p2, p1)
            return self.cut_segment(p1, p2)

        if mark_diff & 4:
            if mark1 & 4:
                p1, p2 = self.__cut_with_horizontal_border(self.bottom, p1, p2)
            else:
                p2, p1 = self.__cut_with_horizontal_border(self.bottom, p2, p1)
            return self.cut_segment(p1, p2)

        if mark_diff & 8:
            if mark1 & 8:
                p1, p2 = self.__cut_with_horizontal_border(self.top, p1, p2)
            else:
                p2, p1 = self.__cut_with_horizontal_border(self.top, p2, p1)
            return self.cut_segment(p1, p2)

        return p1, p2

    def cut_polygon(self, polygon):
        result_vertexes = []
        prev_vertex = polygon.vertexes[0]

        for i in range(1, len(polygon.vertexes)):
            p1, p2 = self.cut_segment(prev_vertex, polygon.vertexes[i])
            if p1 is not None:
                if len(result_vertexes) == 0 or not result_vertexes[-1] == p1:
                    result_vertexes.append(p1)
                result_vertexes.append(p2)
            prev_vertex = polygon.vertexes[i]

        p1, p2 = self.cut_segment(prev_vertex, polygon.vertexes[0])
        if p1 is not None:
            if len(result_vertexes) == 0 or not result_vertexes[-1] == p1:
                result_vertexes.append(p1)
            result_vertexes.append(p2)

        if not len(result_vertexes):
            return []

        return [domain.Polygon(result_vertexes)]
