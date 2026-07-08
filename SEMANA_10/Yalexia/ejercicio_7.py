import sqlite3  # Importamos el módulo estándar de Python para interactuar con bases de datos SQLite[cite: 220].

import os       # Importamos el módulo os para manejar rutas de archivos en el sistema operativo.
 
# --- CONFIGURACIÓN DE RUTA ---

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Obtenemos la ruta absoluta de la carpeta donde está este script.

ruta_db = os.path.join(BASE_DIR, "cursos.db")         # Unimos la carpeta base con el nombre de la base de datos ("cursos.db")[cite: 492].
 
# --- FUNCIÓN AUXILIAR DE CONEXIÓN ---

def conectar():

    conn = sqlite3.connect(ruta_db)  # Establecemos la conexión. Si "cursos.db" no existe en la ruta, lo crea automáticamente[cite: 224].

    # row_factory = sqlite3.Row permite que los resultados de un SELECT se comporten como diccionarios en vez de tuplas[cite: 243, 494].

    conn.row_factory = sqlite3.Row   

    return conn                      # Retornamos el objeto de conexión para poder usarlo en las otras funciones.
 
# --- FUNCIÓN DE INICIALIZACIÓN ---

def crear_tabla():

    conn = conectar()                # Llamamos a nuestra función para conectarnos a la base de datos.

    # Ejecutamos una consulta SQL directa para crear la tabla 'cursos' solo si aún no existe en el archivo.

    conn.cursor().execute("""

        CREATE TABLE IF NOT EXISTS cursos (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            docente TEXT NOT NULL,

            cupos INTEGER NOT NULL,

            activo INTEGER DEFAULT 1

        )

    """)

    conn.commit()                    # Confirmamos y guardamos los cambios de la estructura en la base de datos[cite: 238].

    conn.close()                     # Cerramos la conexión para liberar memoria y evitar bloqueos[cite: 239].
 
# --- C (CREATE - Crear registro) ---

def insertar_curso(nombre, docente, cupos):

    conn = conectar()                # Abrimos conexión.

    # Usamos signos de interrogación (?) como parámetros de seguridad para evitar ataques de Inyección SQL[cite: 235, 494].

    # Los valores reales (nombre, docente, cupos) se pasan de forma segura en una tupla al final de la instrucción.

    conn.cursor().execute("INSERT INTO cursos (nombre, docente, cupos) VALUES (?,?,?)", (nombre, docente, cupos))

    conn.commit()                    # Guardamos el nuevo registro permanentemente en el disco[cite: 494].

    conn.close()                     # Cerramos la conexión.

    print(f"Curso '{nombre}' insertado.") # Imprimimos un mensaje de éxito en la terminal.
 
# --- R (READ - Leer registros) ---

def listar_cursos():

    conn = conectar()                # Abrimos conexión.

    cur = conn.cursor()              # Creamos un 'cursor', que es el objeto encargado de ejecutar las consultas y recorrer resultados.

    cur.execute("SELECT * FROM cursos")  # Ejecutamos la consulta SQL para traer todos los registros de la tabla.

    print("\n--- LISTA DE CURSOS ---")

    for fila in cur.fetchall():      # cur.fetchall() recupera todas las filas resultantes de la consulta de un solo golpe[cite: 248].

        print(dict(fila))            # Convertimos cada fila a un diccionario (gracias al row_factory) y lo imprimimos[cite: 249].

    conn.close()                     # Cerramos la conexión.
 
# --- U (UPDATE - Actualizar registro) ---

def actualizar_cupos(id_curso, nuevos_cupos):

    conn = conectar()                # Abrimos conexión.

    # Actualizamos el campo 'cupos' especificando el 'id' exacto del curso que queremos modificar[cite: 251, 253].

    conn.cursor().execute("UPDATE cursos SET cupos=? WHERE id=?", (nuevos_cupos, id_curso))

    conn.commit()                    # Confirmamos la actualización en la base de datos[cite: 494].

    conn.close()                     # Cerramos la conexión.

    print(f"Cupos actualizados para el curso ID: {id_curso}")
 
# --- D (DELETE - Eliminar registro) ---

def eliminar_curso(id_curso):

    conn = conectar()                # Abrimos conexión.

    # Ejecutamos la instrucción DELETE filtrando por el ID[cite: 256, 258]. 

    # IMPORTANTE: La coma en (id_curso,) es obligatoria en Python para que lo reconozca como una tupla, aunque tenga un solo elemento.

    conn.cursor().execute("DELETE FROM cursos WHERE id=?", (id_curso,))

    conn.commit()                    # Confirmamos la eliminación del registro[cite: 494].

    conn.close()                     # Cerramos la conexión.

    print(f"Curso ID: {id_curso} eliminado.")
 
 
# ==========================================

# --- ZONA DE PRUEBAS PARA LA EXPOSICIÓN ---

# ==========================================
 
print("1. Creando base de datos y tabla...")

crear_tabla()                        # Llamamos a la función que asegura que la estructura inicial exista.
 
print("\n2. Insertando cursos...")

insertar_curso("Programación Python", "Percy Pardo Zapata", 30)  # Insertamos el primer curso de prueba.

insertar_curso("Bases de Datos", "Yalexia Uriarte Ahuanari", 25) # Insertamos el segundo curso con el nombre solicitado.
 
print("\n3. Listando después de insertar:")

listar_cursos()                      # Verificamos que los dos cursos se hayan guardado en el archivo .db.
 
print("\n4. Actualizando cupos del curso 1 (de 30 a 40)...")

actualizar_cupos(1, 40)              # Modificamos los cupos del curso con ID 1.
 
print("\n5. Listando después de actualizar:")

listar_cursos()                      # Comprobamos visualmente que el curso 1 ahora tiene 40 cupos.
 
print("\n6. Eliminando el curso 2...")

eliminar_curso(2)                    # Borramos el curso con ID 2 (Bases de Datos).
 
print("\n7. Listado final:")

listar_cursos()                      # Verificamos que solo quede el curso 1 en la base de datos tras la eliminación.
 