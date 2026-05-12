def par(num):
    return num // 2

def impar(num):
    return num * 3 + 1

num = int(input("Ingrese un número mayor que 1: "))

while num <= 1:
    num = int(input("Error. Ingrese un número mayor que 1: "))

while num != 1:
    if num % 2 == 0:
        num = par(num)
    else:
        num = impar(num)
    print(num)