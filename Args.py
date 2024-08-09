# Args
def angka(*Args):
    sum = 0
    Args = list(Args)
    Args[0] = 0
    for i in Args:
        sum += i
    return sum

print(angka(1,2,3,4,5,6))