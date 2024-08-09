# File Open Dialog
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("GUI File Dialog Open")
window.geometry("400x400")

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\ASUS\\Documents",      # Memberikan lokasi awal open file
                                          title="Membuka File Dalam Komputer",
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))    # Memberikan filter tipe file yang cocok
    file = open(filepath, 'r')
    print(file.read())
    file.close()

button = Button(window,
                font=("Arial", 20, 'bold'),
                text="OPEN FILE",
                command=openfile)
button.place(x=120, y=150)

window.mainloop()