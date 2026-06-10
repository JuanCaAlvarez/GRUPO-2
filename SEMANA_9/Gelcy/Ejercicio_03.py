#Enunciado: Leer 'registro_sistema.log' y contar cuántos mensajes hay de cada 
#tipo: INFO, WARNING, ERROR. Mostrar el resumen

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REGIS_SISTEM = os.path.join(BASE_DIR, "archivos_practica/registro_sistema.log")

#Creamos un diccionario en memoria; la variable 'resumen_logs' guarda una REFERENCIA (dirección) a este objeto
resumen_logs = {"INFO": 0, "WARNING": 0, "ERROR": 0}

#Abrimos el archivo en modo lectura ('r'); 'archivo' funciona como nuestro PUNTERO al documento
with open(REGIS_SISTEM, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        #strip(): Quita los saltos de lines. Split("|"): Corta el texto cada vez que encuentra un '|'
        partes = linea.strip().split("|")

        #Verificamos que la línea cortada tenga al menos 2 elementos para evitar errores de formato
        if len(partes) >= 2:
            #Tomamos el segundo elemento (índice 1), que es el tipo de mensaje, y le borramos espacios extras
            tipo_mensaje = partes[1].strip()

            #Revisamos si el tipo de mensaje extraído (INFO, WARNING, ERROR) existe como clave en nuestro diccionario
            if tipo_mensaje in resumen_logs:
                #Buscamos el diccionario original mediante su REFERENCIA y aumentamos en 1 el contador de ese tipo
                resumen_logs[tipo_mensaje] += 1

print("=== RESUMEN DE REGISTROS ===")

#Desempaquetamos el diccionario obteniendo la clave (tipo) y su valor (cantidad) en cada vuelta del bucle
for tipo, cantidad in resumen_logs.items():
    print(f"{tipo}: {cantidad}")