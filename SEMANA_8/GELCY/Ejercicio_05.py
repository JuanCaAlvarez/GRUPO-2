#EJERCICIO 05: Búsqueda y Filtrado de Productos. Tienes una lista de diccionarios de productos con 'nombre', 'categoria' y 'precio'. Implementa 
#una función buscar_productos(lista, termino) que devuelva todos los productos cuyo nombre contenga el término de búsqueda (sin importar mayúsculas). 
#Además, ordena los resultados por precio de menor a mayor.

#Diccionario con los productos
productos = [
    {"nombre": "Laptop", "categoria": "Tecnología", "precio": 2500},
    {"nombre": "Mouse", "categoria": "Tecnología", "precio": 100},
    {"nombre": "Laptop Gamer", "categoria": "Tecnología", "precio": 3500},
    {"nombre": "Escritorio", "categoria": "Muebles", "precio": 300},
    {"nombre": "Lapiceros", "categoria": "Útiles", "precio": 5}
]

#Función para buscar los productos
def buscar_productos(lista, termino):
    #Lista para almacenar los resultados
    resultados = []

    #Bucle para buscar coincidencias con el término de búsqueda
    for producto in lista:
        if termino.lower() in producto["nombre"].lower():
            resultados.append(producto) #Añade el resultado a la lista

    #Ordenar por precio
    resultados.sort(key=lambda producto: producto["precio"]) #Lambda: Indica al sort que valor se usa para ordenar. En este caso, PRECIO
    return resultados

#Buscar productos
encontrados = buscar_productos(productos, "top")

#Mostrar resultados
print("Productos encontrados:")

for producto in encontrados:
    print(producto["nombre"], "-", producto["precio"])