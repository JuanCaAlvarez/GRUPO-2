# Lista de nombres de los estudiantes
nombres = ["Carlos", "Juan", "Maria", "Carla"]

# Diccionario donde cada materia tiene una lista de notas
materias = {
    "Comunicación": [15, 14, 18, 12],    # notas de comunicación
    "Matemática": [20, 16, 15, 18],      # notas de matemática
    "Ciencia": [14, 19, 13, 11],         # notas de ciencia
    "Historia": [19, 12, 15, 18]         # notas de historia
}
# Función que calcula el promedio de una lista de números
def promedio(lista):
    return sum(lista) / len(lista)   # suma los valores y divide entre la cantidad

# imprime el título de promedios por materia
print("Promedios por materia:") 

# recorre cada materia y sus notas 
for materia, notas in materias.items():
    # muestra el nombre de la materia y su promedio con 2 decimales
    print(f"{materia}: {promedio(notas):.2f}")

# imprime el titulo de mejor estudiante por materia
print("\nMejor estudiante por materia:")   

# recorre cada materia y sus notas
for materia, notas in materias.items():
    max_nota = max(notas)    # obtiene la nota mas alta de la lista
    indice = notas.index(max_nota)  # busca la posición de esa nota
    # muestra el nombre del estudiante con mejor nota
    print(f"{materia}: {nombres[indice]} con {max_nota}")

# lista vacía donde se guardarán los promedios generales
promedios_generales = []

# recorre cada estudiante usando su indice
for i in range(len(nombres)):
    suma = 0     # variable para acumular las notas del estudiante

    # recorre las listas de notas de cada materia
    for notas in materias.values():
        suma += notas[i]    # suma la nota del estudiante en esa materia

    prom = suma / len(materias)     # calcula el promedio general del estudiante

    # guarda una tupla (nombre, promedio)
    promedios_generales.append((nombres[i], prom))

# usa lambda para tomar el promedio (posición 1 de la tupla) y ordenar de mayor a menor
resultado = sorted(promedios_generales, key=lambda x: x[1], reverse=True)

# imprime el titulo del Ranking general
print("\nRanking general:")

# recorre la lista ordenada
for nombre, prom in resultado:
    # muestra el nombre y su promedio con 2 decimales
    print(f"{nombre}: { prom:.2f}")
