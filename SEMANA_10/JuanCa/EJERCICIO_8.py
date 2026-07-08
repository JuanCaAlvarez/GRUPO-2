import copy  # Importamos el módulo copy para poder usar copy() y deepcopy().
import json  # Importamos el módulo json para exportar nuestro reporte final.
import os    # Importamos os para manejar las rutas de forma dinámica.

# --- CONFIGURACIÓN DE RUTA ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Obtenemos la ruta absoluta de la carpeta del script.
ruta_json = os.path.join(BASE_DIR, "analisis.json")   # Armamos la ruta completa donde se guardará el JSON.

def analizar_referencias(obj):
    print("Iniciando análisis de referencias en la memoria RAM...")

    # --- 1. CREACIÓN DE LAS DIFERENTES VERSIONES ---
    # Alias: Simplemente le damos otro nombre al mismo objeto. Comparten la misma dirección de memoria.
    alias = obj
    
    # Copia superficial (Shallow Copy): Crea una nueva lista principal, pero los elementos internos siguen compartidos.
    copia_s = copy.copy(obj)
    
    # Copia profunda (Deep Copy): Clona absolutamente todo de forma recursiva. Es un objeto 100% autónomo.
    copia_d = copy.deepcopy(obj)

    # --- 2. MUTACIÓN DEL OBJETO ORIGINAL ---
    # Para demostrar cómo funcionan las referencias, alteramos un dato interno del objeto original.
    # Cambiamos el valor asociado a la clave "estado" en el primer elemento de la lista.
    obj[0]["estado"] = "ALTERADO_POR_MUTACION"

    # --- 3. CONSTRUCCIÓN DEL REPORTE ---
    # Creamos un diccionario evaluando qué pasó con cada versión después de haber mutado el original.
    # - id(): Obtiene la dirección de memoria exacta.
    # - is: Es un operador lógico que devuelve True si dos variables apuntan al mismísimo objeto físico en la RAM.
    reporte = {
        "analisis_alias": {
            "id_memoria": id(alias),
            "es_mismo_objeto_que_original": alias is obj,  # Esto será True
            "fue_afectado_por_mutacion": alias[0]["estado"] == "ALTERADO_POR_MUTACION"  # Esto será True
        },
        "analisis_copia_superficial": {
            "id_memoria": id(copia_s),
            "es_mismo_objeto_que_original": copia_s is obj,  # Esto será False (la lista externa es nueva)
            "fue_afectado_por_mutacion": copia_s[0]["estado"] == "ALTERADO_POR_MUTACION" # ¡True! Los diccionarios internos se comparten.
        },
        "analisis_deepcopy": {
            "id_memoria": id(copia_d),
            "es_mismo_objeto_que_original": copia_d is obj,  # Esto será False
            "fue_afectado_por_mutacion": copia_d[0]["estado"] == "ALTERADO_POR_MUTACION" # False. Es totalmente inmune a la mutación.
        }
    }

    # --- 4. GUARDADO EN JSON ---
    with open(ruta_json, "w", encoding="utf-8") as f:
        # Usamos indent=4 para que el JSON quede muy ordenado y fácil de leer.
        # default=str es un salvavidas: si Python encuentra un tipo de dato (como un ID larguísimo) que JSON no entiende, lo convierte a texto.
        json.dump(reporte, f, indent=4, default=str)

    print(f"¡Análisis completado! Se ha generado el archivo: {ruta_json}")


# ==========================================
# --- ZONA DE PRUEBAS PARA LA EXPOSICIÓN ---
# ==========================================

# Creamos un objeto mutable (una lista) que adentro tiene otro objeto mutable (un diccionario).
# Usar datos anidados es OBLIGATORIO para poder demostrar el fallo de la copia superficial.
datos_prueba = [{"id": 1, "estado": "INTACTO"}]

# Ejecutamos la función pasándole nuestra data de prueba.
analizar_referencias(datos_prueba)