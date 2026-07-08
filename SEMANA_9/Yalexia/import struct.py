import struct  # Importa el módulo struct para trabajar con datos binarios

numeros = (1, 2, 3, 4, 5)    # Define una tupla de números enteros

# Escribir
with open("numeros.bin", "wb") as f:     # Abre (o crea) el archivo en modo escritura binaria
    f.write(struct.pack("5i", *numeros)) # Convierte los 5 enteros a formato binario y los escribe en el archivo 

# Leer
with open("numeros.bin", "rb") as f:       # Abre el archivo en modo lectura binaria 
    datos = struct.unpack("5i", f.read())  # Lee el contenido binario y lo convierte nuevamente en 5 enteros

print("Original:", numeros)   # Muestra la tupla original
print("Leído:", datos)        # Muestra los datos leídos desde el archivo binario
