import domain


class Route(object):
    def __init__(self, start, finish, step_count):
        self.steps = []
        self.current_step_idx = -1

        max_vertex_count = max(len(start.vertexes), len(finish.vertexes))

        self.start_vertexes = []
        self.finish_vertexes = []

        for i in range(0, max_vertex_count):
            start_idx = i % len(start.vertexes)
            self.start_vertexes.append(start.vertexes[start_idx])
            finish_idx = i % len(finish.vertexes)
            self.finish_vertexes.append(finish.vertexes[-finish_idx])

        self.aligned_start = domain.Polygon(self.start_vertexes)

        deltas = []
        for i in range(0, max_vertex_count):
            deltas.append((self.finish_vertexes[i] - self.start_vertexes[i]) / step_count)
        self.delta = domain.Polygon(deltas)

        self.steps.append(self.aligned_start)
        for i in range(1, step_count+1):
            self.steps.append(self.steps[i - 1] + self.delta)

    def finished(self):
        return self.current_step_idx == len(self.steps) - 1

    def next_step(self):
        if not self.finished():
            self.current_step_idx += 1
        return self.steps[self.current_step_idx]

    def paint(self, canvas):
        for i in range(0, len(self.start_vertexes)):
            s = self.start_vertexes[i]
            f = self.finish_vertexes[i]
            canvas.create_line(s.x, s.y, f.x, f.y)
            d = s + self.delta.vertexes[i]
            canvas.create_line(s.x, s.y, d.x, d.y, fill="red")
