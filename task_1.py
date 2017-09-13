from tkinter import *

import domain

canvas = Canvas(width=900, height=900)
canvas.pack()

p_from = domain.PolygonFactory.create_random(250, 250, 200, 5)
p_from.paint(canvas, visible=False)

p_to = domain.PolygonFactory.create_random(650, 650, 200, 6)
p_to.paint(canvas, visible=False)

route = domain.Route(p_from, p_to, 200)

# route.paint(canvas)

cur_polygon = None

shadow_mode = False

window_mode = True

if window_mode:
    window = domain.RectWindow(domain.Point(300, 300), domain.Point(600, 600))
    window.paint(canvas)
    # p1 = domain.Point(420, 700)
    # p2 = domain.Point(700, 200)
    # canvas.create_line(p1.x, p1.y, p2.x, p2.y)
    # p1, p2 = window.cut_segment(p1, p2)
    # if p1 is not None:
    #     canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill='red')


def paint_move():
    global route
    global canvas
    global cur_polygon
    global shadow_mode

    if not route.finished():
        if cur_polygon is not None and not shadow_mode:
            cur_polygon.clear()
        cur_polygon = route.next_step()
        cur_polygon.paint(canvas)
        canvas.after(20, paint_move)


# canvas.after(500, paint_move)
mainloop()
