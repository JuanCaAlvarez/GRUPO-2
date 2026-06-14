import os
import csv

# 1. Definimos la ruta base dinámica
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 2. Armamos la ruta completa al archivo
ruta_archivo = os.path.join(BASE_DIR, "estudiantes.csv")

def procesar_estudiantes(archivo):
    notas = []  # Creamos una lista vacía para almacenar las notas y luego promediarlas
    
    # Abrimos el archivo en modo lectura ("r"). 
    # encoding="utf-8" asegura que lea bien las tildes y ñ.
    # newline="" evita saltos de línea adicionales al leer en diferentes sistemas operativos.
    with open(archivo, "r", encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)  # DictReader convierte cada fila en un diccionario usando la primera fila (cabecera) como claves
        
        for fila in lector:  # Iteramos línea por línea el archivo sin cargar todo en la memoria a la vez
            nota_actual = float(fila["nota"])  # Convertimos el valor string del CSV a un número decimal (float) para poder operar con él
            notas.append(nota_actual)  # Agregamos la nota convertida a nuestra lista de notas
            
            if nota_actual >= 11.0:  # Evaluamos si la nota es mayor o igual al umbral aprobatorio
                # Imprimimos los datos del alumno accediendo a los valores por el nombre de la columna
                print(f"Aprobado: {fila['nombre']} - {fila['carrera']} ({nota_actual})")
    
    if notas:  # Verificamos que la lista no esté vacía para evitar el error de división por cero
        prom = sum(notas) / len(notas)  # sum() suma todos los elementos y len() cuenta cuántos hay
        print(f"\nPromedio del grupo: {prom:.2f}")  # Imprimimos el promedio formateado a 2 decimales (.2f)

# Llamamos a la función asumiendo que el archivo existe en la misma carpeta
procesar_estudiantes(ruta_archivo)