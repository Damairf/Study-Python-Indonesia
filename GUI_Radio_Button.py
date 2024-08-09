# Radio Button
from tkinter import *

makanan = ['Nasi Goreng Ayam', 'Nasi Goreng Seafood', 'Nasi Goreng Mawut', 'Nasi Goreng Telur']

def pesan():
    if (x.get()==0):
        print("Kamu memesan nasi goreng ayam")
    elif (x.get()==1):
        print("Kamu memesan nasi goreng Seafood")
    elif (x.get()==2):
        print("Kamu memesan nasi goreng mawut")
    elif (x.get()==3):
        print("Kamu memesan nasi goreng telur")

window = Tk()
window.title("Radio Button GUI")

x = IntVar()

nasgorAyam = PhotoImage(file='Gambar\\senyumkuning.png')
nasgorSeafood = PhotoImage(file='Gambar\\senyumkuning.png')
nasgorMawut = PhotoImage(file='Gambar\\senyumkuning.png')
nasgorTelur = PhotoImage(file='Gambar\\senyumkuning.png')

makananImage = [nasgorAyam, nasgorSeafood, nasgorMawut, nasgorTelur]    # Memberi gambar pada tiap indeks

for index in range (len(makanan)):
    radiobutton = Radiobutton(window,
                              text=makanan[index],  # Membuat button setiap teks pada list array
                              variable=x,           # Memberikan variable kepada list array
                              value=index,          # Memberikan value pada setiap index
                              padx=20,
                              command=pesan,
                              font=('Arial', 20, 'bold'),
                              image=makananImage[index],    # Memasukkan gambar tiap indeks
                              compound=LEFT,
                              indicatoron=0,        # Menghilangkan kolom button checkbox
                              width=480)
    radiobutton.pack(anchor=W)              # Membuat supaya semua button rata kiri / west

window.mainloop()