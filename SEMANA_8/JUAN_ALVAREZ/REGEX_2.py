import re

texto_clientes = "Juan: 987654321, Ana (casa): 444-5555, Carlos móvil: 912 345 678, Error: 99911"

# Explicación del patrón:
# \d{3} : Busca grupos exactos de 3 números
# [\s-]? : Permite que haya un espacio o un guion de forma opcional (?)
patron_telefono = r'\d{3}[\s-]?\d{3}[\s-]?\d{3}'

telefonos = re.findall(patron_telefono, texto_clientes)

print("Teléfonos móviles válidos encontrados:")
for tel in telefonos:
    print(f" - {tel}")