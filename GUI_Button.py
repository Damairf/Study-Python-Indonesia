# Button
from tkinter import *

window = Tk()
window.title("Button GUI")
window.geometry("200x200")

photo = PhotoImage(file='Gambar\\senyumkuning.png')

count = 0

def klik():
    global count
    count+=1
    print(count)

button = Button(window,
                text="BUTTON",                  # Memasukkan teks              
                font=('Arial', 15, 'bold'),     # Memberikan custom font
                command=klik,                   # Memberikan perintah
                fg='Black',                     # Memberikan warna teks
                bg='#ff8c00',                   # Memberikan background button
                activeforeground='Black',       # Memberikan warna teks setelah button di tekan
                activebackground='#915000',     # Memberikan warna background setelah button di tekan
                state=ACTIVE,                   # Mengatur sifat button (Aktif/Nonaktif)
                padx=10,                        # Memberikan padding sumbu x
                pady=10,                        # Memberikan padding sumbu y
                image=photo,                    # Memasukkan gambar pada button
                compound=TOP)                   # Mengatur posisi gambar pada button
button.pack()

window.mainloop()