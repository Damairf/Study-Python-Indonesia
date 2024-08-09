# File Write
teks = input("Masukkan teks yang ingin dimasukkan ke file: ")

with open("C:\\Users\\ASUS\\Documents\\tes_file_py.txt", "a") as file:
    file.write(teks)
    print("Berhasil menambahkan teks")