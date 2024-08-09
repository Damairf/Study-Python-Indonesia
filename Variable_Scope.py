# Variable Scope
nama = "Damai"      # Global Scope = dapat diakses dalam dan luar function

def namaTengah():
    nama = "Raya"   # Local Scope = hanya dapat diakses dalam function
    print(nama)
    
namaTengah()
print(nama)