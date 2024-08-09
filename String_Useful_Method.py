# Useful String Method
buah = "pisang_goreng"
print(len(buah))                # Menghitung berapa jumlah huruf dalam kalimat
print(buah.find("p"))           # Mencari huruf yang diinginkan berada pada indeks keberapa
print(buah.capitalize())        # Membuat kalimat memiliki huruf kapital depan
print(buah.upper())             # Membuat semua huruf menjadi kapital
print(buah.lower())             # Membuat semua huruf menjadi kecil / tidak kapital
print(buah.isdigit())           # Memeriksa apakah variabel sebuah integer, jika iya maka True / jika tidak maka False
print(buah.isalpha())           # Memeriksa apakah variabel mengandung spasi atau tidak, jika tidak maka True / jika iya maka False
print(buah.count("g"))          # Memeriksa ada berapa huruf yang dicari dalam kalimat
print(buah.replace("i","e"))    # Mengganti huruf spesifik dengan huruf yang diberikan
print(buah*3)                   # Menampilkan kalimat sesuai dengan jumlah yang diberikan

teks = input("Masukkan kalimat anda: ")
cari = input("Cari huruf yang ingin diganti: ")
ganti = input("Ganti huruf dengan: ")

print("Teks awal: "+teks+"\nHuruf diganti: "+cari+"\nHuruf pengganti: "+ganti+"\nTeks akhir: "+teks.replace(cari, ganti))