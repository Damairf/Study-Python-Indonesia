# Checkbox
from tkinter import *

window = Tk()
window.title("Checkbox GUI")

photo = PhotoImage(file='Gambar\\senyumkuning.png')

def hasil():
    if (x.get()== 1):           # Jika value dari variable adalah on
        print("Kamu setuju")
    else:
        print("Kamu tidak setuju")

x = IntVar()        # Menentukan value variabel, bisa int, string, boolean

chek_button = Checkbutton(window,
                          text="Saya setuju",
                          variable=x,       # Menentukan variabel sebagai value
                          onvalue=1,        # Menentukan value jika on
                          offvalue=0,       # Menentukan value jika off
                          command=hasil,
                          font=('Arial', 20, 'bold'),
                          fg='Black',
                          bg='Orange',
                          activeforeground='Black',
                          activebackground='Orange',
                          padx=20,
                          pady=10,
                          image=photo,
                          compound=LEFT)
chek_button.pack()

window.mainloop()