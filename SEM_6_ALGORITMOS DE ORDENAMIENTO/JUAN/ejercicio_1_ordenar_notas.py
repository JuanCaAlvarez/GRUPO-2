notas = [85, 42, 93, 67, 28, 75]

def bubble_sort(lista_original):
    lista = lista_original.copy()
    n = len(lista)
    for i in range(n):
        for j in range (0, n-i-1):
            if lista [j] > lista [j + 1 ]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista_original):
    lista = lista_original.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range (i + 1,n):
            if lista[j] < lista [min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

print ("ORDENAR NOTAS")
print(f"Lista original: {notas}")

notas_bubble = bubble_sort(notas)
print(f"\na) Ordenado con Bubble sort: {notas_bubble}")

notas_selection = selection_sort(notas)
print(f"b) Ordenado con Selection sort: {notas_selection}")

nota_minima = min(notas)
nota_maxima = max(notas)
promedio = sum(notas) / len(notas)

print(f" -Nota minima: {nota_minima}")
print(f" -Nota maxima: {nota_maxima}")
print(f" -Promedio: {promedio:.2f}")
