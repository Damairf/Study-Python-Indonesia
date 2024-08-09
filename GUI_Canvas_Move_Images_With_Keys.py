# Move Canvas Images With Keys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def atas1(event):
    canvas1.move(image_canvas1, 0, -10)
def bawah1(event):
    canvas1.move(image_canvas1, 0, +10)
def kiri1(event):
    canvas1.move(image_canvas1, -10, 0)
def kanan1(event):
    canvas1.move(image_canvas1, +10, 0)

def keluar(event):
    if (messagebox.askyesno(title="Keluar", message="Apakah anda yakin ingin keluar?")):
        quit()

window = Tk()
window.title("GUI Move Image With Keys")

window.bind("<w>", atas1)
window.bind("<s>", bawah1)
window.bind("<a>", kiri1)
window.bind("<d>", kanan1)
window.bind("<Up>", atas1)
window.bind("<Down>", bawah1)
window.bind("<Left>", kiri1)
window.bind("<Right>", kanan1)

window.bind("<q>", keluar)

image_icon = PhotoImage(file='Gambar\\senyumkuning.png')

canvas1 = Canvas(window, width=500, height=500, bg="red")
canvas1.pack()
image_canvas1 = canvas1.create_image(10, 10, image=image_icon, anchor=NW)

window.mainloop()