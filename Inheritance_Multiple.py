# Inheritance Multiple
class Herbivora:
    def sayur(self):
        print("Hewan ini memakan sayuran")
        
class Karnivora:
    def daging(self):
        print("Hewan ini memakan daging")
        
class Sapi(Herbivora):
    pass
class Singa(Karnivora):
    pass

sapi = Sapi()
singa = Singa()

sapi.sayur()
singa.daging()