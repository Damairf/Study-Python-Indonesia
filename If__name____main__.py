# If __name__ = __main__
# 1. Modul dapat dijalankan sendiri
# 2. Modul dapat diimpor dan digunakan pada modul lain

def halo():
    print("Hello World")
    
if __name__ == '__main__':
    halo()