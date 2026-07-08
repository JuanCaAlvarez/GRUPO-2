<<<<<<< HEAD
# Enunciado 8: Extraer hashtags de un tweet usando cadenas
# Este programa busca las palabras que empiezan con #
# Luego las convierte a minúsculas y las ordena alfabéticamente.

# Creamos una variable llamada tweet.
# Aquí se guarda el texto que vamos a analizar.
tweet = "Aprendiendo #Python con #Datos y #Programacion en clase de #PYTHON"

# Usamos split() para dividir el tweet en palabras.
# Cada palabra se separa por los espacios.
palabras = tweet.split()

# Creamos una lista vacía donde guardaremos los hashtags encontrados.
hashtags = []

# Recorremos cada palabra del tweet.
for palabra in palabras:

    # Verificamos si la palabra empieza con el símbolo #.
    if palabra.startswith("#"):

        # Convertimos el hashtag a minúsculas usando lower().
        hashtag = palabra.lower()

        # Agregamos el hashtag a la lista.
        hashtags.append(hashtag)

# Ordenamos la lista de hashtags alfabéticamente.
hashtags_ordenados = sorted(hashtags)

# Mostramos el resultado final.
=======
# Enunciado 8: Extraer hashtags de un tweet usando cadenas
# Este programa busca las palabras que empiezan con #
# Luego las convierte a minúsculas y las ordena alfabéticamente.

# Creamos una variable llamada tweet.
# Aquí se guarda el texto que vamos a analizar.
tweet = "Aprendiendo #Python con #Datos y #Programacion en clase de #PYTHON"

# Usamos split() para dividir el tweet en palabras.
# Cada palabra se separa por los espacios.
palabras = tweet.split()

# Creamos una lista vacía donde guardaremos los hashtags encontrados.
hashtags = []

# Recorremos cada palabra del tweet.
for palabra in palabras:

    # Verificamos si la palabra empieza con el símbolo #.
    if palabra.startswith("#"):

        # Convertimos el hashtag a minúsculas usando lower().
        hashtag = palabra.lower()

        # Agregamos el hashtag a la lista.
        hashtags.append(hashtag)

# Ordenamos la lista de hashtags alfabéticamente.
hashtags_ordenados = sorted(hashtags)

# Mostramos el resultado final.
>>>>>>> 7edf3ee7fd75c3d00f204393b163b1a8c5240f33
print(hashtags_ordenados)