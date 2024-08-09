# Color Chooser
from tkinter import *
from tkinter import colorchooser

window = Tk()
window.title("GUI Color Chooser")
window.geometry("420x420")

def click_cmd():
    color = colorchooser.askcolor()
    colorhex = color[1]
    print(colorhex)
    window.config(background=colorhex)      # Merubah warna background pada window

click_btn = Button(window,
               text="BUTTON",
               command=click_cmd)
click_btn.pack()

window.mainloop()