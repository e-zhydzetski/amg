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

prev_polygon = None

shadow_mode = False

window_mode = True

if window_mode:
    window = domain.RectWindow(domain.Point(300, 300), domain.Point(600, 600))
    window.paint(canvas)


def paint_move():
    global route
    global canvas
    global prev_polygon
    global shadow_mode

    if not route.finished():
        if prev_polygon is not None and not shadow_mode:
            prev_polygon.clear()
        prev_polygon = route.next_step()
        prev_polygon.paint(canvas)
        canvas.after(20, paint_move)


canvas.after(500, paint_move)
mainloop()
