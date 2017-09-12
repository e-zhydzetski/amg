from tkinter import *

c = Canvas(width=460, height=460, bg='grey80')
c.pack()

oval = c.create_oval(30, 10, 130, 80, fill="orange")
c.create_rectangle(180, 10, 280, 80, tag="rect", fill="lightgreen")
trian = c.create_polygon(330, 80, 380, 10, 430, 80, fill='white', outline="red")


def oval_func(event):
    c.delete(oval)
    c.create_text(30, 10, text="Здесь был круг", anchor="w")


def rect_func(event):
    c.delete("rect")
    c.create_text(180, 10, text="Здесь был\nпрямоугольник", anchor="nw")


def triangle(event):
    c.create_polygon(350, 70, 380, 20, 410, 70, fill='yellow', outline="black")


c.tag_bind(oval, '<Button-1>', oval_func)
c.tag_bind("rect", '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)


def reset_figures():
    global oval
    global trian
    c.delete(oval)
    oval = c.create_oval(30, 10, 130, 80, fill="orange")
    c.tag_bind(oval, '<Button-1>', oval_func)
    c.delete("rect")
    c.create_rectangle(180, 10, 280, 80, tag="rect", fill="lightgreen")
    c.tag_bind("rect", '<Button-1>', rect_func)
    c.delete(trian)
    trian = c.create_polygon(330, 80, 380, 10, 430, 80, fill='white', outline="red")
    c.tag_bind(trian, '<Button-1>', triangle)
    c.after(1000, reset_figures)
    

reset_figures()

c.after(1000, reset_figures)

mainloop()
