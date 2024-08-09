# Function To Variables
def Hello():
    print("Halo kapten")
    
Hi = Hello
print(Hi)       # Akan mencetak memory addres di komputer
print(Hello)    # Akan mencetak memory addres di komputer

print()
cetak = print
cetak("Halo halo bando")