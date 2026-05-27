# Lista de nombres de los estudiantes
nombres = ["Ana", "Luis", "Carlos", "María"]

# Diccionario donde cada materia tiene una lista de notas
materias = {
    "Matemática": [15, 18, 14, 17],      # Notas de Matemática
    "Comunicación": [16, 17, 15, 18],    # Notas de Comunicación
    "Historia": [14, 16, 13, 17]         # Notas de Historia
}

# Función que calcula el promedio de una lista de números
def promedio(lista):
    return sum(lista) / len(lista)  # Suma los valores y divide entre la cantidad

# Imprime el título de promedios por materia
print("Promedios por materia:")

# Recorre cada materia y sus notas
for materia, notas in materias.items():
    # Muestra el nombre de la materia y su promedio con 2 decimales
    print(f"{materia}: {promedio(notas):.2f}")

# Imprime el título de mejor estudiante por materia
print("\nMejor estudiante por materia:")

# Recorre cada materia y sus notas
for materia, notas in materias.items():
    max_nota = max(notas)  # Obtiene la nota más alta de la lista
    indice = notas.index(max_nota)  # Busca la posición de esa nota
    # Muestra el nombre del estudiante con mejor nota
    print(f"{materia}: {nombres[indice]} con {max_nota}")

# Lista vacía donde se guardarán los promedios generales
promedios_generales = []

# Recorre cada estudiante usando su índice
for i in range(len(nombres)):
    suma = 0  # Variable para acumular las notas del estudiante
    
    # Recorre las listas de notas de cada materia
    for notas in materias.values():
        suma += notas[i]  # Suma la nota del estudiante en esa materia
    
    prom = suma / len(materias)  # Calcula el promedio general del estudiante
    
    # Guarda una tupla (nombre, promedio)
    promedios_generales.append((nombres[i], prom))

# Función que devuelve el promedio (posición 1 de la tupla)
def obtener_promedio(x):
    return x[1]  # Devuelve el segundo valor (promedio)

# Ordena la lista de mayor a menor usando el promedio
resultado = sorted(promedios_generales, key=obtener_promedio, reverse=True)

# Imprime el título del ranking general
print("\nRanking general:")

# Recorre la lista ordenada
for nombre, prom in resultado:
    # Muestra el nombre y su promedio con 2 decimales
    print(f"{nombre}: {prom:.2f}")