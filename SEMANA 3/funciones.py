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

# Programa principal

a = int(input("Ingrese el primer número: "))

b = int(input("Ingrese el segundo número: "))
 
print("Suma:", suma(a, b))

print("Resta:", resta(a, b))

print("Multiplicación:", multiplicacion(a, b))

print("División:", division(a, b))

print("Residuo:", residuo(a, b))

print("Factorial de A:", factorial(a))

print("Factorial de B:", factorial(b))