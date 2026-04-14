# Solicitar dos números al usuario
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Comparar los números
if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Ambos números son iguales")