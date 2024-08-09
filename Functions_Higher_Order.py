# Higher Order Function
# 1. Dapat menerima function sebagai argumen
# 2. return function

def keras(suara):
    return suara.upper()

def kecil(suara):
    return suara.lower()

def salam(func):
    suara = func("Halo")
    print(suara)
    
salam(keras)
salam(kecil)

print()
def pembagi(x):
    def dibagi(y):
        return y / x
    return dibagi

angka1 = pembagi(2)
print(angka1(10))