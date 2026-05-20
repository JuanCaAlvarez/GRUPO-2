#Definimos la funcion
def validar_email(correo):
    #Strip: Elimina espacios
    #Upper: Convierte en mayúsculas
    correo = correo.strip().upper()

    #Condicional para verificar si es un correo válido
    if "@" in correo:
        #Split: Divine el correo por "@"
        partes = correo.split("@")

        #Condicional para devolver el dominio
        if len(partes) == 2 and "." in partes[1]:
            dominio = partes[1]
            return dominio
    return "Correo inválido"

#Solicita al usuario ingresar un email
email = input("Ingrese un correo: ")
#Imprimimos resultados
print(validar_email(email))