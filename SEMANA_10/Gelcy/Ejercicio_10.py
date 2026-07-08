#Ejercicio 10:
#Mini-ORM: Clase que Envuelve sqlite3 con Referencias Internas. Crea una clase Repositorio(archivo_db, tabla) con métodos: insertar(dict), 
#buscar(clave, valor), actualizar(id, dict_cambios) y eliminar(id). Internamente mantiene un caché en memoria (dict de listas). Los métodos 
#deben sincronizar el caché con sqlite3 y manejar correctamente las referencias para que modificar el objeto retornado NO corrompa el caché.

import sqlite3  # Módulo para interactuar con la base de datos relacional.
import copy     # Módulo vital aquí: nos permite hacer 'deepcopy' para proteger el caché en memoria[cite: 513, 514].
import os       # Módulo para el manejo dinámico de las rutas de archivos.

# --- CONFIGURACIÓN DE RUTA ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Obtenemos la ruta absoluta de la carpeta actual.

# ==========================================
# --- CLASE PRINCIPAL: MINI-ORM ---
# ==========================================
class Repositorio:
    # El método __init__ se ejecuta automáticamente al crear un objeto de esta clase.
    def __init__(self, nombre_db, tabla):
        self.ruta_db = os.path.join(BASE_DIR, nombre_db) # Armamos la ruta dinámica hacia la BD.
        self.tabla = tabla                               # Guardamos el nombre de la tabla con la que trabajaremos.
        self.cache = {}                                  # Inicializamos el caché en memoria RAM (diccionario vacío)[cite: 513].

    # Método interno (oculto) para no repetir el código de conexión en cada función.
    def _conectar(self):
        conn = sqlite3.connect(self.ruta_db)
        conn.row_factory = sqlite3.Row  # Para que los resultados parezcan diccionarios.
        return conn

    # --- C (CREATE) ---
    def insertar(self, datos):
        # datos es un dict, ej: {"id": 1, "nombre": "Yalexia"}
        columnas = ", ".join(datos.keys())               # Extraemos las claves para nombrar las columnas.
        parametros = ", ".join(["?"] * len(datos))       # Creamos un "?" por cada valor para evitar Inyección SQL[cite: 524].
        valores = tuple(datos.values())                  # Convertimos los valores del diccionario a una tupla.
        
        conn = self._conectar()
        # Construimos la consulta SQL dinámicamente y le pasamos los valores.
        conn.cursor().execute(f"INSERT INTO {self.tabla} ({columnas}) VALUES ({parametros})", valores)
        conn.commit()
        conn.close()
        
        # EL PASO CRÍTICO: Guardamos en caché una COPIA PROFUNDA del diccionario.
        # Así, si el usuario modifica el dict original fuera de la clase, nuestro caché NO se corrompe[cite: 513, 514].
        self.cache[datos["id"]] = copy.deepcopy(datos)
        print(f"[*] Registro ID {datos['id']} insertado en SQLite y guardado en caché.")

    # --- R (READ) ---
    def buscar(self, clave, valor):
        # Buscamos recorriendo los valores guardados en nuestro caché (es muchísimo más rápido que ir al disco/SQLite).
        for item in self.cache.values():
            if item.get(clave) == valor:
                # Si lo encontramos, retornamos una COPIA PROFUNDA[cite: 514].
                # Esto evita que quien recibe el dato lo modifique por accidente y altere el caché interno.
                return copy.deepcopy(item)
        return None  # Retorna None si no encuentra coincidencias.

    # --- U (UPDATE) ---
    def actualizar(self, id_item, dict_cambios):
        # Preparamos el texto dinámico para el SET (ej: "nombre=?, nota=?").
        set_str = ", ".join([f"{k}=?" for k in dict_cambios.keys()])
        valores = list(dict_cambios.values()) # Extraemos los valores a actualizar.
        valores.append(id_item)               # Añadimos el ID al final de la lista para la condición WHERE.
        
        conn = self._conectar()
        conn.cursor().execute(f"UPDATE {self.tabla} SET {set_str} WHERE id=?", tuple(valores))
        conn.commit()
        conn.close()
        
        # Sincronizamos el caché para que refleje lo que acabamos de guardar en SQLite[cite: 513].
        if id_item in self.cache:
            for k, v in dict_cambios.items():
                self.cache[id_item][k] = v    # Modificamos los valores específicos en la RAM.
            # Volvemos a blindar esa posición del caché con un nuevo deepcopy[cite: 515].
            self.cache[id_item] = copy.deepcopy(self.cache[id_item])
            print(f"[*] Registro ID {id_item} actualizado en SQLite y caché sincronizado.")

    # --- D (DELETE) ---
    def eliminar(self, id_item):
        conn = self._conectar()
        conn.cursor().execute(f"DELETE FROM {self.tabla} WHERE id=?", (id_item,))
        conn.commit()
        conn.close()
        
        # Sincronizamos la eliminación borrando también el dato de la memoria RAM.
        if id_item in self.cache:
            del self.cache[id_item]
            print(f"[*] Registro ID {id_item} eliminado de SQLite y del caché.")


# ==========================================
# --- ZONA DE PRUEBAS PARA LA EXPOSICIÓN ---
# ==========================================

print("--- INICIANDO PRUEBA DEL MINI-ORM ---")

# 1. PREPARACIÓN DEL ENTORNO (Obligatorio para que no falle)
ruta_db_prueba = os.path.join(BASE_DIR, "orm_prueba.db")
conexion = sqlite3.connect(ruta_db_prueba)
conexion.execute("""
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        carrera TEXT,
        nota REAL
    )
""")
conexion.commit()
conexion.close()

# 2. INSTANCIAMOS NUESTRA CLASE REPOSITORIO
# Le pasamos el nombre del archivo y la tabla que acabamos de crear.
repo_alumnos = Repositorio("orm_prueba.db", "alumnos")

print("\n>>> PROBANDO INSERTAR")
alumno_1 = {"id": 1, "nombre": "Yalexia Uriarte", "carrera": "Sistemas", "nota": 18.0}
alumno_2 = {"id": 2, "nombre": "Carlos Alvarez", "carrera": "Industrial", "nota": 15.5}
repo_alumnos.insertar(alumno_1)
repo_alumnos.insertar(alumno_2)

print("\n>>> PROBANDO BUSCAR Y REFERENCIAS (DEEPCOPY)")
# Buscamos a Yalexia usando el método de clave-valor
resultado = repo_alumnos.buscar("nombre", "Yalexia Uriarte")
print(f"Encontrado: {resultado}")

# INTENTAMOS CORROMPER EL CACHÉ (El usuario modifica el resultado que le devolvió la búsqueda)
resultado["nota"] = 0.0  
print("\nValidación de seguridad:")
print(f"- Nota en variable externa: {resultado['nota']}")
# Imprimimos directamente desde el caché interno para confirmar que sigue intacto
print(f"- Nota original en el caché interno: {repo_alumnos.cache[1]['nota']} (¡El caché está a salvo!)")

print("\n>>> PROBANDO ACTUALIZAR")
repo_alumnos.actualizar(1, {"nota": 20.0}) # Le subimos la nota a Yalexia a 20 de forma oficial
resultado_actualizado = repo_alumnos.buscar("id", 1)
print(f"Datos tras actualización: {resultado_actualizado}")

print("\n>>> PROBANDO ELIMINAR")
repo_alumnos.eliminar(2) # Eliminamos a Carlos
busqueda_eliminado = repo_alumnos.buscar("id", 2)
print(f"Buscando al ID 2 tras eliminar: {busqueda_eliminado}")