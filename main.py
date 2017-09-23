from tkinter import *

import domain
import settings

canvas = Canvas(width=900, height=900, bg=settings.window_mode and settings.invisible_background_color or settings.visible_background_color)
canvas.pack()

p_from = domain.PolygonFactory.create_random(150, 150, 100, 5)
p_from.paint(canvas, visible=False)

p_to = domain.PolygonFactory.create_random(700, 700, 100, 6)
p_to.paint(canvas, visible=False)

route = domain.Route(p_from, p_to, 300)

full_polygon = None
visible_polygon_parts = None

window = None
if settings.window_mode == 1:
    window = domain.ComplexWindowFactory.create_cross(450, 450, 300, 100)
if settings.window_mode == 2:
    window = domain.ComplexWindowFactory.create_3pyramid(400, 350, 200)

if window:
    window.paint(canvas)


def paint_move(pos=None):
    global route
    global canvas
    global visible_polygon_parts
    global full_polygon
    global window

    if not route.finished():
        if not settings.shadow_mode:
            if full_polygon is not None:
                full_polygon.clear()
                full_polygon = None
            if visible_polygon_parts is not None:
                for vpp in visible_polygon_parts:
                    vpp.clear()
                visible_polygon_parts = None

        full_polygon = route.next_step()

        if settings.window_mode:
            visible_polygon_parts = window.cut_polygon(full_polygon)
            full_polygon.paint(canvas, visible=False)
            for vpp in visible_polygon_parts:
                vpp.paint(canvas)
        else:
            full_polygon.paint(canvas)

        canvas.after(20, paint_move)


canvas.after(500, paint_move)

# canvas.bind("<Button-1>", paint_move)

mainloop()
