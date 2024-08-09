# Windows Tabs
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("GUI Window Tab")
window.geometry('400x400')

notebook = ttk.Notebook(window) # Mengatur jumlah jendela

tab1 = Frame(notebook)      # Membuat frame baru tab 1
tab2 = Frame(notebook)      # Membuat frame baru tab 2
tab3 = Frame(notebook)      # Membuat frame baru tab 3

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")
notebook.pack(expand=True, fill=BOTH)   # expand = melebarkan untuk mengisi ruang yang kosong
                                        # fill = mengisi ruang pada sumbu x dan y

Label(tab1, text="Ini adalah tab 1", font=('Arial', 10, 'bold'), width=50, height=25, bg="red").pack()
Label(tab2, text="Ini adalah tab 2", font=('Arial', 10, 'bold'), width=50, height=25, bg="orange").pack()
Label(tab3, text="Ini adalah tab 3", font=('Arial', 10, 'bold'), width=50, height=25, bg="yellow").pack()

window.mainloop()