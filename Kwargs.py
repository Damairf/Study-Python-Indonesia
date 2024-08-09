# Kwargs
def nama(**Kwargs):
    print("Halo",end=" ")
    for key,value in Kwargs.items():
        print(value,end=" ")

nama(awal = "Damai", Tengah = "Raya", Akhir = "Fakhruddin")