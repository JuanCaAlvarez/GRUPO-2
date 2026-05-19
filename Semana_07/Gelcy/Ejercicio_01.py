#Pide al usuario su nombre y muestra: 'Hola, [NOMBRE]! Bienvenido al curso.'
#El nombre debe aparecer en MAYÚSCULAS.

#Pedimos al usuario que ingrese su nombre
texto = input("Ingrese su nombre: ")

#Con la función UPPER, el texto ingresado en minusculas se mostrará en MAYÚSCULAS
print("Hola", texto.upper(), "¡Bienvenido al curso!")