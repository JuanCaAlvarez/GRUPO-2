import re  # Importamos la librería para usar expresiones regulares

# Lista con datos mezclados en textos
datos = [
    "Ana García - edad:25 - tel:987654321",
    "Luis Pérez - edad:30 - tel:912345678"
]

personas = []  # Aquí guardaremos los datos ordenados

# Recorremos cada texto de la lista
for dato in datos:
    # Patrón para extraer nombre, edad y teléfono
    patron = r"(.+) - edad:(\d+) - tel:(\d+)"

    # Separamos los datos encontrados
    nombre, edad, telefono = re.search(patron, dato).groups()

    # Guardamos cada persona en un diccionario
    personas.append({
        "nombre": nombre,
        "edad": int(edad),
        "telefono": telefono
    })

# Ordenamos la lista según la edad
personas.sort(key=lambda persona: persona["edad"])

# Mostramos el resultado
for persona in personas:
    print(persona)