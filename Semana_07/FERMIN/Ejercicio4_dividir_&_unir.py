# Enunciado 4: Dividir y unir palabras
# Este programa trabaja con una cadena de colores separados por comas.
# Luego separa cada color, los convierte a mayúsculas y finalmente los une con una barra vertical.

# Se crea una variable llamada cadena.
# Dentro de ella se guarda un texto con varios colores separados por comas.
cadena = "rojo,verde,azul,amarillo"

# La función split(",") separa la cadena cada vez que encuentra una coma.
# El resultado será una lista con los colores separados.
# Ejemplo: ["rojo", "verde", "azul", "amarillo"]
colores = cadena.split(",")

# Se crea una nueva lista llamada colores_mayuscula.
# Esta línea recorre cada color de la lista colores.
# La función upper() convierte cada palabra a mayúsculas.
# Ejemplo: "rojo" se convierte en "ROJO".
colores_mayuscula = [color.upper() for color in colores]

# La función join() une todos los elementos de la lista en una sola cadena.
# En este caso, los colores se unirán usando el símbolo | como separador.
# Ejemplo: ROJO | VERDE | AZUL | AMARILLO
resultado = " | ".join(colores_mayuscula)

# La función print() muestra en pantalla el resultado final.
print(resultado)