# Grid
from tkinter import *

window = Tk()
window.title("GUI Grid")

title = Label(window, text="Masukkan Data Diri", font=('Arial', 20)).grid(row=0, column=0, columnspan=2)

firstname = Label(window, text="Masukan nama depan: ", font=('Arial', 15)).grid(row=1, column=0, sticky=W)
inputfirst = Entry(window, font=('Arial', 15)).grid(row=1, column=1)

lastname = Label(window, text="Masukan nama belakang: ", font=('Arial', 15)).grid(row=2, column=0, sticky=W)
inputlast = Entry(window, font=('Arial', 15)).grid(row=2, column=1)

telp = Label(window, text="Masukan Telepon: ", font=('Arial', 15)).grid(row=3, column=0, sticky=W)
inputtelp = Entry(window, font=('Arial', 15)).grid(row=3, column=1)

email = Label(window, text="Masukan Email: ", font=('Arial', 15)).grid(row=4, column=0, sticky=W)
inputemail = Entry(window, font=('Arial', 15)).grid(row=4, column=1)

submit_btn = Button(window, text="SUBMIT", font=('Arial', 15)).grid(row=5, columnspan=2)

window.mainloop()