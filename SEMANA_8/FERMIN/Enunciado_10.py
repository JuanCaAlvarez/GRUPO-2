<<<<<<< HEAD
import re  # Librería para buscar palabras con expresiones regulares

texto = input("Ingrese un párrafo: ").lower()

# Extrae palabras formadas por letras y apóstrofes
palabras = re.findall(r"[a-záéíóúñü]+(?:'[a-záéíóúñü]+)*", texto)

frecuencia = {}  # Diccionario para contar palabras

# Contamos cuántas veces aparece cada palabra
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Ordenamos por mayor frecuencia y luego alfabéticamente
ordenadas = sorted(frecuencia.items(), key=lambda x: (-x[1], x[0]))

# Palabras que aparecen una sola vez
unicas = sorted([p for p, cantidad in frecuencia.items() if cantidad == 1])

print("\nTOP 5 PALABRAS:")
for palabra, cantidad in ordenadas[:5]:
    print(palabra, ":", cantidad)

print("\nPALABRAS ÚNICAS:")
=======
import re  # Librería para buscar palabras con expresiones regulares

texto = input("Ingrese un párrafo: ").lower()

# Extrae palabras formadas por letras y apóstrofes
palabras = re.findall(r"[a-záéíóúñü]+(?:'[a-záéíóúñü]+)*", texto)

frecuencia = {}  # Diccionario para contar palabras

# Contamos cuántas veces aparece cada palabra
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Ordenamos por mayor frecuencia y luego alfabéticamente
ordenadas = sorted(frecuencia.items(), key=lambda x: (-x[1], x[0]))

# Palabras que aparecen una sola vez
unicas = sorted([p for p, cantidad in frecuencia.items() if cantidad == 1])

print("\nTOP 5 PALABRAS:")
for palabra, cantidad in ordenadas[:5]:
    print(palabra, ":", cantidad)

print("\nPALABRAS ÚNICAS:")
>>>>>>> 7edf3ee7fd75c3d00f204393b163b1a8c5240f33
print(unicas)