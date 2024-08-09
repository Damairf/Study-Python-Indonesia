# For Loops
import time

for i in range(10):             # Akan mencetak 1 - 10
    print(i+1)
print()

for j in range(50,100+1,2):     # Akan mencetak 50 - 100, dengan kelipatan 2
    print(j)
print()

for a in "DAMAI RAYA":          # Akan mencetak teks satu per-satu
    print(a)
print()

for b in range(5):              # Akan mencetak teks sebanyak 5x
    print("PERDAMAIAN")
print()

for i in range(10,1-1,-1):      # Akan mencetak hitung mundur dari 10 - 1,
    print(i)                    # dengan jeda 1 detik tiap mencetak
    time.sleep(1)
print("SELESAI")