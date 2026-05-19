# Ejemplo de una línea típica de Log de Apache
linea_log = '192.168.1.50 - - [18/May/2026:20:00:00 -0500] "GET /index.html HTTP/1.1" 200 1024'



# 1. Separamos por espacios por defecto
partes = linea_log.split()



# 2. Extraemos por índices según la estructura del log
ip = partes[0]



# El método suele quedar como '"GET', así que le quitamos las comillas dobles
metodo_http = partes[5].replace('"', '')



ruta = partes[6]
codigo_estado = partes[8]



# 3. Imprimimos los resultados extraídos
print(f"IP: {ip}")
print(f"Método HTTP: {metodo_http}")
print(f"Ruta: {ruta}")
print(f"Código de Estado: {codigo_estado}")