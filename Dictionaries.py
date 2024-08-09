# Dictionaries
menu = {'Paket 1':'Nasi + Ayam + Es Teh', 
        'Paket 2':'Nasi Goreng + Es Teh', 
        'Paket 3':'Steak Ayam + Es Teh', 
        'Paket 4':'Mie Goreng + Es teh'}

menu.update({'Paket 5':'Bakso + Es Teh'})
# menu.pop('Paket 3')           # Menghapus data tertentu pada array
# menu.clear()                  # Menghapus semua data pada array

print(menu['Paket 1'])
print()
print(menu.get('Paket 7'))      # Mengambil dan mengecek apakah terdapat indeks
print()
print(menu.keys())              # Menampilkan semua key
print()
print(menu.values())            # Menampilkan semua value
print()
print(menu.items())             # Menampilkan semua item yang tersedia pada array
print()

for key, value in menu.items():
    print(key, value)