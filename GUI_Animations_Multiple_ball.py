# Multiple Animation Class Ball
class Bola_canvas:
    def __init__(self, canvas, x, y, diameter, kecepatanX, kecepatanY, warna):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=warna)
        self.kecepatanX = kecepatanX
        self.kecepatanY = kecepatanY
        
    def move(self):
        koordinat = self.canvas.coords(self.image)
        if(koordinat[2]>(self.canvas.winfo_width()) or koordinat[0]<(0)):
            self.kecepatanX = -self.kecepatanX
        if(koordinat[3]>(self.canvas.winfo_height()) or koordinat[1]<(0)):
            self.kecepatanY = -self.kecepatanY
        self.canvas.move(self.image, self.kecepatanX, self.kecepatanY)