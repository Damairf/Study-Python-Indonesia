# String Format
makanan = "Kebab"
minuman = "Es Teh"

print("Saya makan {} dan minum {}".format(makanan,minuman))
print("Saya makan {1} dan minum {0}".format(makanan,minuman))

teks = "Saya makan {} dan minum {}"
print(teks.format(makanan,minuman))

print()
nama = "Safi"
umur = 20
print("Nama kamu {} Ayu".format(nama))
print("Nama kamu {:10} Ayu, umur kamu {} tahun".format(nama,umur))
print("Nama kamu {:<10} Ayu".format(nama))
print("Nama kamu {:>10} Ayu".format(nama))
print("Nama kamu {:^10} Ayu".format(nama))

print()
phi = 3.14159265358979323846
print("Phi adalah {:.2f}".format(phi))      # Mengambil dua digit dibelakang koma

print()
angka = 12000
print("Angka adalah {:,}".format(angka))    # Memberikan koma setiap kelipatan 3
print("Angka adalah {:b}".format(angka))    # Mengubah menjadi angka biner
print("Angka adalah {:o}".format(angka))    # Mengubah menjadi angka octal
print("Angka adalah {:X}".format(angka))    # Mengubah menjadi angka heksadesimal
print("Angka adalah {:E}".format(angka))    # Mengubah menjadi angka scientific