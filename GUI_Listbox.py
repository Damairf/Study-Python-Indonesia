# List Box
from tkinter import *

window = Tk()
window.title("GUI Listbox")

def pesan():
    makanan = []
    for i in listbox.curselection():
        makanan.insert(i, listbox.get(i))
        
    for i in makanan:
        print("Kamu memesan", i)
    
def tambah():
    masukan = tambah_menu.get()
    if masukan == "":
        print("Perlu memasukkan nama makanan")
    elif any(char.isdigit() for char in masukan):
        print("Tidak boleh memasukkan angka")
    else:
        listbox.insert(listbox.size(),masukan)
        listbox.config(height=listbox.size())
        
def hapus():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
        listbox.config(height=listbox.size())

listbox = Listbox(window,
                  font=('constantia', 20),
                  bg='Orange',
                  fg='Black',
                  width=18,
                  selectmode=MULTIPLE)      # Membuat supaya dapat memilih lebih dari 1 item dalam listbox
listbox.pack()
listbox.config(height=listbox.size())

listbox.insert(1,"Nasi Goreng")
listbox.insert(2,"Mie Goreng")
listbox.insert(3,"Capcay")
listbox.insert(4,"Mie Rebus")
listbox.insert(5,"Nasi Mawut")

tambah_menu = Entry(window,
                    font=('Constantia', 20),
                    width=18,
                    fg='Orange',
                    bg='Black')
tambah_menu.pack()

tambah_btn = Button(window,
                    font=('Arial', 15, 'bold'),
                    command=tambah,
                    text="TAMBAH")
tambah_btn.pack(side=LEFT)

pesan_btn = Button(window,
                    font=('Arial', 15, 'bold'),
                    command=pesan,
                    text="PESAN")
pesan_btn.pack(side=LEFT)

hapus_btn = Button(window,
                    font=('Arial', 15, 'bold'),
                    command=hapus,
                    text="HAPUS")
hapus_btn.pack(side=LEFT)

window.mainloop()