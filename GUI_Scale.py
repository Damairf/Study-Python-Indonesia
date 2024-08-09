# Scale
from tkinter import *

window = Tk()
window.title("GUI Scale")

def submit():
    suhu = scale.get()
    if suhu <= 30:
        print("Suhu adalah", suhu, "derajat celcius")
        print("Suhu normal")
    else:
        print("Suhu adalah", suhu, "derajat celcius")
        print("Suhu panas")

photo = PhotoImage(file='Gambar\\senyumkuning.png')
photoLabel = Label(image=photo)
photoLabel.pack(side=RIGHT)

scale = Scale(window,
              from_=0,              # Untuk mengatur angka dalam skala
              to=100,               # Untuk mengatur angka dalam skala
              length=600,           # Untuk mengatur panjang skala
              orient=HORIZONTAL,    # Untuk mengatur orientasi skala (Vertical/Horizontal)   
              font=('consolas', 20),
              tickinterval=10,      # Menambahkan titik angka patokan dalam skala
              resolution=5,         # Membuat skala bertambah sesuai kelipatan
            # showvalue=0,          # 0 = menghilangkan indikator angka, 1 = untuk menampilkan
              troughcolor='Orange', # Memberikan warna pada garis skala
              fg='Orange',
              bg='Black',
              activebackground='Black')
scale.pack()
# scale.set(20)       # Mengatur titik awal dalam skala ke angka spesifik
scale.set(((scale['from']-scale['to'])/2)+scale['to'])  # Mengatur titik awal skala selalu di tengah

submit_btn = Button(window,
                text="SUBMIT",
                command=submit,
                font=('Arial', 15, 'bold'))
submit_btn.pack()

window.mainloop()