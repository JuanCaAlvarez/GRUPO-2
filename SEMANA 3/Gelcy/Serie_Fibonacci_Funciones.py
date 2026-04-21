#realizar un algoritmo que permita mostrar los "n" primeros números de la serie de fivonachi

num = int(input("Ingrese la cantidad de números: "))

#Serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

def fibonacci(num):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(3, num + 1):
        nuevo = a + b
        print(nuevo)
        a = b
        b = nuevo


fibonacci(num)