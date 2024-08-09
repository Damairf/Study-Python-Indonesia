# Method Chaining
class Mobil:
    def nyala(self):
        print("Kamu menyalakan mobil")
        return self
    def maju(self):
        print("Kamu mengendarai mobil")
        return self
    def berhenti(self):
        print("Kamu memberhentikan mobil")
        return self
    def mati(self):
        print("Kamu mematikan mobil")
        return self
    
mobil = Mobil()
mobil.nyala().maju().berhenti().mati()