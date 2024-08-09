# 2D Lists
makanan = ["Pizza", "Burger", "Hotdog"]
minuman = ["Soda", "Kopi", "Teh"]
dessert = ["Donut", "Brownis", "Cake"]

menu = [makanan, minuman, dessert]

while True:
    pilihan1 = int(input("Masukkan angka pertama 0/1/2 : "))
    if pilihan1 > 2 or pilihan1 < 0:
        print("Pilih antara 0, 1, 2")
    else:
        break
   
while True: 
    pilihan2 = int(input("Masukkan angka pertama 0/1/2 : "))
    if pilihan2 > 2 or pilihan2 < 0:
        print("Pilih antara 0, 1, 2")
    else:
        break
    
print("Menu kamu",menu[pilihan1][pilihan2])