# File Read
try:
    with open("C:\\Users\\ASUS\\Documents\\tes_file_py.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("(Error) File tidak ditemukan ")