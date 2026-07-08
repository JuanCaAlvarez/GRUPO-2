#Lista original de nombres con mayúsculas y minúsculas mezcladas
nombres = ['Juan', 'carlos', 'Gelcy', 'yalexia', 'Fermin']

#Imprimimos la lista original intacta para poder compararla
print("La lista de nombres original es: ", nombres)

#Usamos .sort() que modifica la lista original y no retorna ningún valor nuevo 
#usamos key=str.lower que ignora las mayúsculas convirtiendo los textos temporalmente para comparar 
nombres.sort(key=str.lower) 

#Imprimimos la lista original que ya fue modificada por el método sort() 
print("Lista ordenada usando sort() ignorando mayúsculas:", nombres)

#Usamos sorted() que retorna una lista nueva ordenada, manteniendo la original intacta 
#Colocamos reverse=True que es un parámetro clave que indica que el ordenamiento debe ser descendente
#Usamos key=str.lower que ignora mayúsculas convirtiendo los textos temporalmente para comparar correctamente
nueva_descendente = sorted(nombres, reverse=True, key=str.lower)

#Imprimimos la nueva lista creada de forma descendente
print("Lista ordenada descendentemente y ignorando mayusculas con sorted(): ", nueva_descendente)