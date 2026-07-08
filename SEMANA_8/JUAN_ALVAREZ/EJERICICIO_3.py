#Lista inicial de correos electrónicos
emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

#Usamos .count() que recorre todo el string contando cuántas veces aparece un substring específico
#Unimos la lista en un solo string de texto para poder aplicarle el método .count()
texto_emails = " ".join(emails)
#Cuenta todas las ocurrencias del substring 'gmail' dentro de todo el texto
total_gmail = texto_emails.count('gmail')
#Muestra la cantidad obtenida por pantalla
print(f"A) Cantidad de emails de Gmail: {total_gmail}")

#Imprime la cabecera de la lista de correos resultantes
print("B) Emails que terminan en '.com': ")
#Bucle que itera a través de cada elemento de la lista 'emails'
for email in emails:
    #Usamos .endswith() que verifica si la cadena termina con el sufijo '.com' y devuelve un booleano (True/False)
    if email.endswith('.com'):
        #Si la condición es True, imprime el correo
        print(f"   - {email}")

#El operador 'in' verifica si un substring existe dentro de la lista y devuelve un tipo booleano
existe_luis = 'luis@outlook.com' in emails 
#Imprime el resultado de la comprobación lógica (True o False)
print(f"C) ¿luis@outlook.com está en la lista?: {existe_luis}")