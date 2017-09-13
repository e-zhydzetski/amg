from tkinter import *

import domain

canvas = Canvas(width=900, height=900)
canvas.pack()

p_from = domain.PolygonFactory.create_random(250, 250, 200, 5)
p_from.paint(canvas, visible=False)

p_to = domain.PolygonFactory.create_random(650, 650, 200, 6)
p_to.paint(canvas, visible=False)

route = domain.Route(p_from, p_to, 200)

route.paint(canvas)

prev_polygon = None

shadow = False


def paint_move():
    global route
    global canvas
    global prev_polygon
    global shadow

    if not route.finished():
        if prev_polygon is not None and not shadow:
            prev_polygon.clear()
        prev_polygon = route.next_step()
        prev_polygon.paint(canvas)
        canvas.after(20, paint_move)


canvas.after(500, paint_move)
mainloop()
