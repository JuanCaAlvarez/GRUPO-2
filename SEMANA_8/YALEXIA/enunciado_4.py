# crear lista de diccionario
estudiantes =  [
    {"nombre": "Andrea", "carrera": "ingenieria", "promedio": 16},   # Estudiante 1
    {"nombre": "Carlos", "carrera": "derecho", "promedio": 14},      # Estudiante 2
    {"nombre": "Maria", "carrera": "medicina", "promedio": 17},      # Estudiante 3
    {"nombre": "Ana", "carrera": "contabilidad", "promedio": 15}     # Estudiante 4
]
  
# imprimir nombre y promedio de cada estudiante
for estudiante in estudiantes:
    print(estudiante['nombre'], '->', estudiante['promedio'])  # Imprimimos el nombre y el promedio de cada estudiante

# encontrar el estudiante con el promedio mas alto

mejor = estudiantes[0]     # Guardamos el primer estudiante como el mejor inicialmente

# Recorremos nuevamente la lista para encontrar el mayor promedio
for estudiante in estudiantes:      # Recorremos cada estudiante de la lista
    if estudiante["promedio"] > mejor["promedio"]:    # Comparamos si el promedio actual es mayor que el mejor
        mejor = estudiante             # Si es mayor, actualizamos y guardamos este estudiante como el nuevo mejor
        
print("\nEstudiante con el promedio mas alto: ")      # Mostramos un mensaje indicando el mejor estudiante
print(f"{mejor['nombre']} con promedio {mejor['promedio']}")  # Imprimimos el nombre y promedio del mejor estudiante
