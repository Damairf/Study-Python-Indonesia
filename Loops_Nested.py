# Nested Loops
Garis = int(input("Masukkan jumlah garis: "))
Kolom = int(input("Masukkan jumlah kolom: "))
Simbol = input("Masukkan jumlah simbol: ")

for i in range(Garis):
    for j in range(Kolom):
        print(Simbol, end="")
    print()