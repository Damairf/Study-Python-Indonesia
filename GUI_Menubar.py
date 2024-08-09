# Menubar
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("GUI Menubar")
window.geometry("300x300")

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Projek\\Projek-Code\\Latihan\\Python\\File")
    file = open(filepath, 'r')
    print(file.read())
    file.close()

def saveFile():
    print("File berhasil disimpan")
    
def exitFile():
    quit()

def copyFile():
    print("Berhasil menyalin")

def cutFile():
    print("Berhasil memotong")

def pasteFile():
    print("Berhasil menempel")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,
                tearoff=0,
                font=('Arial', 10))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open",
                     command=openFile)
fileMenu.add_command(label="Save",
                     command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",
                     command=exitFile)

editMenu = Menu(menubar,
                tearoff=0,
                font=('Arial', 10))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy",
                     command=copyFile)
editMenu.add_command(label="Cut",
                     command=cutFile)
editMenu.add_command(label="Paste",
                     command=pasteFile)

window.mainloop()