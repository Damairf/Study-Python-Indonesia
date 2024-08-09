# Entry Box
from tkinter import *

window = Tk()
window.title("Entry Box GUI")

def submit():
    text_input = entry.get()
    print("Password: "+text_input)
    # entry.config(state=DISABLED)          # Membuat entry box tidak aktif
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)

entry = Entry(window,
              font=('Arial', 30),
              fg="Orange",
              bg="Black",
              show="*")                     # Membuat teks yang diinput pada kolom menjadi *
# entry.insert(0, "Masukkan password")      # Membuat teks awalan sebagai contoh

entry.pack(side=LEFT)

delete_btn = Button(window, text="DELETE",font=('Arial', 10), command=delete, fg='Black', bg='Orange')
delete_btn.pack(side=RIGHT)

backspace_btn = Button(window, text="BACKSPACE",font=('Arial', 10), command=backspace, fg='Black', bg='Orange')
backspace_btn.pack(side=RIGHT)

input_btn = Button(window, text="SUBMIT",font=('Arial', 10), command=submit, fg='Black', bg='Orange')
input_btn.pack(side=RIGHT)

window.mainloop() 