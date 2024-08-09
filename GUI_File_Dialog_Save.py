# File Save Dialog
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

window = Tk()
window.title("GUI File Dialog Save")

def save_cmd():
    file = filedialog.asksaveasfile(initialdir="D:\\Projek\\Projek-Code\\Latihan\\Python\\File",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    if file is None:
        return
    filetext = str(teks.get("1.0", END))
    file.write(filetext)
    file.close()
    messagebox.showinfo(title="Save Berhasil", message="File berhasil disimpan")

teks = Text(window,
            font=('Arial', 15),
            width=50,
            height=10,
            bg="light yellow",
            padx=20,
            pady=20)
teks.pack()

save_btn = Button(window,
                  font=('Arial', 15, 'bold'),
                  command=save_cmd,
                  text="SAVE")
save_btn.pack()

window.mainloop()