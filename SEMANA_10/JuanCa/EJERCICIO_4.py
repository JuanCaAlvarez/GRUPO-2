
import copy  # Importamos el módulo copy para gestionar cómo se duplican los objetos en memoria


def duplicar_notas(lista_original):
    # Usamos copy.deepcopy() porque nuestra lista contiene diccionarios (objetos mutables dentro de otro mutable).
    # Si solo usáramos copy.copy() o =, modificar la copia afectaría a la original. Deepcopy crea entidades totalmente independientes.
    resultado = copy.deepcopy(lista_original)
    
    for item in resultado:  # Iteramos sobre la NUEVA lista
        item["nota"] *= 1.5  # Multiplicamos la nota por 1.5 y sobreescribimos el valor
        
    return resultado  # Retornamos la lista modificada

# Definimos nuestra data original
original = [{"nombre": "Ana", "nota": 10}, {"nombre": "Luis", "nota": 12}]

# Ejecutamos la función y guardamos el retorno en una nueva variable
nueva = duplicar_notas(original)

# id() nos devuelve la dirección de memoria. Aquí comprobamos que apuntan a lugares distintos en la RAM.
print(f"ID original: {id(original)} | ID nueva: {id(nueva)}")

# Demostramos que la mutación solo afectó a la copia, manteniendo la original intacta (concepto de inmutabilidad externa)
print(f"Nota original Ana: {original[0]['nota']}") # Output: 10
print(f"Nota calculada Ana: {nueva[0]['nota']}")   # Output: 15.0