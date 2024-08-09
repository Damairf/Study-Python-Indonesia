# Delete File
import os
import shutil

jalur = "C:\\Users\\ASUS\\Desktop\\file_move.txt"

try:
    if os.path.isfile(jalur):
        os.remove(jalur)
        print("Anda berhasil menghapus file")
    elif os.path.isdir():
        shutil.rmtree(jalur)
        print("Anda berhasil menghapus folder beserta isinya")
except FileNotFoundError:
    print("File tidak ditemukan")
except PermissionError:
    print("Anda tidak punya permisi")