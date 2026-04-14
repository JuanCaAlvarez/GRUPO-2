
n = int(input("Ingresa un número: "))
print(f"\nTabla de multiplicar del {n}:")

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")