# Tipos de datos fundamentales
nombre = "Maria"        #str (cadena de texto)
edad   = 22             #int (entero)
promedio = 16.5         #float (decimal)
activo = True           #bool (booleano)
vacio = None            #NoneType (vacio)

# Verificar el tipo
print(type(nombre))     # <class 'str'>
print(type(edad))       # <class 'int'>

# Conversion de tipos (casting)
texto_num = str(edad)   # 22 -> "22"
num_texto = str("30")   # "30" -> 30