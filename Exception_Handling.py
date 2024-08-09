# Exception Handling
try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    result = angka1 / angka2
except ZeroDivisionError as e:
    print(e)
    print("Tidak bisa membagi angka dengan 0")
except ValueError as e:
    print(e)
    print("Masukkan angka bukan huruf")
except Exception as e:
    print(e)
    print("Terjadi kesalahan")
else:
    print(result)
finally:
    print("Perintah ini akan selalu berjalan")