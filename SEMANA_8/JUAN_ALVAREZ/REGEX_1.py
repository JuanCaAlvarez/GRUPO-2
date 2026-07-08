import re

texto = "Contacta a soporte en ayuda@empresa.com o escríbele al gerente a luis_perez123@gmail.com.pe para más detalles."

# Explicación del patrón:
# [\w.-]+ : Busca letras, números, puntos o guiones antes del @
# @       : Debe contener un arroba
# [\w.-]+ : Busca el dominio (ej. gmail, empresa)
# \.      : Debe contener un punto real
# [a-zA-Z]+ : El final del dominio (.com, .pe, etc.)
patron_correo = r'[\w.-]+@[\w.-]+\.[a-zA-Z]+'

# re.findall() devuelve una lista con todos los correos encontrados
correos_encontrados = re.findall(patron_correo, texto)

print("Correos detectados:")
for correo in correos_encontrados:
    print(f" - {correo}")