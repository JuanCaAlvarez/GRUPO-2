# Enunciado 8: Extraer hashtags de un tweet
# Este programa recibe un texto de tweet.
# Luego busca todas las palabras que empiezan con el símbolo #.
# Finalmente, las convierte a minúsculas, las ordena alfabéticamente
# y las muestra dentro de una lista.

# Importamos la librería re.
# Esta librería permite buscar patrones dentro de un texto.
import re

# Creamos una variable llamada tweet.
# Aquí guardamos el texto del tweet que vamos a analizar.
tweet = "Aprendiendo #Python con #Datos y #Programacion en clase de #PYTHON"

# Usamos la función findall() para buscar todos los hashtags.
# El patrón r"#\w+" significa:
# #  busca el símbolo numeral.
# \w busca letras, números o guion bajo.
# + indica que puede haber una o más letras después del #.
hashtags = re.findall(r"#\w+", tweet)

# Creamos una nueva lista llamada hashtags_minusculas.
# Recorremos cada hashtag encontrado y lo convertimos a minúsculas con lower().
hashtags_minusculas = [hashtag.lower() for hashtag in hashtags]

# Usamos sorted() para ordenar la lista alfabéticamente.
hashtags_ordenados = sorted(hashtags_minusculas)

# Mostramos en pantalla la lista final de hashtags.
print(hashtags_ordenados)