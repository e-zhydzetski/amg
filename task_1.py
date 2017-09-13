from tkinter import *

import domain

canvas = Canvas(width=900, height=900)
canvas.pack()

p_from = domain.PolygonFactory.create_random(200, 200, 100, 5)
p_from.paint(canvas, visible=False)

p_to = domain.PolygonFactory.create_random(700, 700, 150, 6)
p_to.paint(canvas, visible=False)

route = domain.Route(p_from, p_to, 200)

# route.paint(canvas)

full_polygon = None
cur_polygon = None

shadow_mode = False

window_mode = True

window = None
if window_mode:
    window = domain.RectWindow(domain.Point(150, 400), domain.Point(750, 500))
    window.paint(canvas)
    # p1 = domain.Point(320, 700)
    # p2 = domain.Point(200, 200)
    # canvas.create_line(p1.x, p1.y, p2.x, p2.y)
    # p1, p2 = window.cut_segment(p1, p2)
    # if p1 is not None:
    #     canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill='red')


def paint_move(pos=None):
    global route
    global canvas
    global cur_polygon
    global full_polygon
    global shadow_mode
    global window

    if not route.finished():
        if not shadow_mode:
            if full_polygon is not None:
                full_polygon.clear()
                full_polygon = None
            if cur_polygon is not None:
                cur_polygon.clear()
                cur_polygon = None

        full_polygon = route.next_step()

        if window_mode:
            cur_polygon = window.cut_polygon(full_polygon)
            if cur_polygon:
                cur_polygon.paint(canvas)
            full_polygon.paint(canvas, visible=False)
        else:
            full_polygon.paint(canvas)

        canvas.after(20, paint_move)


canvas.after(500, paint_move)

# canvas.bind("<Button-1>", paint_move)

mainloop()
