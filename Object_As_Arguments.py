# Object As Arguments
class Mobil:
    warna = None

class Motor:
    warna = None

def ganti_warna(kendaraan, warna):
    kendaraan.warna = warna
    
mobil = Mobil()
motor = Motor()

ganti_warna(mobil,"Merah")
ganti_warna(motor,"Biru")

print("Mobil berwarna",mobil.warna)
print("Motor berwarna",motor.warna)