def analizar_frecuencia(parrafo):
    # 1. Limpiamos signos de puntuación usando replace encadenado
    parrafo_limpio = parrafo.replace(".", "").replace(",", "").replace("¡", "").replace("!", "")

    # 2. Pasamos todo a minúsculas
    parrafo_limpio = parrafo_limpio.lower()

    # 3. Dividimos por espacios en una lista de palabras
    palabras = parrafo_limpio.split()

    # Definimos palabras vacías a ignorar
    stopwords = ["el", "la", "de", "y", "en", "un", "una", "con", "es", "para"]

    diccionario_frecuencias = {}

    for palabra in palabras:
        if palabra not in stopwords:
            # Si la palabra ya está en el diccionario, sumamos 1
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1
            # Si no está, la inicializamos en 1
            else:
               diccionario_frecuencias[palabra] = 1

    return diccionario_frecuencias



# Prueba
texto = "¡El análisis de datos con Python es genial! Python es muy útil en datos."
print(analizar_frecuencia(texto))