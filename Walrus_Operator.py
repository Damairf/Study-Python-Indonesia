# Walrus Operator :=
#print(benar = True)    # Perintah tersebut tidak dapat dijalankan, maka harus menggunakan :=
#print(benar := True)   # Dengan menggunakan := perintah dapat dijalankan

# Operator ini memungkinkan penugasan dan evaluasi ekspresi dalam satu langkah

list_makanan = list()

while makanan := input("Masukkan nama makanan: ") != "exit":
    list_makanan.append(makanan)
    
if (angka := int(input("Masukkan angka: "))) > 10:
    print("Angka lebih besar dari 10")
else:
    print("Angka kurang dari atau sama dengan 10")