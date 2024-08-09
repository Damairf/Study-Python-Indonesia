    # Progress Bar
from tkinter import *
from tkinter.ttk import*
import time

def download():
    GB = 100
    x = 0
    speed = 2
    while(x<GB):
        time.sleep(0.05)
        progress_bar['value']+=(speed/GB)*100
        x+=speed
        percent.set(str(int((x/GB)*100))+"%")
        text.set(str(x)+"/"+str(GB)+" berhasil di download")
        window.update_idletasks()

window = Tk()
window.title("GUI Progress Bar")

text = StringVar()
percent = StringVar()

progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10)

completed = Label(window, textvariable=text).pack()
persen = Label(window, textvariable=percent).pack()

button = Button(window, text="DOWNLOAD", command=download).pack()

window.mainloop()