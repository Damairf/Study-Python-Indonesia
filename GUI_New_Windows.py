# New Window
# Toplevel() = window yang paling atas (jika induk window ditutup maka akan ikut tertutup, 
#              tetapi jika top window ditutup, induk tidak ikut tertutup)
# Tk() = window mandiri, tidak terikat dengan window apapun (jika induk dihapus
#        window tk tidak akan ikut tertutup) 

from tkinter import *

def new_tab():
    new_window = Tk()       # Akan membuka jendela baru
    new_window.title("GUI New Window 2")
    new_window.geometry('300x50')
    old_window.destroy()    # Akan menghancurkan jendela lama

old_window = Tk()
old_window.title("GUI New Window")
old_window.geometry('300x50')

Button(old_window, text="Buka jendela baru", command=new_tab).pack()

old_window.mainloop()