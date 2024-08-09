# Inheritance
class Hewan:
    hidup = True
    
    def makan(self):
        print("Hewan ini sedang makan")
    def tidur(self):
        print("Hewan ini sedang tidur")
        
class Kucing(Hewan):
    def meow(self):
        print("Kucing meow meow")
class Anjing(Hewan):
    def guk(self):
        print("Anjing guk guk")
        
kucing = Kucing()
anjing = Anjing()

print(kucing.hidup)
kucing.makan()
kucing.meow()
anjing.tidur()
anjing.guk()