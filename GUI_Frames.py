# Frame
from tkinter import *

window = Tk()
window.title("GUI Frame")
window.geometry('400x400')

frame = Frame(window, bg="red", relief=RAISED, bd=10)
frame.place(x=90, y=100)

Button(frame, text="W", font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame, text="A", font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=('Consolas', 25), width=3).pack(side=LEFT)

window.mainloop()