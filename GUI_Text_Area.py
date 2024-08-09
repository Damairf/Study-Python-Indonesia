# Text Area
from tkinter import *

window = Tk()
window.title("GUI Text Area")

def submit_cmd():
    masukan = teks.get("1.0", END)      # Mengambil teks dari indeks pertama sampai terakhir
    print(masukan)
    
def delete_cmd():
    teks.delete("1.0", END)

teks = Text(window,
            font=("Constantia", 20),
            height=10,
            width=50,
            padx=20,
            pady=20,
            bg="Light Yellow")
teks.pack()

submit_btn = Button(window,
                    text="SUBMIT",
                    command=submit_cmd,
                    font=('Arial', 15, 'bold'))
submit_btn.pack(side=RIGHT)

delete_btn = Button(window,
                    text="DELETE",
                    command=delete_cmd,
                    font=('Arial', 15, 'bold'))
delete_btn.pack(side=RIGHT)

window.mainloop()