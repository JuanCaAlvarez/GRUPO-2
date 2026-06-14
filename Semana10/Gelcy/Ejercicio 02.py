#Ejercicio 02:
#Escribir Reporte CSV A partir de una lista de diccionarios con claves nombre, nota y carrera, genera un archivo "reporte.csv" que 
#incluya una columna adicional estado con valores "Aprobado" o "Reprobado" (umbral 11). Agrega una fila final con el promedio.

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTE_ALUMNOS = os.path.join(BASE_DIR, "reporte.csv")

#Creamos la lista de diccionarios con las claves: NOMBRE, NOTA y CARRERA
alumnos = [
    {"nombre": "Ana", "nota": 15, "carrera": "Ingeniería"},
    {"nombre": "Luis", "nota": 9, "carrera": "Derecho"},
    {"nombre": "María", "nota": 18, "carrera": "Medicina"},
    {"nombre": "Nessareth", "nota": 20, "carrera": "Ingeniería"},
    {"nombre": "Elías", "nota": 17, "carrera": "Contabilidad"},
]

#Acumulador 
suma = 0

#CREAMOS Y ESCRIBIMOS EL ARCHIVO "reporte.csv"
with open(REPORTE_ALUMNOS, "w", newline="", encoding="utf-8") as archivo:

    campos = ["nombre", "nota", "carrera", "estado"]

    escritor = csv.DictWriter(archivo, fieldnames=campos)

    #Escribir encabezados
    escritor.writeheader()

    #Bucle para recorrer la lista de alumnos
    for alumno in alumnos:

        #Determinar si aprobó o reprobó
        if alumno["nota"] >= 11:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        #Acumular las notas para calcular el promedio
        suma += alumno["nota"]

        #Escribir la fila
        escritor.writerow({
            "nombre": alumno["nombre"],
            "nota": alumno["nota"],
            "carrera": alumno["carrera"],
            "estado": estado
        })

    #CALCULAMOS EL PROMEDIO
    promedio = suma / len(alumnos)

    #Agregar fila final con el promedio
    escritor.writerow({
        "nombre": "PROMEDIO", 
        "nota": promedio, 
        "carrera": "Sin Carrera",
        "estado": "Sin Estado"
    })


print("Reporte generado correctamente.")