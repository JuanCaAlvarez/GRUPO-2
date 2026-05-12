notas = [85, 42, 93, 67, 28, 75] #Colocamos la lista -> notas que contiene los datos desordenados

def bubble_sort(lista_original): #Definimos la funcion bubble_sort
    lista = lista_original.copy() #Creamos una copia de la lista para que los calculos no se vean afectados
    n = len(lista) #obtenemos el tamaño de la lista
    for i in range(n): #Controlas cuantas pasadas se va hacer a la lista
        for j in range (0, n-i-1): # compara elementos adyacentes, el -i-1 es para no revisar los elementos que ya cambiaron al final y estan ordenados 
            if lista [j] > lista [j + 1 ]: #cambia de lugar si la izquierda es mayor que el de la derecha, se intercambian 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista_original): #Definimos la funcion selection_sort
    lista = lista_original.copy() #protegemos los datos originales 
    n = len(lista) #obtenemos el tamaño de la lista
    for i in range(n):
        min_idx = i #Se supone que el primer elemento de la lista no ordenada es el mas pequeño
        for j in range (i + 1,n): #Busca por cada vuelta el valor minimo a su posicion definitiva del principio
            if lista[j] < lista [min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

print ("ORDENAR NOTAS")
print(f"Lista original: {notas}") #Imprimimos el encabezado y mostramos como estaban los datos al inicio

notas_bubble = bubble_sort(notas)
print(f"\na) Ordenado con Bubble sort: {notas_bubble}")

notas_selection = selection_sort(notas)
print(f"b) Ordenado con Selection sort: {notas_selection}") #Se llama a las funciones y se guarda los resultados en nuevas variables para imprimirlos de manera independiente

nota_minima = min(notas) #valor minimo
nota_maxima = max(notas) #valos maximo
promedio = sum(notas) / len(notas) # calculas el promedio con la suma de los elementos dividiendo por la cantidad 

print(f" -Nota minima: {nota_minima}") #Mostramos la nota minima
print(f" -Nota maxima: {nota_maxima}") #Mostramos la nota maxima
print(f" -Promedio: {promedio:.2f}") #Mostramos el promedio , se coloca el :.2F para mostrar hasta 2 decimales
