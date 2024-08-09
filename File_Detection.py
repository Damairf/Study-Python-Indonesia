# File Detection
import os
jalur = "C:\\Users\\ASUS\\Documents\\tes_file_py.txt"

if os.path.exists(jalur):
    print("Lokasi ada")
    if os.path.isfile(jalur):
        print("Ini adalah file")
    elif os.path.isdir(jalur):
        print("Ini adalah folder")
else:
    print("Lokasi tidak ada")