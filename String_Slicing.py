# String Slicing
# Slicing = indexing[] atau slice()
#           [start : stop : step]
nama_panjang = "Damai Raya Fakhruddin"
nama_depan = nama_panjang[0:5]          # Mencetak dari indeks 0 sampai sebelum 5
nama_tengah = nama_panjang[6:10]        # Mencetak dari indeks 6 sampai sebelum 10
nama_belakang = nama_panjang[11:21]     # Mencetak dari indeks 11 sampai sebelum 21
nama_lengkap = nama_panjang[0:21]       # Mencetak dari indeks 0 sampai sebelum 21
nama_acak = nama_panjang[::2]           # Mencetak dari nama panjang tetapi tiap kelipatan indeks ke 2
reversed_nama = nama_panjang[::-2]      # Mencetak kebalikan dari nama panjang tiap kelipatan indeks ke 2

print(nama_depan, nama_tengah, nama_belakang)
print(nama_lengkap)
print(nama_acak)
print(reversed_nama)

website1 = "http://google.com"
website2 = "http://tokopedia.com"
slice = slice(7,-4)                 # Mengambil dari indeks ke 7 dari depan dan indeks ke 4 dari belakang

print(website1[slice])
print(website2[slice])

print()