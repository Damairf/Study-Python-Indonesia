# Super Function
class Persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
class Persegi(Persegi_panjang):
    def __init__(self, panjang, lebar):
        super().__init__(panjang, lebar)
    def luas(self):
        return self.panjang*self.lebar
        
class Kubus(Persegi_panjang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__(panjang, lebar)
        self.tinggi = tinggi
    def volume(self):
        return self.panjang*self.lebar*self.tinggi
    
pilihan = int(input("Daftar rumus:\n1. Luas Persegi\n2. Volume Kubus\nPilihan anda: "))
if pilihan == 1:
    angka = int(input("Masukkan sisi persegi: "))
    persegi = Persegi(angka, angka)
    print("Luas persegi dengan sisi "+str(angka)+" adalah "+str(persegi.luas()))
if pilihan == 2:
    angka = int(input("Masukkan sisi kubus: "))
    kubus = Kubus(angka, angka, angka)
    print("Luas kubus dengan sisi "+str(angka)+" adalah "+str(kubus.volume()))