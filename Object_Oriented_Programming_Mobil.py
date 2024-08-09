# Object Oriented Programming Mobil
class Mobil:
    
    roda = 4    # Class Variable = class yang dapat dirubah dari kelas lain
    
    def __init__(self,merk,seri,warna):
        self.merk = merk    # Instance Class = class yang hanya dimiliki def sendiri dan hanya dapat diedit oleh def sendiri
        self.seri = seri    # Instance Class = class yang hanya dimiliki def sendiri dan hanya dapat diedit oleh def sendiri
        self.warna = warna  # Instance Class = class yang hanya dimiliki def sendiri dan hanya dapat diedit oleh def sendiri
        
    def jalan(self):
        print("Mobil ini sedang berjalan")
    def berhenti(self):
        print("Mobil ini sedang berhenti")    