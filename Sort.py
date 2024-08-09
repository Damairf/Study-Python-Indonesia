# Sort
# sort() method = digunakan dengan list
# sotr() function = digunakan dengan iterasi

siswa = ['Bambang', 'Agus', 'Xaviera', 'Mahmud', 'Budi']
siswa.sort()
# siswa.sort(reverse=True)      # mengurutkan dari paling belakang

for i in siswa:
    print(i)
print()

peserta = [('Justin', 'B', 82),
           ('Baba', 'C', 70),
           ('Alex', 'B', 85),
           ('Pasha', 'A', 92),
           ('Salwa', 'F', 63)]

skor = lambda skors: skors[1]
poin = lambda poins: poins[2]
peserta.sort(key=poin, reverse=True)

for i in peserta:
    print(i)
print()    

karyawan = ('Miftah', 'Azriel', 'Rahmat', 'Gogo', 'Susi')
sorted_karyawan = sorted(karyawan, reverse=True)

for i in sorted_karyawan:
    print(i)
print()

gaji = (('Samuel', 5000000),
        ('Edward', 3500000),
        ('Stan', 7300000),
        ('Amel', 4000000),
        ('Kris', 9000000))

nomimal = lambda gajix: gajix[1]
gaji_sorted = sorted(gaji, key=nomimal)

for i in gaji_sorted:
    print(i)