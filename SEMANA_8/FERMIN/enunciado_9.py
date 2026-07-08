<<<<<<< HEAD
import re  # Permite buscar palabras usando expresiones regulares

def buscador(catalogo, query):
    resultados = []  # Aquí se guardan los libros encontrados

    for libro in catalogo:  # Recorremos cada libro
        puntos = 0

        # Si la búsqueda está en el título, vale 2 puntos
        if re.search(query, libro["titulo"], re.I):
            puntos += 2

        # Si la búsqueda está en el autor, vale 1 punto
        if re.search(query, libro["autor"], re.I):
            puntos += 1

        # Solo guardamos libros que coinciden
        if puntos > 0:
            resultados.append((puntos, libro))

    # Ordena por mayor puntaje y luego por año
    return sorted(resultados, key=lambda x: (-x[0], x[1]["año"]))


# Lista de libros
catalogo = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García", "año": 1967},
    {"titulo": "Cien sonetos de amor", "autor": "Pablo Neruda", "año": 1959},
    {"titulo": "El amor eterno", "autor": "Gabriel García", "año": 1985}
]

# Búsqueda del usuario
query = input("Buscar: ")

# Mostrar resultados
for puntos, libro in buscador(catalogo, query):
=======
import re  # Permite buscar palabras usando expresiones regulares

def buscador(catalogo, query):
    resultados = []  # Aquí se guardan los libros encontrados

    for libro in catalogo:  # Recorremos cada libro
        puntos = 0

        # Si la búsqueda está en el título, vale 2 puntos
        if re.search(query, libro["titulo"], re.I):
            puntos += 2

        # Si la búsqueda está en el autor, vale 1 punto
        if re.search(query, libro["autor"], re.I):
            puntos += 1

        # Solo guardamos libros que coinciden
        if puntos > 0:
            resultados.append((puntos, libro))

    # Ordena por mayor puntaje y luego por año
    return sorted(resultados, key=lambda x: (-x[0], x[1]["año"]))


# Lista de libros
catalogo = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García", "año": 1967},
    {"titulo": "Cien sonetos de amor", "autor": "Pablo Neruda", "año": 1959},
    {"titulo": "El amor eterno", "autor": "Gabriel García", "año": 1985}
]

# Búsqueda del usuario
query = input("Buscar: ")

# Mostrar resultados
for puntos, libro in buscador(catalogo, query):
>>>>>>> 7edf3ee7fd75c3d00f204393b163b1a8c5240f33
    print(libro["titulo"], "-", puntos, "puntos")