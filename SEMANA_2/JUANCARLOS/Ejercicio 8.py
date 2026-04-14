import random

numero_secreto = random.randint(1, 100)
intentos = 0
intento_usuario = 0

print("Adivina el número entre 1 y 100")

while intento_usuario != numero_secreto:
    intento_usuario = int(input("Tu numero: "))
    intentos = intentos + 1
    
    if intento_usuario < numero_secreto:
        print("Es mayor")
    elif intento_usuario > numero_secreto:
        print("Es menor")
    else:
        print("Ganaste! Te tomo", intentos, "intentos")