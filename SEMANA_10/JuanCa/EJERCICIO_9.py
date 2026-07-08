import os
import csv
import json
import sqlite3
import copy
from collections import defaultdict  # Estructura de datos que auto-inicializa sus claves

# --- CONFIGURACIÓN DE RUTAS DINÁMICAS ---
# Obtenemos la ruta exacta de la carpeta donde está guardado este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Armamos las rutas absolutas para todos los archivos que vamos a usar o crear
ruta_csv = os.path.join(BASE_DIR, "estudiantes.csv")
ruta_json = os.path.join(BASE_DIR, "resultado.json")
ruta_db = os.path.join(BASE_DIR, "notas.db")


# --- PASO A: EXTRAER (Leer el CSV) ---
alumnos = []
# Abrimos el CSV original en modo lectura
with open(ruta_csv, "r", encoding="utf-8", newline="") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        fila["nota"] = float(fila["nota"])  # Convertimos la nota de texto a decimal
        alumnos.append(fila)


# --- PASO B: TRANSFORMAR (Procesar los datos) ---
# Hacemos un deepcopy para procesar los datos sin alterar la lista original extraída
procesados = copy.deepcopy(alumnos)

# Ordenamos la lista de mayor a menor basándonos en la nota (para poder rankearlos)
procesados.sort(key=lambda x: x["nota"], reverse=True) 

for i, alum in enumerate(procesados):  # enumerate nos da un contador (i) que arranca en 0
    # Asignamos el estado usando un operador ternario
    alum["estado"] = "Aprobado" if alum["nota"] >= 11 else "Reprobado"
    # El ranking es la posición en la lista ordenada (sumamos 1 porque el índice empieza en 0)
    alum["ranking"] = i + 1  


# --- PASO C: CARGAR EN JSON (Agrupado por carrera) ---
# defaultdict(list) crea automáticamente una lista vacía si la carrera aún no existe en el diccionario
jerarquia = defaultdict(list)
for alum in procesados:
    jerarquia[alum["carrera"]].append(alum)  # Agrupamos los alumnos por carrera

# Guardamos el diccionario jerárquico en un nuevo archivo JSON
with open(ruta_json, "w", encoding="utf-8") as f:
    json.dump(jerarquia, f, indent=2, ensure_ascii=False)


# --- PASO D: CARGAR EN SQLITE3 (Base de datos relacional) ---
# Conectamos a la base de datos (se crea el archivo si no existe en la ruta especificada)
conn = sqlite3.connect(ruta_db)
cursor = conn.cursor()

# 1. Creamos la tabla obligatoriamente por si es la primera vez que ejecutamos el script
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        carrera TEXT NOT NULL,
        nota REAL,
        estado TEXT,
        ranking INTEGER
    )
""")

# 2. Preparamos una lista de tuplas, que es el formato exacto que sqlite3 requiere para inserciones masivas
datos_sql = [(a["nombre"], a["carrera"], a["nota"], a["estado"], a["ranking"]) for a in procesados]

# 3. executemany inserta todos los registros de un solo golpe, optimizando el rendimiento
cursor.executemany("INSERT INTO notas (nombre, carrera, nota, estado, ranking) VALUES (?,?,?,?,?)", datos_sql)

# Confirmamos los cambios en el disco y cerramos la conexión
conn.commit()
conn.close()

print("¡Proceso ETL completado con éxito! Revisa tu carpeta para ver el JSON y la base de datos creados.")