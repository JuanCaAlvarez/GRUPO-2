<<<<<<< HEAD
# EJERCICIO BÁSICO 1: Lectura y referencias de memoria
with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        
        # 1. Validación de seguridad: Si la línea está vacía, saltar a la siguiente
        if not linea.strip():
            continue
            
        datos = linea.strip().split(",")
        
        # 2. Validación estructural: Asegurarnos de que realmente hay 4 columnas
        if len(datos) == 4:
            nombre = datos[0] 
            nota = float(datos[3]) 
            
            print(f"Estudiante: {nombre} | Referencia (id): {id(nombre)}")
            print(f"Nota: {nota} | Referencia (id): {id(nota)}")
            print("-" * 40)
        else:
=======
# EJERCICIO BÁSICO 1: Lectura y referencias de memoria
with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        
        # 1. Validación de seguridad: Si la línea está vacía, saltar a la siguiente
        if not linea.strip():
            continue
            
        datos = linea.strip().split(",")
        
        # 2. Validación estructural: Asegurarnos de que realmente hay 4 columnas
        if len(datos) == 4:
            nombre = datos[0] 
            nota = float(datos[3]) 
            
            print(f"Estudiante: {nombre} | Referencia (id): {id(nombre)}")
            print(f"Nota: {nota} | Referencia (id): {id(nota)}")
            print("-" * 40)
        else:
>>>>>>> 7edf3ee7fd75c3d00f204393b163b1a8c5240f33
            print(f"Línea ignorada por formato incorrecto: {linea.strip()}")