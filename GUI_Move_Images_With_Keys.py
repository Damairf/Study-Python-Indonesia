# Move Images With Keys
from tkinter import *
from tkinter import messagebox

def atas(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def bawah(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def kiri(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def kanan(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())
def keluar(event):
    if messagebox.askyesno(title="Keluar", message="Apakah anda yakin ingin keluar?"):
        quit()

window = Tk()
window.title("GUI Move Image With Keys")
window.geometry("500x500")

image_icon = PhotoImage(file='Gambar\\senyumkuning.png')
label = Label(window, image=image_icon)
label.place(x=0, y=0)

window.bind("<w>", atas)
window.bind("<a>", kiri)
window.bind("<s>", bawah)
window.bind("<d>", kanan)
window.bind("<Up>", atas)
window.bind("<Left>", kiri)
window.bind("<Down>", bawah)
window.bind("<Right>", kanan)
window.bind("<q>", keluar)

window.mainloop()