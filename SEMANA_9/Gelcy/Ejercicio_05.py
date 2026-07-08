#Enunciado: Leer 'inventario.txt', calcular el valor total de cada producto (precio * cantidad) y crear
#un nuevo archivo 'reporte_inventario.txt' con los productos ordenados de mayor a menor valor total.

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_INVENTARIO = os.path.join(BASE_DIR, "archivos_practica/inventario.txt")
RUTA_REPORTE = os.path.join(BASE_DIR, "archivos_practica/reporte_inventario.txt")

#Lista vacía donde guardaremos los datos procesados de cada producto
lista_productos = []

#Leer el archivo "inventario.txt"
with open(RUTA_INVENTARIO, "r", encoding="utf-8") as archivo_lectura:
    for linea in archivo_lectura:
        partes = linea.strip().split(",")

        #Validamos que la línea tenga los 4 datos (ID, Nombre, Precio, Cantidad)
        if len(partes) == 4:
            id_prod = partes[0].strip()
            nombre = partes[1].strip()
            precio = float(partes[2].strip())
            cantidad = int(partes[3].strip())

            valor_total = precio * cantidad

            #Guardamos todo en un diccionario temporal para este producto
            producto = {
                "id": id_prod,
                "nombre": nombre,
                "valor_total": valor_total,
            }

            #Agregamos el producto a nuestra lista general (se guarda por REFERENCIA)
            lista_productos.append(producto)

#key=lambda x: x["valor_total"]: Ordena basándose en el valor total.
lista_productos.sort(key=lambda x: x["valor_total"], reverse=True)

#Abrimos el archivo reporte en modo escritura.
with open(RUTA_REPORTE, "w", encoding="utf-8") as archivo_escritura:
    archivo_escritura.write("ID | PRODUCTO | VALOR TOTAL\n")
    archivo_escritura.write("---------------------------------------\n")

    #Recorremos la lista y escribimos de forma directa
    for p in lista_productos:
        # Extraemos los datos normales
        id_prod = p["id"]
        nombre = p["nombre"]
        valor = p["valor_total"]

        archivo_escritura.write(f"{id_prod} | {nombre} | S/ {valor}\n")

print(
    "¡Reporte creado!"
)