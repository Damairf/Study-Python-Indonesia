# Logical Operators (and,or,not) = untuk mengecek jika dua atau lebih kondisi bersifat True
suhu = int(input("Berapa suhu diluar: "))
if suhu >= 0 and suhu <= 30:        # Variabel suhu dan suhu
    print("Suhu diluar terlihat normal")
    print("Aman")
elif suhu < 0 or suhu > 30:         # Variabel suhu atau suhu
    print("Suhu diluar sedang tidak normal")
    print("Tidak aman")

tinggi = int(input("Berapa tinggi anda: "))
if not(tinggi >= 160):      # Jika tinggi tidak lebih dari 160 maka
    print("Kamu pendek")
elif not(tinggi <= 160):    # Jika tinggi tidak lebih pendek dari 160 maka
    print("Kamu tinggi")