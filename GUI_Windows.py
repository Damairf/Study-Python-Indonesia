# GUI Window
from tkinter import *
# widgets = GUI elements; button, textbox, label, image
# Window = Container untuk menahan semua widgets

window = Tk()   # Menginisiasi sebuah window
window.geometry("420x420")
window.title("GUI Window Python")
icon = PhotoImage(file='Gambar\\stopwatch.png')
window.iconphoto(True, icon)
window.config(background="#4b85d1")

window.mainloop()   # Untuk menampilkan window ke layar     