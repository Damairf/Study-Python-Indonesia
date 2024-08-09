# Multiple Animation
from tkinter import *
from GUI_Animations_Multiple_ball import *
import time

WIDTH = 500
HEIGHT = 500

window = Tk()
window.title("GUI Multiple Animation")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bola_volley = Bola_canvas(canvas, 0, 0, 100, 2, 3, "yellow")
bola_tennis = Bola_canvas(canvas, 10, 10, 50, 3, 4, "green")
bola_basket = Bola_canvas(canvas, 20, 20, 100, 1, 3, "orange")
bola_pingpong = Bola_canvas(canvas, 0, 0, 30, 5, 6, "red")
bola_ungu = Bola_canvas(canvas, 10, 10, 80, 3, 2, "purple")
bola_pink = Bola_canvas(canvas, 20, 20, 60, 4, 5, "pink")

while True:
    bola_pink.move()
    bola_pingpong.move()
    bola_basket.move()
    bola_tennis.move()
    bola_volley.move()
    bola_ungu.move()
    window.update()
    time.sleep(0.01)

window.mainloop()