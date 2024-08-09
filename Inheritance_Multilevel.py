# Inheritance Multilevel
class Organisme:
    hidup = True
    
class Hewan(Organisme):
    def makan(self):
        print("Hewan ini sedang makan")
        
class Kucing(Hewan):
    def meow(self):
        print("Kucing meow meow")
        
kucing = Kucing()
print(kucing.hidup)
kucing.makan()
kucing.meow()