# Random Numbers
import random

angka_acak = random.randint(1,6)
angka = random.random()             # Berisi angka acak diantara 0 - 1
print("Angka acak:",angka_acak)
print("Angka antara 0-1:",angka)

print()
makanan = ["Bakso", "Burger", "Kebab", "Roti"]
pilihmakan = random.choice(makanan)     # Memilih pilihan dari list
print("Makanan acak:",pilihmakan)

print()
kartu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "As"]
random.shuffle(kartu)               # Mengacak pilihan yang diberikan
print("Urutan kartu:",kartu)