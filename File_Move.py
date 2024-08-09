# File Move
import os
source = "C:\\Users\\ASUS\\Documents\\tes_file_py_copy.txt"
destinasi = "C:\\Users\\ASUS\\Desktop\\file_move.txt"

try:
    if os.path.exists(destinasi):
        print("File sudah ada")
    else:
        os.replace(source, destinasi)
        print("File berhasil dipindahkan ke destinasi")
except FileNotFoundError:
    print("(Error) File tidak ditemukan")