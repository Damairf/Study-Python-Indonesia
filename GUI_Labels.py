# Label
# Area untuk menaruk teks, gambar dalam window
from tkinter import *

window = Tk()
window.title("Label GUI")
# window.geometry("420x420")

photo = PhotoImage(file='Gambar\\senyumkuning.png')

label = Label(window,
        text="Hello World",             # Memasukkan text
        font=('Arial', 30, 'bold'),     # Memberikan custom font
        fg='#4b85d1',                   # Memberikan warna text
        bg='black',                     # Memberikan warna background
        relief='raised',                # Memberikan border pada label
        bd=10,                          # Mengatur ketebalan border
        padx=20,                        # Mengatur jarak sumbu x
        pady=20,                        # Mengatur jarak sumbu y
        image=photo,                    # Menambahkan gambar
        compound=BOTTOM)                # Mengatur posisi gambar pada label

label.pack()              # Akan otomatis menempel di tengah window
# label.place(x=100,y=100)    # Dapat mengatur tata letak pada window

window.mainloop()