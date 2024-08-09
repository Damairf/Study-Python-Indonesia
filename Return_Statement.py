# Return Statement
def angka(angka1, angka2):
    result = angka1 * angka2
    return result

jawaban1 = int(input("Masukkan angka pertama: "))
jawaban2 = int(input("Masukkan angka kedua: "))

print("Hasil perkalian dari", jawaban1, "dan", jawaban2, "adalah", angka(jawaban1,jawaban2))