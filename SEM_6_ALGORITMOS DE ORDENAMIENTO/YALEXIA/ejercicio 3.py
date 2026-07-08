# Cola simple usando lista
cola = []

# a) Tomar turno
def tomar_turno(cliente):
    cola.append(cliente)

# b) Atender cliente
def atender():
    if cola:
        print("Atendiendo a:", cola.pop(0))
    else:
        print("No hay clientes")

# c) Mostrar cola
def mostrar_cola():
    print("En espera:", len(cola))
    print(cola)

# d) Simulación

# Entran 4 clientes
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Carlos")
tomar_turno("Maria")

mostrar_cola()
print("-----")

# Se atienden 2
atender()
atender()

mostrar_cola()
print("-----")

# Entra 1 más
tomar_turno("Pedro")

mostrar_cola()
print("-----")

# Se atienden todos
while cola:
    atender()

mostrar_cola()