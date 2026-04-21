def factorial(n):
    if n < 0:
        return "Error: no existe factorial de número negativo"

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado 