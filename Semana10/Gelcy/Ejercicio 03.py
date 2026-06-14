#Ejercicio 03:
#Guardar y Cargar JSON. Crea un diccionario que represente un catálogo de productos con al menos 3 ítems (id, nombre, precio, stock).
#Guárdalo en "catalogo.json" con formato legible (indent=2). Vuelve a cargarlo y muestra solo los productos con stock < 20.

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOGO_PRODUCTOS = os.path.join(BASE_DIR, "catalogo.json")

catalogo = {
    "productos": [
        {"id": 1, "nombre": "Laptop", "precio": 2500, "stock": 15},
        {"id": 2, "nombre": "Mouse", "precio": 80, "stock": 30},
        {"id": 3, "nombre": "Teclado", "precio": 150, "stock": 10},
        {"id": 4, "nombre": "Tablet", "precio": 350, "stock": 9},
        {"id": 5, "nombre": "Audífonos", "precio": 60, "stock": 20},
    ]
}

#Guardar el JSON
with open(CATALOGO_PRODUCTOS, "w", encoding="utf-8") as archivo:
    json.dump(catalogo, archivo, indent=2, ensure_ascii=False)

#Cargar el JSON
with open(CATALOGO_PRODUCTOS, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

#Mostrar productos con stock menor a 20
print("=" * 60)
print("Productos con stock menor a 20:")
print("=" * 60)

for producto in datos["productos"]:
    if producto["stock"] < 20:
        print(producto)

print("=" * 60)