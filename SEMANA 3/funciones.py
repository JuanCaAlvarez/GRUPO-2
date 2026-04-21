#funciones
def suma(a, b):
    return a + b
 
def resta(a, b):
    return a - b
 
def multiplicacion(a, b):
    return a * b
 
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división entre cero"
 
def residuo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: división entre cero"
    

# funcion factorial
def factorial(n):
    if n < 0:
     return "Error: no existe factorial de número negativo"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado