import json  # Para leer y escribir el inventario
import csv   # Para leer el reporte de ventas
import os    # Para manejar las rutas dinámicas
 
# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_json = os.path.join(BASE_DIR, "inventario.json")
ruta_csv = os.path.join(BASE_DIR, "ventas.csv")
 
def actualizar_stock():
    # 1. LEER EL INVENTARIO JSON
    with open(ruta_json, "r", encoding="utf-8") as f:
        inventario = json.load(f)  # Convertimos el JSON a un diccionario de Python en memoria
    # 2. LEER LAS VENTAS CSV
    with open(ruta_csv, "r", encoding="utf-8", newline="") as f:
        ventas = csv.DictReader(f)  # Leemos el CSV tratando cada fila como un diccionario
        for venta in ventas:  # Recorremos cada venta registrada
            id_v = int(venta["id_producto"])  # Extraemos el ID y lo convertimos a entero
            cant_v = int(venta["cantidad_vendida"])  # Extraemos la cantidad vendida a entero
            # 3. ACTUALIZAR STOCK EN MEMORIA
            for prod in inventario["productos"]:  # Buscamos el producto en nuestro diccionario
                if prod["id"] == id_v:  # Si los IDs coinciden...
                    nuevo_stock = prod["stock"] - cant_v  # Restamos la venta al stock actual
                    # Operador ternario para asegurar que el stock no sea un número negativo
                    prod["stock"] = nuevo_stock if nuevo_stock >= 0 else 0
 
    # 4. GUARDAR EL INVENTARIO ACTUALIZADO
    with open(ruta_json, "w", encoding="utf-8") as f:
        # Sobreescribimos el archivo JSON original con los nuevos datos actualizados
        json.dump(inventario, f, indent=2, ensure_ascii=False)
 
    # 5. REPORTE FINAL
    print("Inventario actualizado con éxito. Productos agotados (Stock 0):")
    for prod in inventario["productos"]:
        if prod["stock"] == 0:
            print(f"- {prod['nombre']}")
 
 
# ==========================================
# --- ZONA DE PRUEBAS PARA LA EXPOSICIÓN ---
# ==========================================
 
# Esta función crea archivos de prueba automáticamente para que tu código no falle al buscar
def preparar_archivos_prueba():
    # Creamos un inventario ficticio
    inv_prueba = {
        "tienda": "Tech Store",
        "productos": [
            {"id": 1, "nombre": "Laptop HP", "precio": 2500.0, "stock": 10},
            {"id": 2, "nombre": "Mouse Logitech", "precio": 45.0, "stock": 5}
        ]
    }
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(inv_prueba, f, indent=2, ensure_ascii=False)
    # Creamos un archivo de ventas ficticio
    with open(ruta_csv, "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["id_producto", "cantidad_vendida"]) # Cabecera
        escritor.writerow(["1", "2"])  # Se venden 2 Laptops (Quedarán 8)
        escritor.writerow(["2", "5"])  # Se venden 5 Mouses (Quedarán 0, se agotará)
 
# Ejecutamos la preparación y luego nuestro proceso principal
print("Generando archivos de prueba...")
preparar_archivos_prueba()
print("Ejecutando actualización...")
actualizar_stock()