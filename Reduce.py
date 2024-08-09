# Reduce
# Mengambil 2 value secara terus menerus sampai akhirnya hanya menjadi 1 value yang tergabung
# reduce(function, iterasi)

import functools

kata = ("K", "E", "N", "D", "A", "L")
teks = functools.reduce(lambda x, y: x + y, kata)
print(teks)
# Akan menjumlahkan 2 value secara urut sampai menjadi 1 value dari beberapa value awal yang dijumlahkan
# contoh: K + E = KE, KE + N = KEN, KEN + ...

print()

factorial = (7, 6, 5, 4, 3, 2, 1)
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
# Akan melakukan perkalian tiap 2 value secara urut dan menghasilkan 1 value total dari perkalian beberapa value
# contoh: 7 * 6 = 42, 42 * 5 = 210, 210 * 4 = ...