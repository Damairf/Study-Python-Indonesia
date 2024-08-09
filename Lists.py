# Lists
makanan = ["Sate", "Bakwan", "Bakso", "Kebab", "Burger"]
makanan[0] = "Hotdog"

# makanan.append("Pizza")           # Menambahkan list pada array
# makanan.remove("Bakwan")          # Membuang list tertentu
# makanan.pop()                     # Membuang list terakhir pada array
# makanan.insert(2, "Martabak")     # Menambah list pada array indeks tertentu
# makanan.sort()                    # Mengurutkan list
# makanan.clear()                   # Menghapus semua indeks yang ada pada list

for x in makanan:
    print(x)
print()

kelas = []
while True:
    nama = input("Masukkan nama: ").capitalize()
    kelas.append(nama)
    while True:
        pilihan = input("Apakah ingin memasukkan nama lagi? [Y/N]\n").capitalize()
        if pilihan == "Y":
            print()
            print("Silahkan masukkan nama lagi")
            break
        elif pilihan == "N":
            break
        else:
            print()
            print("Silahkan masukkan Y/N")
    if pilihan == "N":
        break
    else:
        pass
print()
print("Nama siswa: ", end="")
for i in kelas:
    print(i,"",end="")