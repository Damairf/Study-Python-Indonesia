# List Comprehensions
# list = [ekspresi for untuk item pada setiap iterasi]

kubik = [i * i for i in range(1,11)]
print(kubik)
print()

nilai = [100, 90, 95, 80, 75, 70, 60, 55, 65, 69]
lulus = list(filter(lambda kkm: kkm>=70, nilai))
gagal = [i if i >= 70 else "Gagal" for i in nilai]
print(lulus)
print(gagal)