#Abrimos o creamos el archivo 'notas_nuevas.txt' en modo escritura ('w'), lo cual vacía cualquier contenido previo que existiera allí.
with open("notas_nuevas.txt", "w", encoding="utf-8") as archivo_salida:
    
    #Abrimos en paralelo el archivo original 'estudiantes.txt' en modo de solo lectura ('r') para extraer la información.
    with open("estudiantes.txt", "r", encoding="utf-8") as archivo_origen:
        
        #Iniciamos el ciclo para procesar secuencialmente cada una de las líneas de texto del archivo de origen.
        for linea in archivo_origen:
            
            #Verificamos si la línea leída está completamente vacía para evitar fallos de segmentación o división.
            if not linea.strip():
                #Saltamos la línea en blanco y continúa con el bucle sin ejecutar el código que viene debajo.
                continue
                
            #Segmentamos la línea de texto usando la coma como delimitador para poblar una lista indexada de variables.
            datos = linea.strip().split(",")
            
            #Comprobamos que la lista resultante contenga las 4 columnas estructurales del archivo fuente.
            if len(datos) == 4:
                
                #Creamos una etiqueta de referencia llamada 'nombre' apuntando al string del alumno (índice 0).
                nombre = datos[0]
                
                #Creamos una etiqueta de referencia llamada 'nota' apuntando al valor numérico decimal del alumno (índice 3).
                nota = float(datos[3])
                
                #Evaluamos mediante un condicional si el valor numérico de la nota es mayor o igual al umbral de 8.5.
                if nota >= 8.5:
                    
                    #Escribimos la cadena formateada en el archivo. Se añade '\n' manualmente porque el método write() no inserta saltos de línea.
                    archivo_salida.write(f"{nombre} - {nota}\n")

#Se muestra un mensaje final de confirmación en la terminal del sistema una vez que los dos archivos se cierran de forma segura.
print("¡Archivo 'notas_nuevas.txt' generado exitosamente con los alumnos aprobados!")