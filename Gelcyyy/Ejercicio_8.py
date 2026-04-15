# Solicitar cantidad de notas
n = int(input("¿Cuántas notas deseas ingresar?: "))

# Inicializar variables
suma = 0
mayor = -1
menor = 21
aprobados = 0

# Ingreso de notas
for i in range(n):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    
    suma += nota
    
    if nota > mayor:
        mayor = nota
        
    if nota < menor:
        menor = nota
        
    if nota >= 11:
        aprobados += 1

# Cálculo del promedio
promedio = suma / n

# Mostrar resultados
print("\n--- Estadísticas ---")
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {mayor:.2f}")
print(f"Nota más baja: {menor:.2f}")
print(f"Cantidad de aprobados: {aprobados}")