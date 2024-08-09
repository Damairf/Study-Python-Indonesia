# Dictionary Comprehension
# dictionary = {key: expression for (key, value) in iterasi}
# dictionary = {key: expression for (key, value) in iterasi dengan pengkondisian if}
# dictionary = {key: (if/else) for (key, value) in iterasi}
# dictionary = {key: function(value) for (key, value) in iterasi}

kota_a = {"Semarang": 25, "Jogja": 22, "Solo": 23, "Magelang": 20}
kota_b = {key: round((value-32)*(5/9)) for (key, value) in kota_a.items()}
print(kota_b)
print()

cuaca = {"Kendal": "Cerah", "Temanggung": "Hujan", "Bogor": "Cerah", "Bandung": "Cerah", "Cilacap": "Hujan"}
cuaca_cerah = {key: value for (key, value) in cuaca.items() if value == "Cerah"}
print(cuaca_cerah)
print()

suhu = {"Pati": 35, "Malang": 40, "Jakarta": 38, "Tegal": 33}
suhu_aman = {key: ("Suhu normal" if value <= 35 else "Suhu panas") for (key, value) in suhu.items()}
print(suhu_aman)
print()

def temp(value):
    if value <= 35:
        return "Suhu normal"
    else:
        return "Suhu panas"
    
suhu2 = {"Klaten": 35, "Madura": 40, "Pekalongan": 38, "Brebes": 33}
suhu_aman2 = {key: temp(value) for (key, value) in suhu2.items()}
print(suhu_aman2)