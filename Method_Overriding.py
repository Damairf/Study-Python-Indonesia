# Method Overriding
class Hewan:
    def makan(self):
        print("Hewan ini sedang makan")
        
class Kucing(Hewan):
    def makan(self):
        print("Kucing ini sedang makan")
        
kucing = Kucing()
kucing.makan()