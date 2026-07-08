def analizar_frecuencia(parrafo): # Definimos una función que recibe un texto (párrafo)
    # 1. Limpiamos signos de puntuación usando replace encadenado
    parrafo_limpio = parrafo.replace(".", "").replace(",", "").replace("¡", "").replace("!", "") # Eliminamos signos de puntuación del texto

    # 2. Pasamos todo a minúsculas
    parrafo_limpio = parrafo_limpio.lower() # Convertimos todo el texto a minúsculas para evitar duplicados

    # 3. Dividimos por espacios en una lista de palabras

    palabras = parrafo_limpio.split() # Convertimos el texto en una lista de palabras

    # Definimos palabras vacías a ignorar
    stopwords = ["el", "la", "de", "y", "en", "un", "una", "con", "es", "para"] # Lista de palabras comunes que no se contarán

    diccionario_frecuencias = {} # Creamos un diccionario vacío para almacenar las frecuencias

    for palabra in palabras:         # Recorremos cada palabra de la lista
        if palabra not in stopwords: # Verificamos que la palabra no sea una stopword 
            # Si la palabra ya está en el diccionario, sumamos 1
              if palabra in diccionario_frecuencias:
                 diccionario_frecuencias[palabra] += 1  # Incrementamos su contador
            # Si no está, la inicializamos en 1
              else:
                  diccionario_frecuencias[palabra] = 1 # Agregamos la palabra con valor inicial 1

    return diccionario_frecuencias # Retornamos el diccionario con las frecuencias

# Prueba
texto = "¡El análisis de datos con Python es genial! Python es muy útil en datos." # Definimos un texto de ejemplo
print(analizar_frecuencia(texto)) # Llamamos a la función e imprimimos el resultado