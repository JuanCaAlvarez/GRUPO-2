import re

texto_registros = "Documentos ingresados: 74125896, 4512A785 (inválido), 1234567 (incompleto), 85236974."

# Explicación del patrón:
# \b : Representa un límite de palabra (asegura que no corte números más largos)
# \d{8} : Exactamente 8 dígitos
# \b : Otro límite de palabra al final
patron_dni = r'\b\d{8}\b'

dnis_validos = re.findall(patron_dni, texto_registros)

print("DNIs válidos detectados:")
print(dnis_validos)