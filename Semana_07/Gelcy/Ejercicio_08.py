#Enunciado 8: Extraer hashtags de un tweet. Este programa recibe un texto de tweet.
#Luego busca todas las palabras que empiezan con el símbolo #. Finalmente, las 
#convierte a minúsculas, las ordena alfabéticamente y las muestra dentro de una lista.

#Solicitamos al usuario ingresar un tweet
tweet = input("Ingrese un tweet: ")

#Split: Divide el texto por medio de espacios y lo convierte en lista
palabras = tweet.split()

#Creamos lista vacía
hashtags = []

#Iniciamos un bucle que recorre palabra por palabra
for palabra in palabras:

    #Condicional para encontrar  una palabra inicie con #
    if palabra.startswith("#"):
        #Si encuentra, lo coloca en minusculas y lo añade a la lista hashtags
        hashtags.append(palabra.lower())

#Sort: Ordena alfabéticamente
hashtags.sort()

#Imprime resultados
print("Hashtags encontrados:", hashtags)