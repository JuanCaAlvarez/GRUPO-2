# Ejemplo de una línea típica de Log de Apache
linea_log = '192.168.1.50 - - [18/May/2026:20:00:00 -0500] "GET /index.html HTTP/1.1" 200 1024'


# 1. Separamos por espacios por defecto
partes = linea_log.split()    #dividimos la cadena en una lista usando espacios como separador

# 2. Extraemos por índices según la estructura del log
ip = partes[0]      # la IP siempre está en la primera posición

# El método suele quedar como '"GET', así que le quitamos las comillas dobles
metodo_http = partes[5].replace('"', '')   # obtenemos el metodo HTTP y eliminamos las comillas


ruta = partes[6]   # la ruta del recurso está en la posición 6
codigo_estado = partes[8]  # el código de estado HTTP está en la posición 8

# 3. Imprimimos los resultados extraídos
print(f"IP: {ip}")     # mostramos la dirección IP
print(f"Método HTTP: {metodo_http}") # mostramos el metodo HTTP (GET, POST, etc.)
print(f"Ruta: {ruta}")   # mostramos la ruta soliciada
print(f"Código de Estado: {codigo_estado}") # mostramos el código de respuestas del servidor