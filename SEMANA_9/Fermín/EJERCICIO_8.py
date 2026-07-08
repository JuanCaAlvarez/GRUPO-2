<<<<<<< HEAD
# EXPLICACIÓN PARA LA EXPOSICIÓN:
# "Para este último ejercicio, crearemos nuestra propia base de datos binaria desde cero. 
# Implementaremos tres funciones clave: insertar datos, buscar un registro específico saltando en la memoria con seek(), y listar todo el contenido."

import struct
import os

# 1. Definimos la estructura: '20s' (string de 20 bytes) y 'i' (entero de 4 bytes). Total: 24 bytes.
FORMATO_BD = "20s i"
TAMANO_REGISTRO = struct.calcsize(FORMATO_BD)
ARCHIVO_BIN = "jugadores.bin"

# --- FUNCIÓN 1: ESCRIBIR ---
def insertar_registro(nombre, puntaje):
    # 'ab' (Append Binary) crea el archivo si no existe y añade bytes al final.
    with open(ARCHIVO_BIN, "ab") as f:
        # Rellenamos con nulos (\0) para que el texto mida exactamente 20 bytes.
        nombre_b = nombre.encode('utf-8').ljust(20, b'\0')
        data = struct.pack(FORMATO_BD, nombre_b, puntaje)
        f.write(data)

# --- FUNCIÓN 2: LEER POR ÍNDICE ---
def leer_por_indice(indice):
    with open(ARCHIVO_BIN, "rb") as f:
        # MAGIA: seek() salta directamente al byte exacto donde empieza nuestro registro.
        f.seek(indice * TAMANO_REGISTRO)
        data_cruda = f.read(TAMANO_REGISTRO)
        
        if data_cruda:
            nombre_b, puntaje = struct.unpack(FORMATO_BD, data_cruda)
            # decodificamos y limpiamos la basura (nulos).
            return f"Nombre: {nombre_b.strip(b'\0').decode('utf-8')}, Puntaje: {puntaje}"
        return "Registro no encontrado."

# --- FUNCIÓN 3: LISTAR TODOS (La que pedía el enunciado final) ---
def listar_todos():
    print("\n--- LISTADO COMPLETO DE REGISTROS BINARIOS ---")
    
    # Validación por si tratamos de leer antes de crear el archivo
    if not os.path.exists(ARCHIVO_BIN):
        print("El archivo binario aún no ha sido creado.")
        return

    with open(ARCHIVO_BIN, "rb") as f:
        # Un bucle infinito que leerá bloque por bloque hasta que se acaben los datos.
        while True:
            # Leemos exactamente 24 bytes (lo que pesa un registro).
            data_cruda = f.read(TAMANO_REGISTRO)
            
            # Si f.read() devuelve vacío, significa que llegamos al final del archivo. Rompemos el bucle.
            if not data_cruda:
                break 
                
            nombre_b, puntaje = struct.unpack(FORMATO_BD, data_cruda)
            nombre = nombre_b.strip(b'\0').decode('utf-8')
            print(f"- Nombre: {nombre} | Puntaje: {puntaje}")


# ==========================================
# DEMOSTRACIÓN EN VIVO PARA LA PRESENTACIÓN
# ==========================================

# Insertamos un par de registros de prueba (esto CREA el archivo automáticamente)
insertar_registro("JugadorAlpha", 1500)
insertar_registro("JugadorBeta", 2300)
insertar_registro("GamerPro99", 9999)

# Demostramos la lectura directa por índice (Imprimirá a JugadorBeta)
print("Buscando el índice 1 (el segundo registro) con seek():")
print(leer_por_indice(1))

# Demostramos el listado completo
=======
# EXPLICACIÓN PARA LA EXPOSICIÓN:
# "Para este último ejercicio, crearemos nuestra propia base de datos binaria desde cero. 
# Implementaremos tres funciones clave: insertar datos, buscar un registro específico saltando en la memoria con seek(), y listar todo el contenido."

import struct
import os

# 1. Definimos la estructura: '20s' (string de 20 bytes) y 'i' (entero de 4 bytes). Total: 24 bytes.
FORMATO_BD = "20s i"
TAMANO_REGISTRO = struct.calcsize(FORMATO_BD)
ARCHIVO_BIN = "jugadores.bin"

# --- FUNCIÓN 1: ESCRIBIR ---
def insertar_registro(nombre, puntaje):
    # 'ab' (Append Binary) crea el archivo si no existe y añade bytes al final.
    with open(ARCHIVO_BIN, "ab") as f:
        # Rellenamos con nulos (\0) para que el texto mida exactamente 20 bytes.
        nombre_b = nombre.encode('utf-8').ljust(20, b'\0')
        data = struct.pack(FORMATO_BD, nombre_b, puntaje)
        f.write(data)

# --- FUNCIÓN 2: LEER POR ÍNDICE ---
def leer_por_indice(indice):
    with open(ARCHIVO_BIN, "rb") as f:
        # MAGIA: seek() salta directamente al byte exacto donde empieza nuestro registro.
        f.seek(indice * TAMANO_REGISTRO)
        data_cruda = f.read(TAMANO_REGISTRO)
        
        if data_cruda:
            nombre_b, puntaje = struct.unpack(FORMATO_BD, data_cruda)
            # decodificamos y limpiamos la basura (nulos).
            return f"Nombre: {nombre_b.strip(b'\0').decode('utf-8')}, Puntaje: {puntaje}"
        return "Registro no encontrado."

# --- FUNCIÓN 3: LISTAR TODOS (La que pedía el enunciado final) ---
def listar_todos():
    print("\n--- LISTADO COMPLETO DE REGISTROS BINARIOS ---")
    
    # Validación por si tratamos de leer antes de crear el archivo
    if not os.path.exists(ARCHIVO_BIN):
        print("El archivo binario aún no ha sido creado.")
        return

    with open(ARCHIVO_BIN, "rb") as f:
        # Un bucle infinito que leerá bloque por bloque hasta que se acaben los datos.
        while True:
            # Leemos exactamente 24 bytes (lo que pesa un registro).
            data_cruda = f.read(TAMANO_REGISTRO)
            
            # Si f.read() devuelve vacío, significa que llegamos al final del archivo. Rompemos el bucle.
            if not data_cruda:
                break 
                
            nombre_b, puntaje = struct.unpack(FORMATO_BD, data_cruda)
            nombre = nombre_b.strip(b'\0').decode('utf-8')
            print(f"- Nombre: {nombre} | Puntaje: {puntaje}")


# ==========================================
# DEMOSTRACIÓN EN VIVO PARA LA PRESENTACIÓN
# ==========================================

# Insertamos un par de registros de prueba (esto CREA el archivo automáticamente)
insertar_registro("JugadorAlpha", 1500)
insertar_registro("JugadorBeta", 2300)
insertar_registro("GamerPro99", 9999)

# Demostramos la lectura directa por índice (Imprimirá a JugadorBeta)
print("Buscando el índice 1 (el segundo registro) con seek():")
print(leer_por_indice(1))

# Demostramos el listado completo
>>>>>>> 7edf3ee7fd75c3d00f204393b163b1a8c5240f33
listar_todos()