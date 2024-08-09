# Drag and Drop
from tkinter import *

def drag_start(event):
    widget = event.widget       # Menginisiasi supaya semua modul widget dapat menjalankan function yang sama
    widget.startX = event.x     # Mengambil titik x saat ini dan mengubah titik baru menjadi titik awal
    widget.startY = event.y     # Mengambil titik y saat ini dan mengubah titik baru menjadi titik awal

def motion_start(event):
    widget = event.widget       # Menginisiasi supaya semua modul widget dapat menjalankan function yang sama
    x = widget.winfo_x() - widget.startX + event.x      # info titik x saat ini - titik x sebelumnya + titik x terbaru
    y = widget.winfo_y() - widget.startY + event.y      # info titik y saat ini - titik y sebelumnya + titik y terbaru
    widget.place(x=x, y=y)

window = Tk()
window.title("GUI Drag and Drop")
window.geometry("400x400")

label1 = Label(window, bg="red", width=10, height=5)
label1.place(x=10, y=10)
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=200, y=200)

label1.bind("<Button-1>", drag_start)
label1.bind("<B1-Motion>", motion_start)
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", motion_start)

window.mainloop()