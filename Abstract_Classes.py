# Abstract  Class
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Mobil(Kendaraan):
    def go(self):
        print("Mobil ini sedang berjalan")
    
    def stop(self):
        print("Mobil ini sedang berhenti")
        
class Motor(Kendaraan):
    def go(self):
        print("Motor ini sedang berjalan")
        
    def stop(self):
        print("Motor ini sedang berhenti")
        
motor = Motor()
mobil = Mobil()

mobil.go()
mobil.stop()
motor.go()
motor.stop()