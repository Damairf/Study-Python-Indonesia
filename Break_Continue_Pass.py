# Break Continue Pass
while True:
    nama = input("Masukkan nama anda: ")
    if nama != "":
        print("Selamat datang", nama)
        break                           # Break menghentikan pengulangan
print()

nomor = "123-456-789"
for i in (nomor):
    if i == "-":
        continue                        # Continue akan melewati
    print(i, end="")
print()    
print()
for j in range(1,21):
    if j == 13:
        pass                            # Pass akan melompati
    print(j, end="")