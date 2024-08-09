# Sets
# Sets terdiri dari beberapa indeks yang disimpan secara acak dan tidak dapat berisi duplikat
hewan = {"Ayam", "Bebek", "Sapi", "Kambing"}
bunga = {"Melati", "Matahari", "Anggrek", "Mawar", "Kambing"}

# hewan.add("Badak")                # Menambah data pada sets
# hewan.remove("Ayam")              # Menghapus data tertentu pada sets
# hewan.update(bunga)               # Memperbarui supaya sets hewan ditambah dengan sets bunga
# hewan.clear()                     # Menghapus semua data pada sets hewan

print(bunga.difference(hewan))      # Mencetak perbedaan apa yang tidak dimiliki hewan pada bunga
print(hewan.intersection(bunga))    # Mencetak apa saja yang sama diantara kedua sets
print()

alam = hewan.union(bunga)           # Menggabungkan sets hewan dan bunga menjadi 1 variabel

for x in alam:
    print(x)