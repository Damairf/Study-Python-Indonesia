# Duck Typing
# Perintah akan tetap dijalankan meskipun mengambil class yang salah jika class tersebut memiliki
# method yang sama dengan class yang seharusnya diambil.

class Duck:
    def jalan(self):
        print("Bebek berjalan")
    
    def suara(self):
        print("Bebek kwek kwek")
        
class Chicken:
    def jalan(self):
        print("Ayam berjalan")
        
    def suara(self):
        print("Ayam berkokok")
        
class Cow:
    def suara(self):
        print("Sapi moo moo")
        
class Person:
    def tangkap(self, duck):
        duck.jalan()
        duck.suara()
        print("Bebek berhasil ditangkap")
        
duck = Duck()
chicken = Chicken()
cow = Cow()
person = Person()

person.tangkap(chicken)