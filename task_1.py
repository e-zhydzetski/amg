from tkinter import *

import domain

canvas = Canvas(width=900, height=900)
canvas.pack()

p_from = domain.PolygonFactory.create_random(150, 150, 100, 5)
p_from.paint(canvas, visible=False)

p_to = domain.PolygonFactory.create_random(700, 700, 150, 6)
p_to.paint(canvas, visible=False)

route = domain.Route(p_from, p_to, 300)

# route.paint(canvas)

full_polygon = None
visible_polygon_parts = None

shadow_mode = False

window_mode = 2

window = None
if window_mode == 1:
    window = domain.ComplexWindowFactory.create_cross(450, 450, 300, 100)
if window_mode == 2:
    window = domain.PolygonWindow([
        domain.Point(450, 350),
        domain.Point(550, 550),
        domain.Point(350, 550)
    ], canvas)

if window:
    window.paint(canvas)


def paint_move(pos=None):
    global route
    global canvas
    global visible_polygon_parts
    global full_polygon
    global shadow_mode
    global window

    if not route.finished():
        if not shadow_mode:
            if full_polygon is not None:
                full_polygon.clear()
                full_polygon = None
            if visible_polygon_parts is not None:
                for vpp in visible_polygon_parts:
                    vpp.clear()
                visible_polygon_parts = None

        full_polygon = route.next_step()

        if window_mode:
            visible_polygon_parts = window.cut_polygon(full_polygon)
            for vpp in visible_polygon_parts:
                vpp.paint(canvas)
            full_polygon.paint(canvas, visible=False)
        else:
            full_polygon.paint(canvas)

        # canvas.after(20, paint_move)


# canvas.after(500, paint_move)

canvas.bind("<Button-1>", paint_move)

p1 = None
def add_point(pos):
    global p1
    p = domain.Point(pos.x, pos.y)
    if p1:
        canvas.create_line(p1.x, p1.y, p.x, p.y)
        p1, p = window.cut_segment(p1, p)
        if p1 is not None:
            canvas.create_line(p1.x, p1.y, p.x, p.y, fill="red")
        p1 = None
    else:
        p1 = p


canvas.bind("<Button-3>", add_point)

mainloop()
