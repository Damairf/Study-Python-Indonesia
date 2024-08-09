# Keyboard Event
from tkinter import *

def enter(event):
    label.config(text=event.keysym)

window = Tk()
window.title("GUI Keyboard Event")
window.geometry('420x420')

window.bind("<Key>", enter)

label = Label(window, font=("Arial", 50))
label.pack()

window.mainloop()