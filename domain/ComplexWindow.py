import domain


class ComplexWindow:
    def __init__(self, windows):
        self.windows = windows

    def paint(self, canvas):
        for wnd in self.windows:
            wnd.paint(canvas)

    def cut_polygon(self, polygon):
        result_polygons = []
        for wnd in self.windows:
            result_polygon = wnd.cut_polygon(polygon)
            if result_polygon:
                result_polygons.append(result_polygon)
        return result_polygons


class ComplexWindowFactory:
    @staticmethod
    def create_cross(center_x, center_y, radius, width):
        wnd1 = domain.RectWindow(
            domain.Point(center_x - radius, center_y - width // 2),
            domain.Point(center_x + radius, center_y + width // 2)
        )
        wnd2 = domain.RectWindow(
            domain.Point(center_x - width // 2, center_y - radius),
            domain.Point(center_x + width // 2, center_y + radius)
        )
        return ComplexWindow([wnd1, wnd2])
