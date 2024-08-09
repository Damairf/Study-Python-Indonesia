# Map
# Dapat digunakan untuk setiap iterasi pada tuples(), list[], dll
# map(function, iterasi)

toko = [("Baju", 15.50),
        ("Celana", 10.40),
        ("Topi", 5.00),
        ("Jaket", 30.00)]

to_rupiah = lambda data: (data[0], data[1]*16000)

toko_rupiah = list(map(to_rupiah, toko))

for i in toko_rupiah:
    print(i)
print()    

makanan = [("Burger", 20000),
           ("Hotdog", 18000),
           ("Kentang", 10000),
           ("Es Krim", 12000)]

to_diskon = lambda diskon: (diskon[0], diskon[1]*(75/100))
makanan_diskon = list(map(to_diskon, makanan))

for i in makanan_diskon:
    print(i)