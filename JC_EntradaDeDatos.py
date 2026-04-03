# input() siempre devuelve str
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# Convertir a número
edad = int(input("¿Cuántos años tienes? "))
nota = float(input("Ingresa tu nota: "))

# Ejemplo completo
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
suma = n1 + n2
print(f"Suma = {suma:.2f}")