#EJERCICIO 06: Combinación de Arreglos y Ordenamiento. Tienes dos arreglos paralelos: productos (strings) y ventas (enteros). Combínalos 
#en una lista de diccionarios, luego: 1. Ordena por ventas de mayor a menor. 2. Imprime el ranking con posición (1°, 2°, etc.). 3. Calcula 
#el promedio de ventas e indica cuáles están sobre la media

#Arreglos paralelos
productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Tablet"]
ventas = [30, 10, 15, 20, 25]

#Combinar en lista de diccionarios
lista_productos = []

for i in range(len(productos)): 
    diccionario = {
        "producto": productos[i],
        "ventas": ventas[i]
    }
    lista_productos.append(diccionario)

#Ordenar por ventas de mayor a menor
lista_productos.sort(key=lambda x: x["ventas"], reverse=True) #REVERSE=TRUE: Invierte el orden

#Mostrar ranking
print("RANKING DE VENTAS")

#Bucle para crear el ranking de ventas
for i in range(len(lista_productos)):
    print(f"{i+1}° {lista_productos[i]['producto']} - {lista_productos[i]['ventas']} ventas")

#Creamos un acumulador
suma = 0

#Sumamos las ventas de cada producto 
for producto in lista_productos:
    suma += producto["ventas"]

#Calculamos el promedio
promedio = suma / len(lista_productos)

print("\nPromedio de ventas:", promedio)

#Mostrar productos sobre la media
print("\nProductos sobre la media:")

#Mostramos los productos que tienen una venta mayor al promedio
for producto in lista_productos:
    if producto["ventas"] > promedio:
        print(producto["producto"], "-", producto["ventas"])
