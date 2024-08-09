# If Statement
umur = int(input("Berapa usia anda: "))
if umur <= 0:
    print("Kamu belum lahir")
elif umur <= 18:
    print("Kamu anak-anak")
elif umur <= 26:
    print("Kamu remaja")
elif umur <= 40:
    print("Kamu dewasa")
elif umur <= 70:
    print("Kamu tua")
elif umur >= 70:
    print("Kamu sepuh")