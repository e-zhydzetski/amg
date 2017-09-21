import domain


class PolygonWindow(object):
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.segments = []
        for i in range(0, len(self.vertexes)):
            segment = domain.Segment(self.vertexes[i - 1], self.vertexes[i])
            self.segments.append(segment)

    def paint(self, canvas):
        canvas_vertexes = []
        for vertex_point in self.vertexes:
            canvas_vertexes.append(vertex_point.x)
            canvas_vertexes.append(vertex_point.y)

        canvas.create_polygon(canvas_vertexes, fill="white", outline="")

    def cut_segment(self, p1, p2):
        intersection = False  # crutch
        p1_inside = True  # crutch
        t1 = -1
        t2 = 2
        for ws in self.segments:
            wsn = ws.normal
            P = (p2 - p1) * wsn
            Q = (p1 - ws.p1) * wsn

            if Q < 0:
                p1_inside = False

            if P == 0:
                if Q < 0:
                    return None, None
                else:
                    pass
            else:
                t = - Q / P
                if 1 >= t >= 0:
                    p = p1 + (p2 - p1) * t  # crutch
                    if p in ws:  # crutch
                        intersection = True
                        if P < 0:
                            t2 = min(t, t2)
                        else:
                            t1 = max(t, t1)

        if t2 > 1 and (intersection or p1_inside):
            t2 = 1

        if t1 < 0 and (intersection or p1_inside):
            t1 = 0

        if t1 < 0 and t2 > 1 or t1 > t2:
            return None, None

        new_p1 = p1 + (p2 - p1) * t1
        new_p2 = p1 + (p2 - p1) * t2

        return new_p1, new_p2

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
