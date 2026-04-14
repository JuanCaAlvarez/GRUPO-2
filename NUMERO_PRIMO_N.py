import math
N = int(input("Ingresa un número N: "))
print(f"Números primos desde 2 hasta {N}:")

for num in range(2, N + 1):
    es_primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(num)