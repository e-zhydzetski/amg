import domain


class PolygonWindow(object):
    def __init__(self, vertexes, canvas):
        self.vertexes = vertexes
        self.segments = []
        for i in range(0, len(self.vertexes)):
            segment = domain.Segment(self.vertexes[i - 1], self.vertexes[i])
            self.segments.append(segment)

        self.canvas = canvas

    def paint(self, canvas):
        canvas_vertexes = []
        for vertex_point in self.vertexes:
            canvas_vertexes.append(vertex_point.x)
            canvas_vertexes.append(vertex_point.y)

        canvas.create_polygon(canvas_vertexes, fill="", outline="gray")

        for segment in self.segments:
            norm_segment = domain.Segment(segment.p1, segment.p1 + segment.normal)

            canvas.create_line(norm_segment.p1.x, norm_segment.p1.y, norm_segment.p2.x, norm_segment.p2.y)
            canvas.create_oval(norm_segment.p2.x - 2, norm_segment.p2.y - 2, norm_segment.p2.x + 2,
                               norm_segment.p2.y + 2)

    def cut_segment(self, p1, p2):
        t1 = None
        t2 = None
        for ws in self.segments:
            wsn = ws.normal
            P = (p2 - p1) * wsn
            Q = (p1 - ws.p1) * wsn
            if P == 0:
                if Q < 0:
                    return None, None
                else:
                    pass
            else:
                t = - Q / P
                if 1 >= t >= 0:
                    if P < 0:
                        t2 = min(t, t2) if t2 else t
                    else:
                        t1 = max(t, t1) if t1 else t

        if not t1 or not t2:
            return None, None

        if not t1:
            t1 = 0

        if not t2:
            t2 = 1

        if t1 > t2:
            return None, None

        new_p1 = p1 + (p2 - p1) * t1
        new_p2 = p1 + (p2 - p1) * t2

        # self.canvas.create_line(new_p1.x, new_p1.y, new_p2.x, new_p2.y, fill="red")

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
