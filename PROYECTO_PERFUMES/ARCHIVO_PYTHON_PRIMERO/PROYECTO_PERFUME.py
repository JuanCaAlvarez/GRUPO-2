# =========================================================
# SISTEMA DE VENTAS - PERFUMES (VERSIÓN PYTHON)
# =========================================================

# Inicialización del Inventario (Listas dinámicas)
codigos = ["P-001", "P-002", "P-003"]
nombres_perfumes = ["Perfume Floral", "Locion Citrus", "Extracto Maderas"]
stock = [10, 5, 0]
precios = [150.00, 120.00, 200.00]

# Directorio de Clientes
nombres_cli = []
telefonos_cli = []

# Historial de Ventas
historial_cliente = []
historial_perfume = []
historial_cantidad = []
historial_total = []
historial_fecha = []

opcion_menu = 0

# BUCLE PRINCIPAL DEL SISTEMA
while opcion_menu != 6:
    print("\n==========================================")
    print("       SISTEMA DE VENTAS - PERFUMES       ")
    print("==========================================")
    print("1. Registrar nueva venta")
    print("2. Ver estado del inventario")
    print("3. Guardar y ver directorio de clientes")
    print("4. Agregar nuevo perfume al catalogo")
    print("5. Buscar en Historial de Ventas")
    print("6. Salir")
    print("==========================================")
    
    # Validación de entrada para evitar que el programa colapse si ingresan letras
    try:
        opcion_menu = int(input("Elija una opcion: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        continue

    if opcion_menu == 1:
        print("\n--- REGISTRAR VENTA ---")
        fecha_pedido = input("Ingrese fecha de la venta (Ej. 24/06): ")
        nombre_cliente = input("Ingrese el nombre del cliente que compra: ")
        
        # Guardado automático de cliente
        if nombre_cliente not in nombres_cli:
            print(">> Cliente nuevo detectado <<")
            telefono = input("Ingrese el telefono para guardarlo en el directorio: ")
            nombres_cli.append(nombre_cliente)
            telefonos_cli.append(telefono)
            print(">> Cliente guardado exitosamente en el directorio <<")
        else:
            print(">> Cliente frecuente reconocido <<")
            
        print("------------------------------------------")
        nombre_perfume = input("Ingrese el NOMBRE del perfume a vender: ")
        
        # Búsqueda en el inventario
        if nombre_perfume in nombres_perfumes:
            indice = nombres_perfumes.index(nombre_perfume)
            print(f"Stock actual: {stock[indice]}")
            
            try:
                cantidad = int(input("Ingrese la cantidad solicitada: "))
            except ValueError:
                print("Error: Ingrese un valor numérico para la cantidad.")
                continue
                
            if cantidad <= stock[indice]:
                # Actualizar inventario
                stock[indice] -= cantidad
                total = cantidad * precios[indice]
                
                # Guardar en historial
                historial_cliente.append(nombre_cliente)
                historial_perfume.append(nombre_perfume)
                historial_cantidad.append(cantidad)
                historial_total.append(total)
                historial_fecha.append(fecha_pedido)
                
                print("\n==========================================")
                print("           COMPROBANTE DE VENTA           ")
                print("==========================================")
                print(f"Fecha: {fecha_pedido}")
                print(f"Cliente: {nombre_cliente}")
                print(f"Producto: {nombre_perfume}")
                print(f"Cantidad: {cantidad}")
                print(f"Total a pagar: S/ {total}")
                print("==========================================")
                print(">> Venta guardada en el historial <<")
            else:
                print(f"ALERTA: Stock insuficiente. Solo quedan {stock[indice]} unidades.")
        else:
            print(f"ALERTA: El perfume '{nombre_perfume}' no existe en el catalogo.")

    elif opcion_menu == 2:
        print("\n--- ESTADO DEL INVENTARIO ---")
        for i in range(len(codigos)):
            print(f"Cod: {codigos[i]} | Prod: {nombres_perfumes[i]} | Stock: {stock[i]} | Precio: S/ {precios[i]}")
            if stock[i] == 0:
                print("   -> ALERTA: STOCK AGOTADO")

    elif opcion_menu == 3:
        print("\n--- DIRECTORIO DE CLIENTES ---")
        print("1. Agregar nuevo cliente manualmente")
        print("2. Ver lista de clientes")
        sub_opcion = input("Elija sub-opcion: ")
        
        if sub_opcion == '1':
            nombre = input("Nombre del cliente: ")
            telefono = input("Telefono: ")
            nombres_cli.append(nombre)
            telefonos_cli.append(telefono)
            print(">> Cliente guardado exitosamente <<")
        elif sub_opcion == '2':
            if len(nombres_cli) == 0:
                print("No hay clientes registrados aun.")
            else:
                print("LISTA DE CLIENTES RECURRENTES:")
                for i in range(len(nombres_cli)):
                    print(f"{i+1}. {nombres_cli[i]} - Cel: {telefonos_cli[i]}")

    elif opcion_menu == 4:
        print("\n--- AGREGAR NUEVO PERFUME ---")
        nuevo_cod = input("Codigo (Ej. P-004): ")
        nuevo_nom = input("Nombre del perfume: ")
        try:
            nuevo_stock = int(input("Stock inicial: "))
            nuevo_precio = float(input("Precio unitario: "))
            # Usamos .append() para agregar a las listas
            codigos.append(nuevo_cod)
            nombres_perfumes.append(nuevo_nom)
            stock.append(nuevo_stock)
            precios.append(nuevo_precio)
            print(">> Perfume agregado al catalogo <<")
        except ValueError:
            print("Error: El stock y el precio deben ser valores numéricos.")

    elif opcion_menu == 5:
        print("\n--- BUSCAR EN HISTORIAL ---")
        print("1. Buscar por Nombre del Cliente")
        print("2. Buscar por Nombre del Perfume")
        tipo = input("Elija el tipo de busqueda (1 o 2): ")
        termino = input("Escriba el nombre exacto a buscar: ")
        
        encontrado = False
        print("\n>> RESULTADOS DE LA BUSQUEDA <<")
        for i in range(len(historial_cliente)):
            if (tipo == '1' and historial_cliente[i] == termino) or (tipo == '2' and historial_perfume[i] == termino):
                print("-----------------------------------")
                print(f"Comprador: {historial_cliente[i]}")
                print(f"Perfume  : {historial_perfume[i]}")
                print(f"Cantidad : {historial_cantidad[i]}")
                print(f"Costo    : S/ {historial_total[i]}")
                print(f"Fecha    : {historial_fecha[i]}")
                encontrado = True
                
        if not encontrado:
            print("No se encontraron registros de ventas con ese nombre.")
            print("-----------------------------------")

    elif opcion_menu == 6:
        print("Cerrando sistema... ¡Hasta pronto!")
    else:
        print("Opcion no valida. Por favor intente de nuevo.")