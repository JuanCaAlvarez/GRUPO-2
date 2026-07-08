#Declaramos datos_csv - valores separados por comas
datos_csv = """HUGO,20,LIMA
PACO,08,AREQUIPA
LUIS,19,IQUITOS""" #Usar """ permite guardar un texto que ocupa varias líneas hacia abajo

#dividimos el texto en una lista de lineas con splitlines()
lineas = datos_csv.splitlines() 

print("--- REPORTE DE NOTAS DE ESTUDIANTES ---")

for linea in lineas:     #La instrucción for linea in lineas- inicia un ciclo que le dice a Python: "Recorre la lista que acabamos de crear, un elemento a la vez".
    
    partes = linea.split(",") #Cada linea se divide justo deonde esta una coma
    
    nombre = partes[0]   #Indicamos su posicion de cada dato [0],[1],[2]
    nota = partes[1]
    ciudad = partes[2]
    
    
    print(f"Estudiante: {nombre} | Nota: {nota.zfill(2)} | Ciudad: {ciudad}") #usamos zfill(2) para rellenar con "0" a la izquierda

