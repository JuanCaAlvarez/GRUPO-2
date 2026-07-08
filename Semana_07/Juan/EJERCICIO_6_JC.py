texto = "El curso de programacion web es lo máximo" #declaramos la frase original
prohibido =["programacion","web"] #declaramos las palabras prohibidas
print(f"Texto original: {texto}")  #Muestra como esta el texto original, "f" significa formato que significa que antes le estas avisando que vas a insertar variables

for palabra in prohibido:#Inicia un bucle (ciclo) que va a recorrer tu lista prohibido. 
    #En la primera vuelta, la variable temporal palabra valdrá "programacion", y en la segunda vuelta valdrá "web".

    asterisco = "*" * len(palabra) #Usamos len(palabra) para saber cuantas letras tiene la palabra actual. Luego lo multiplicamos por "*".

    texto = texto.replace(palabra, asterisco) #Usa el método .replace() para buscar la palabra original dentro del texto y sustituirla por la cadena de asteriscos que acabamos de crear. 
   
print(f"Texto cambiado:{texto}") #Mostramos El texto modificado reemplazando las palabras prohibidas por "*"
