# Lambda
# Lambda ditulis 1 baris, bisa menerima berbagai angka dan argumen, tetapi hanya berlaku 1 perintah
double = lambda x: x * 2
perkalian = lambda x, y: x * y
penjumlahan = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
cek_umur = lambda umur: True if umur >= 18 else False

print(double(4))
print(perkalian(7, 5))
print(penjumlahan(1, 2, 3))
print(full_name("Damai", "Raya"))
print(cek_umur(19))