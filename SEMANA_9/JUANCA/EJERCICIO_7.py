#El objetivo es traducir las alertas de 'WARNING' a 'ADVERTENCIA' de forma completamente segura."
#Importamos el módulo 'os' que nos permite interactuar directamente con el sistema operativo.
import os

#Definimos nuestra función. Le pasamos el nombre del archivo, lo que queremos buscar y el nuevo texto.
def actualizar_archivo_texto(ruta_archivo, palabra_vieja, palabra_nueva):
    
    #Creamos el nombre de un archivo temporal. 
    # "No modificamos el archivo original directamente porque, si hay un corte de luz a la mitad, el log se corrompe."
    ruta_temp = "temporal_" + ruta_archivo
    
    #Usamos un context manager múltiple. Abrimos el original para leer ('r') y el temporal para escribir ('w').
    with open(ruta_archivo, "r", encoding="utf-8") as archivo_in, \
         open(ruta_temp, "w", encoding="utf-8") as archivo_out:
        
        #Iteramos línea por línea de forma eficiente, sin cargar todo el peso del log en la memoria RAM.
        for linea in archivo_in:
            
            #Reemplazamos el texto. 
            #"Como los strings en Python son inmutables, replace() no modifica la línea original, sino que crea un nuevo objeto en memoria."
            linea_actualizada = linea.replace(palabra_vieja, palabra_nueva)
            
            #Escribimos la línea (ya procesada) en nuestro archivo temporal.
            archivo_out.write(linea_actualizada)
            
    #Finalmente, usamos el módulo os para reemplazar el archivo original por nuestro temporal.
    # "Esto sobreescribe el original de un solo golpe, garantizando que los datos estén intactos."
    os.replace(ruta_temp, ruta_archivo)

#Definimos nuestras variables basándonos en el archivo log que nos dieron.
nombre_del_archivo = "registro_sistema.log"
palabra_a_buscar = "WARNING"
palabra_nueva = "ADVERTENCIA"

#Llamamos a la función para que haga el trabajo pesado.
actualizar_archivo_texto(nombre_del_archivo, palabra_a_buscar, palabra_nueva)

#Imprimimos la confirmación visual en la terminal.
print(f"¡Proceso completado con éxito!")
print(f"Se reemplazó la etiqueta '{palabra_a_buscar}' por '{palabra_nueva}' en '{nombre_del_archivo}'.")