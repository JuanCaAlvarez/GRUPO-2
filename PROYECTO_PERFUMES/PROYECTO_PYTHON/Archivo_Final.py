import os
import json

# =========================================================
# SISTEMA DE VENTAS - PERFUMES (VERSIÓN PYTHON FINAL)
# =========================================================

# 1. Configurar el "Base Dir" (Busca automáticamente la carpeta de tu script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(BASE_DIR, "datos_sistema.json")

# 2. Función para guardar todos los datos en el archivo
def guardar_datos():
    datos_completos = {
        "codigos": codigos,
        "nombres_perfumes": nombres_perfumes,
        "stock": stock,
        "precios": precios,
        "nombres_cli": nombres_cli,
        "dni_cli": dni_cli,
        "historial_cliente": historial_cliente,
        "historial_dni": historial_dni,
        "historial_perfume": historial_perfume,
        "historial_cantidad": historial_cantidad,
        "historial_total": historial_total,
        "historial_fecha": historial_fecha
    }
    with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
        json.dump(datos_completos, archivo, indent=4)

# 3. Intentar cargar los datos si el archivo existe
if os.path.exists(ARCHIVO_DATOS):
    with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
        datos_cargados = json.load(archivo)
        
        codigos = datos_cargados.get("codigos", [])
        nombres_perfumes = datos_cargados.get("nombres_perfumes", [])
        stock = datos_cargados.get("stock", [])
        precios = datos_cargados.get("precios", [])
        
        nombres_cli = datos_cargados.get("nombres_cli", [])
        dni_cli = datos_cargados.get("dni_cli", [])
        
        historial_cliente = datos_cargados.get("historial_cliente", [])
        historial_dni = datos_cargados.get("historial_dni", [])
        historial_perfume = datos_cargados.get("historial_perfume", [])
        historial_cantidad = datos_cargados.get("historial_cantidad", [])
        historial_total = datos_cargados.get("historial_total", [])
        historial_fecha = datos_cargados.get("historial_fecha", [])
else:
    # Si el archivo NO existe, carga los datos por defecto iniciales
    codigos = ["P-001", "P-002", "P-003", "P-004"]
    nombres_perfumes = ["Stronger with You Intensely", "Valentino Uomo Born In Roma Intense", "Sauvage EDT", "Erba Pura"]
    stock = [10, 5, 0, 2]
    precios = [420.0, 520.0, 200.0, 840.0]

    nombres_cli = []
    dni_cli = []

    historial_cliente = []
    historial_dni = []
    historial_perfume = []
    historial_cantidad = []
    historial_total = []
    historial_fecha = []

opcion_menu = 0

# BUCLE PRINCIPAL DEL SISTEMA
while opcion_menu != 7:
    print("\n" + "=" * 50)
    print("========== SISTEMA DE VENTAS - PERFUMES ==========")
    print("=" * 50)
    print("1. Registrar nueva venta")
    print("2. Ver estado del inventario")
    print("3. Guardar y ver directorio de clientes")
    print("4. Agregar nuevo perfume al catalogo")
    print("5. Buscar en Historial de Ventas")
    print("6. Añadir stock a un perfume existente")
    print("7. Salir")
    print("=" * 50)
    
    # Validación de entrada para evitar que el programa colapse si ingresan letras
    try:
        opcion_menu = int(input("Elija una opcion: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        continue

    if opcion_menu == 1:
        print("\n--- REGISTRAR VENTA ---")
        fecha_pedido = input("Ingrese fecha de la venta (Ej. 24/06): ")
        dni_ingresado = input("Ingrese DNI del cliente: ")

        while (len(dni_ingresado) != 8 and len(dni_ingresado) != 12) or not dni_ingresado.isdigit():
            print("ERROR: El documento debe tener 8 o 12 digitos numéricos")
            dni_ingresado = input("Ingrese nuevamente el documento: ")
        
        # Guardado automático de cliente
        cliente_existe = False
        nombre_cliente = ""

        for i in range(len(dni_cli)):
            if dni_cli[i] == dni_ingresado:
                cliente_existe = True
                nombre_cliente = nombres_cli[i]

        if not cliente_existe:
            print(">> Cliente nuevo detectado <<")
            nombre_cliente = input("Ingrese nombre del cliente: ")
            dni_cli.append(dni_ingresado)
            nombres_cli.append(nombre_cliente)
            guardar_datos() # Se guarda el nuevo cliente inmediatamente
            print(">> Cliente guardado exitosamente en el directorio <<")
        else:
            print(">> Cliente frecuente reconocido <<")
            
        print("=" * 50)
        print("CATALOGO DISPONIBLE")
        print("=" * 50)

        for i in range(len(nombres_perfumes)):
            print(f"{i+1}. {nombres_perfumes[i]} | Stock: {stock[i]} | Precio: S/ {precios[i]}")

        print("=" * 50)
        nombre_perfume = input("Ingrese el NOMBRE del perfume a vender: ")
        
        # Búsqueda en el inventario
        encontrado = False
        indice = -1

        for i in range(len(nombres_perfumes)):
            if nombres_perfumes[i].lower() == nombre_perfume.lower():
                encontrado = True
                indice = i
        
        if encontrado:
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
                historial_dni.append(dni_ingresado)
                historial_perfume.append(nombres_perfumes[indice])
                historial_cantidad.append(cantidad)
                historial_total.append(total)
                historial_fecha.append(fecha_pedido)
                
                guardar_datos() # Se guardan los cambios de stock y el nuevo historial
                
                print("=" * 50)
                print("========== COMPROBANTE DE VENTA ==========")
                print("=" * 50)
                print(f"Fecha: {fecha_pedido}")
                print(f"Cliente: {nombre_cliente}")
                print(f"DNI: {dni_ingresado}")
                print(f"Producto: {nombres_perfumes[indice]}")
                print(f"Cantidad: {cantidad}")
                print(f"Total a pagar: S/ {total}")
                print("==========================================")
                print(">> Venta guardada en el historial <<")
            else:
                print(f"ALERTA: Stock insuficiente. Solo quedan {stock[indice]} unidades.")
        else:
            print(f"ALERTA: El perfume '{nombre_perfume}' no existe en el catalogo.")

    elif opcion_menu == 2:
        print("\n=============  ESTADO DEL INVENTARIO =============")
        for i in range(len(codigos)):
            print(f"Cod: {codigos[i]} | Prod: {nombres_perfumes[i]} | Stock: {stock[i]} | Precio: S/ {precios[i]}")
            if stock[i] == 0:
                print("   -> ALERTA: STOCK AGOTADO")

    elif opcion_menu == 3:
        print("\n====== DIRECTORIO DE CLIENTES ======")
        print("1. Agregar nuevo cliente manualmente")
        print("2. Ver lista de clientes")
        sub_opcion = input("Elija sub-opcion: ")

        if sub_opcion == '1':
            nombre = input("Nombre del cliente: ")
            dni = input("DNI o Carnet de Extranjeria: ")

            while (len(dni) != 8 and len(dni) != 12) or not dni.isdigit():
                print("ERROR: El documento debe tener 8 o 12 digitos numericos.")
                dni = input("Ingrese nuevamente el documento: ")

            if dni not in dni_cli:
                nombres_cli.append(nombre)
                dni_cli.append(dni)
                guardar_datos() # Se guarda el cliente agregado manualmente
                print(">> Cliente guardado exitosamente <<")
            else:
                print("ERROR: Ya existe un cliente registrado con ese DNI.")

        elif sub_opcion == '2':
            if len(nombres_cli) == 0:
                print("No hay clientes registrados aun.")
            else:
                print("LISTA DE CLIENTES RECURRENTES:")
                for i in range(len(nombres_cli)):
                    print(f"{i+1}. {nombres_cli[i]} - DNI: {dni_cli[i]}")

    elif opcion_menu == 4:
        print("\n--- AGREGAR NUEVO PERFUME ---")
        nuevo_cod = input("Codigo (Ej. P-004): ")
        nuevo_nom = input("Nombre del perfume: ")
        try:
            nuevo_stock = int(input("Stock inicial: "))
            nuevo_precio = float(input("Precio unitario: "))
            
            codigos.append(nuevo_cod)
            nombres_perfumes.append(nuevo_nom)
            stock.append(nuevo_stock)
            precios.append(nuevo_precio)
            
            guardar_datos() # Se guarda el nuevo perfume en el catálogo
            print(">> Perfume agregado al catalogo <<")
        except ValueError:
            print("Error: El stock y el precio deben ser valores numéricos.")

    elif opcion_menu == 5:
        print("\n--- BUSCAR EN HISTORIAL ---")
        print("1. Buscar por DNI del Cliente")
        print("2. Buscar por Nombre del Perfume")

        tipo = input("Elija el tipo de busqueda (1 o 2): ")
        termino = input("Ingrese los datos correspondientes: ")

        encontrado = False

        print("\n>> RESULTADOS DE LA BUSQUEDA <<")

        for i in range(len(historial_cliente)):
            if (tipo == '1' and historial_dni[i] == termino) or \
               (tipo == '2' and historial_perfume[i].lower() == termino.lower()):

                print("-----------------------------------")
                print(f"Comprador: {historial_cliente[i]}")
                print(f"DNI      : {historial_dni[i]}")
                print(f"Perfume  : {historial_perfume[i]}")
                print(f"Cantidad : {historial_cantidad[i]}")
                print(f"Costo    : S/ {historial_total[i]}")
                print(f"Fecha    : {historial_fecha[i]}")

                encontrado = True

        if not encontrado:
            print("No se encontraron registros de ventas.")
            print("-----------------------------------")

    elif opcion_menu == 6:
        print("\n--- AÑADIR STOCK ---")
        nombre_buscar = input("Ingrese el nombre exacto del perfume a recargar: ")
        
        encontrado = False
        
        for i in range(len(nombres_perfumes)):
            if nombres_perfumes[i].lower() == nombre_buscar.lower():
                encontrado = True
                print(f"Producto encontrado: {nombres_perfumes[i]} | Stock actual: {stock[i]}")
                
                try:
                    cantidad_agregar = int(input("Ingrese la nueva cantidad de stock: "))
                    
                    if cantidad_agregar > 0:
                        stock[i] += cantidad_agregar 
                        guardar_datos() # Se guarda el cambio en el archivo JSON
                        print(f">> Stock actualizado exitosamente. Nuevo stock: {stock[i]} <<")
                    else:
                        print("Error: La cantidad a añadir debe ser mayor a cero.")
                        
                except ValueError:
                    print("Error: Ingrese un valor numérico válido.")
                break 
                
        if not encontrado:
            print("ALERTA: El perfume no existe en el catálogo. Utilice la Opción 4 para registrar un producto nuevo.")

    elif opcion_menu == 7:
        guardar_datos() # Respaldo final antes de cerrar
        print("Cerrando sistema... ¡Hasta pronto!")
        
    else:
        print("Opcion no valida. Por favor intente de nuevo.")