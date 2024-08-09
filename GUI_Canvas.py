# Canvas
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("GUI Canvas")
icon = PhotoImage(file='Gambar\\senyumkuning.png')
window.iconphoto(True, icon)

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Canvas 1")
notebook.add(tab2, text="Canvas 2")
notebook.pack(expand=True, fill=BOTH)

canvas1 = Canvas(tab1, width=500, height=500)
canvas1.create_rectangle(50, 50, 200, 200, fill="blue", outline="black", width=4)
points_segitiga = [250, 300, 180, 400, 320, 400]
canvas1.create_polygon(points_segitiga, fill="green", outline="black", width=4)
canvas1.create_arc(0, 0, 500, 500, fill="pink", style=PIESLICE, start=0, width=4)
canvas1.create_line(0, 0, 500, 500, fill="red", width=5)
canvas1.create_line(0, 500, 500, 0, fill="orange", width=5)
canvas1.pack()

# Membutuhkan 4 koordinat, koordinat x y untuk titik awalan dan koordinat x y untuk titik akhiran

canvas2 = Canvas(tab2, width=500, height=500)
canvas2.create_arc(0, 0, 500, 500, extent=180, fill="red", outline="black", width=5)
canvas2.create_arc(0, 0, 500, 500, extent=180, start=180, fill="white", outline="black", width=5)
canvas2.create_oval(180, 180, 320, 320, fill="white", outline="black", width=5)
canvas2.pack()

window.mainloop()