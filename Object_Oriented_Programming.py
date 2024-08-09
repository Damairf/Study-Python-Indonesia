# Object Oriented Programming
from Object_Oriented_Programming_Mobil import Mobil

mobil1 = Mobil("Toyota", "Avanza", "Putih")
mobil2 = Mobil("Honda", "Civic", "Hitam")

print(mobil1.merk, mobil1.seri, mobil1.warna)
mobil1.jalan()
print(mobil2.merk, mobil2.seri, mobil2.warna)
mobil2.berhenti()