#Definimos las 3 listas con 4 productos
nombres = ['Laptop','Consola','Golosina','Camara'] #Lista1
precios = [2000,2500,20,1200] #Lista2
cantidades = [3,5,25,2] #Lista3


precio_total = 0 #Variable empieza en 0 para que comienze a acumular el total

#Usamos zip() que itera las 3 listas en paralelo automáticamente, sincronizándolas por su índice
for nombre, precio, cantidad in zip(nombres, precios, cantidades): #con zip() recorre todos los registros
    #Imprime el registro actual combinando los datos paralelos de las tres listas
    print(f'Producto: {nombre} | Precio: {precio} soles | Cantidad: {cantidad} unidades')

#Multiplicamos el precio por la cantidad del registro y lo suma al total
precio_total += (precio * cantidad)

#Imprime el resultado total una vez que el bucle ha terminado de recorrer los arreglos
print(f'El precio total del inventario es: {precio_total}')