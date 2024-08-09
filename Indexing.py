# Indexing
nama = "damai Raya"

# if nama[0].islower():
#     nama = nama.capitalize()      # Jika nama awal masih belum kapital, maka akan otomatis membuat kapital
# print(nama)

nama_awal = nama[0:5].upper()       # Mengambil nama dari indeks 0 sampai sebelum 5 dan membuatnya menjadi upper semua
nama_akhir = nama[6:].lower()       # Mengambil nama dari indeks 6 sampai akhir dan membuatnya menjadi lower semua
huruf_akhir = nama[-1]              # Mengambil nama dari indeks -1 atau 1 dari terakhir

print(nama_awal, nama_akhir, huruf_akhir)