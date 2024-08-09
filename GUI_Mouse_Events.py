# Mouse Event
from tkinter import *
from tkinter import ttk

def klik1(event):
    print("Kamu menekan mouse kiri")
    print("Koordinat: "+str(event.x)+","+str(event.y))
    print()
def klik2(event):
    print("Kamu menekan mouse tengah / wheel")
    print("Koordinat: "+str(event.x)+","+str(event.y))
    print()
def klik3(event):
    print("Kamu menekan mouse kanan")
    print("Koordinat: "+str(event.x)+","+str(event.y))
    print()
def klik4(event):
    print("Kamu melepas mouse")
    print("Koordinat: "+str(event.x)+","+str(event.y))
    print()
def klik5(event):
    print("Mouse memasuki area")
    print("Koordinat: "+str(event.x)+","+str(event.y))
    print()
def klik6(event):
    print("Mouse keluar dari area")
    print("Koordinat: "+str(event.x)+","+str(event.y))
    print()
def klik7(event):
    print("Koordinat: "+str(event.x)+","+str(event.y))

window = Tk()
window.title("GUI Mouse Event")
window.geometry("400x400")

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill=BOTH)

tab1 = Frame(notebook, bg="red")
tab2 = Frame(notebook, bg="orange")

notebook.add(tab1, text="Mouse 1")
notebook.add(tab2, text="Mouse 2")

tab1.bind("<Button-1>", klik1)        # Mouse klik kiri
tab1.bind("<Button-2>", klik2)        # Mouse klik tengah / wheel
tab1.bind("<Button-3>", klik3)        # Mouse klik kanan
tab1.bind("<ButtonRelease>", klik4)   # Akan berjalan ketika mouse dilepas
tab1.bind("<Enter>", klik5)           # Berjalan ketika mouse memasuki area
tab1.bind("<Leave>", klik6)           # Berjalan ketika mouse keluar dari area
tab2.bind("<Motion>", klik7)          # Akan selalu berjalan mengikuti arah mouse bergerak

window.mainloop()