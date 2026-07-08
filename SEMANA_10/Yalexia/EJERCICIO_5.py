import shelve  # Importamos shelve, el módulo que permite guardar diccionarios de Python en el disco duro.
import os      # Importamos os para manejar las rutas de los archivos de forma dinámica en cualquier sistema operativo.
 
# --- CONFIGURACIÓN DE RUTAS ---
# __file__ obtiene la ruta de este script, abspath saca la ruta absoluta y dirname nos deja solo la carpeta base.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Unimos la carpeta base con el nombre que le daremos a nuestra base de datos ("agenda").
ruta_db = os.path.join(BASE_DIR, "agenda")
 
 
# --- FUNCIÓN 1: CREAR (CREATE) ---
def agregar_contacto(nombre, telefono, email):
    # Abrimos la base de datos con el context manager 'with' para que se cierre sola al terminar la función.
    with shelve.open(ruta_db) as db:
        # Usamos .lower() en el nombre para guardarlo siempre en minúsculas y evitar problemas de mayúsculas al buscar.
        # Asignamos un diccionario con los datos del contacto como valor de esa clave.
        db[nombre.lower()] = {"telefono": telefono, "email": email}
 
 
# --- FUNCIÓN 2: LEER/BUSCAR (READ) ---
def buscar_contacto(nombre):
    with shelve.open(ruta_db) as db:
        # .get() busca la clave (en minúsculas). Si la encuentra, devuelve sus datos; si no, devuelve el texto de error.
        return db.get(nombre.lower(), "Contacto no encontrado")
 
 
# --- FUNCIÓN 3: LISTAR TODOS ---
def listar_contactos():
    with shelve.open(ruta_db) as db:
        print("\n--- LISTA DE CONTACTOS ---")
        # .keys() nos devuelve todas las claves (nombres) que hemos guardado en la base de datos.
        for clave in db.keys():
            # .capitalize() pone la primera letra en mayúscula solo para que se vea bonito al imprimir.
            # db[clave] accede al diccionario de ese contacto específico.
            print(f"{clave.capitalize()}: {db[clave]}")
 
 
# --- FUNCIÓN 4: ACTUALIZAR (UPDATE) ---
# Ponemos "=None" en los parámetros para que sean opcionales (el usuario puede actualizar solo uno si quiere).
def actualizar_contacto(nombre, nuevo_telefono=None, nuevo_email=None):
    with shelve.open(ruta_db) as db:
        clave = nombre.lower()  # Estandarizamos el nombre a buscar.
        if clave in db:  # Verificamos que el contacto exista antes de intentar actualizarlo.
            # PASO 1 DE LA DIAPOSITIVA: LEER
            # Extraemos el diccionario del disco duro y lo guardamos en la memoria RAM (en la variable 'datos_contacto').
            datos_contacto = db[clave]
            # PASO 2 DE LA DIAPOSITIVA: MODIFICAR
            if nuevo_telefono:  # Si el usuario mandó un teléfono nuevo...
                datos_contacto["telefono"] = nuevo_telefono  # Lo cambiamos en la memoria RAM.
            if nuevo_email:     # Si el usuario mandó un email nuevo...
                datos_contacto["email"] = nuevo_email        # Lo cambiamos en la memoria RAM.
            # PASO 3 DE LA DIAPOSITIVA: REASIGNAR
            # Tomamos el diccionario ya modificado y lo sobreescribimos en la base de datos para que se guarde en el disco.
            db[clave] = datos_contacto
            print(f"Contacto '{nombre}' actualizado exitosamente.")
        else:
            print("El contacto no existe.")
 
 
# --- FUNCIÓN 5: ELIMINAR (DELETE) ---
def eliminar_contacto(nombre):
    with shelve.open(ruta_db) as db:
        clave = nombre.lower()
        if clave in db:  # Validamos que exista para que el programa no colapse al intentar borrar algo inexistente.
            del db[clave]  # Usamos el comando 'del' (delete) para eliminar la clave y sus datos asociados.
            print(f"Contacto '{nombre}' eliminado.")
 
 
# ==========================================
# --- ZONA DE PRUEBAS PARA LA EXPOSICIÓN ---
# ==========================================
 
print("1. Agregando contactos iniciales...")
agregar_contacto("Yalexia", "987654321", "yalexia@email.com")
agregar_contacto("Grupo-2", "999000111", "proyecto@universidad.pe")
 
listar_contactos()  # Mostramos cómo quedó la agenda
 
print("\n2. Actualizando el teléfono de Yalexia...")
# Llamamos a actualizar, pasándole solo el teléfono nuevo. El email se quedará igual.
actualizar_contacto("Yalexia", nuevo_telefono="999888777")
 
listar_contactos()  # Mostramos la agenda para comprobar el cambio
