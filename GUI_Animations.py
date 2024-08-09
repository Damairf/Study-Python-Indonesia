# Animation
from tkinter import *
from tkinter import messagebox
import time
import random

WIDTH = 500
HEIGHT = 500
kecepatan1X = 3
kecepatan1Y = 2
kecepatan2X = 4
kecepatan2Y = 5

def keluar(event):
    if (messagebox.askyesno(title="Keluar", message="Apakah anda ingin keluar?")):
        quit()

window = Tk()
window.title("GUI Animation")
window.bind("<q>", keluar)

image_icon = PhotoImage(file='Gambar\\senyumkuning.png')

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas1_img = canvas.create_image(0, 0, image=image_icon, anchor=NW)
canvas2_img = canvas.create_image(0, 400, image=image_icon, anchor=NW)
img_width = image_icon.width()
img_height = image_icon.height()

while True:
    koordinat1 = canvas.coords(canvas1_img)
    if (koordinat1[0]>(WIDTH-img_width) or koordinat1[0]<0):
        kecepatan1X = -kecepatan1X
    if (koordinat1[1]>(HEIGHT-img_height) or koordinat1[1]<0):
        kecepatan1Y = -kecepatan1Y
    
    koordinat2 = canvas.coords(canvas2_img)
    if (koordinat2[0]>(WIDTH-img_width) or koordinat2[0]<0):
        kecepatan2X = -kecepatan2X
    if (koordinat2[1]>(HEIGHT-img_height) or koordinat2[1]<0):
        kecepatan2Y = -kecepatan2Y
        
    canvas.move(canvas1_img, kecepatan1X, kecepatan1Y)
    canvas.move(canvas2_img, kecepatan2X, kecepatan2Y)
    window.update()
    time.sleep(0.01)
    
window.mainloop()