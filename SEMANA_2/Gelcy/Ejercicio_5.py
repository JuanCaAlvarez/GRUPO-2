num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
op = input("Ingresa el operador (+, -, *, /): ")

match op:
    case "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado:.2f}")
    case "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado:.2f}")
    case "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado:.2f}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado:.2f}")
        else:
            print("Error: No se puede dividir entre cero")
    case _:
        print("Operador no válido")
        
