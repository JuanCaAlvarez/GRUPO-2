import os
import json
from datetime import datetime

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

def buscar_perfume(texto):
    palabras = texto.lower().split()

    for i in range(len(nombres_perfumes)):
        nombre = nombres_perfumes[i].lower()

        if all(palabra in nombre for palabra in palabras):
            return i

    return -1

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
    codigos = [
    "P-001","P-002","P-003","P-004","P-005","P-006","P-007","P-008","P-009","P-010", "P-011","P-012","P-013","P-014","P-015","P-016","P-017","P-018","P-019","P-020",
    "P-021","P-022","P-023","P-024","P-025","P-026","P-027","P-028","P-029","P-030","P-031","P-032","P-033","P-034","P-035","P-036","P-037","P-038","P-039","P-040",
    "P-041","P-042","P-043","P-044","P-045","P-046","P-047","P-048","P-049","P-050"
    ]
    nombres_perfumes = [
    "Stronger With You Intensely","Valentino Uomo Born In Roma Intense","Erba Pura","Bleu de Chanel EDP","Dior Homme Intense","Y EDP","La Nuit de L'Homme","Le Beau Le Parfum",
    "Scandal Le Parfum","Invictus Victory Elixir","One Million Elixir","Prada Luna Rossa Carbon","Eros Flame","Acqua di Gio Parfum","Armani Code EDT","The Most Wanted",
    "Club de Nuit Intense Man","Cedrat Boise","Instant Crush","Red Tobacco","Naxos","Alexandria II","Torino 21","Layton","Ombré Leather","Costa Azzurra Parfum",
    "Spicebomb Extreme","L'Homme Ideal L'Intense","Boss Bottled Infinite","Montblanc Explorer EDP","Light Blue Pour Homme","Toy Boy","Bad Boy Cobalt Elixir","Gentleman Reserve Privée",
    "Silver Mountain Water","Ani","Hacivat","Odyssey Aqua","Mandarin Sky","Fakhar Black","Game of Spades Full-House","Hawas Kobra","Summer Hammer","Khamrah","God of Fire",
    "Percival","Arabians Tonka","Imagination","Pacific Chill","9pm Night Out"
    ]
    stock = [
    10, 5, 0, 2, 8, 6, 4, 7, 3, 9, 5, 4, 6, 2, 8, 1, 10, 7, 5, 3, 6, 4, 9, 2, 8, 5, 7, 3, 10, 4, 6, 5, 2, 9, 8, 1, 7, 3, 5, 6, 4, 10, 2, 8, 5, 7, 1, 9, 3, 6
    ]
    precios = [
    420.0, 520.0, 200.0, 840.0, 690.0,480.0, 450.0, 390.0, 510.0, 430.0,470.0, 360.0, 350.0, 560.0, 610.0,240.0, 190.0, 330.0, 680.0, 370.0,310.0, 400.0, 260.0, 590.0,
    730.0, 280.0, 650.0, 300.0, 410.0, 340.0, 490.0, 380.0, 540.0, 720.0, 460.0, 520.0, 270.0, 350.0, 620.0, 440.0, 580.0, 760.0, 320.0, 680.0, 430.0, 390.0, 250.0,
    810.0, 950.0, 600.0
    ]
    nombres_cli = [
    "Ana","Luis","María","Carlos","Sofía","Diego","Valeria","Jorge","Camila","José","Daniela","Kevin","Lucía","Fernando","Andrea","Ricardo","Paola","Miguel","Brenda",
    "Javier","Gabriela","Cristian","Natalia","Eduardo","Patricia","Alonso","Fernanda","Renzo","Milagros","Ángel","Karen","Melissa","Jean","Rosa","Erick","Claudia",
    "Marco","Fiorella","Víctor","Estefanía","Hugo","Carolina","Sebastián","Noelia","Óscar","Tatiana","Adrián","Nicole","Brayan","Valentina"
    ]
    dni_cli = [
    "70345128","71456239","72567340","73678451","74789562","75890673","76901784","77012895","78123906","79234017","70345189","71456290","72567301","73678412","74789523",
    "75890634","76901745","77012856","78123967","79234078","70345190","71456321","72567432","73678543","74789654","75890765","76901876","77012987","78123098","79234109",
    "70345210","71456342","72567453","73678564","74789675","75890786","76901897","77012018","78123129","79234230","70345341","71456452","72567563","73678674","74789785",
    "75890896","76901907","77012039","78123140","79234251"
    ]
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
    
    try:
        opcion_menu = int(input("Elija una opcion: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        continue

    if opcion_menu == 1:
        print("\n--- REGISTRAR VENTA ---")
        cancelar = False 
        
        fecha_pedido = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Fecha y hora de registro: {fecha_pedido}")

        while True:
            dni_ingresado = input("Ingrese DNI del cliente (o 'salir' para cancelar): ")
            if dni_ingresado.lower() == 'salir':
                cancelar = True
                break
            if (len(dni_ingresado) == 8 or len(dni_ingresado) == 12) and dni_ingresado.isdigit():
                break
            else:
                print("ERROR: El documento debe tener 8 o 12 digitos numéricos.")
        
        if cancelar: continue 
        
        cliente_existe = False
        nombre_cliente = ""

        for i in range(len(dni_cli)):
            if dni_cli[i] == dni_ingresado:
                cliente_existe = True
                nombre_cliente = nombres_cli[i]

        if not cliente_existe:
            print(">> Cliente nuevo detectado <<")
            while True:
                nombre_cliente = input("Ingrese nombre del cliente (o 'salir'): ")
                if nombre_cliente.lower() == 'salir':
                    cancelar = True
                    break
                if nombre_cliente.strip() != "":
                    break
                print("ERROR: El nombre no puede estar vacío.")
            
            if cancelar: continue
            
            print(">> Datos del cliente temporalmente listos. Se guardarán al concretar la venta. <<")
        else:
            print(">> Cliente frecuente reconocido <<")
            
        print("\n" + "=" * 50)
        print("CATALOGO DISPONIBLE")
        print("=" * 50)
        for i in range(len(nombres_perfumes)):
            print(f"[{codigos[i]}] {nombres_perfumes[i]} | Stock: {stock[i]} | Precio: S/ {precios[i]}")
        print("=" * 50)
        
        encontrado = False
        indice = -1

        while not encontrado:
            termino_busqueda = input("Ingrese el CÓDIGO o NOMBRE del perfume a vender (o 'salir'): ")

            if termino_busqueda.lower() == 'salir':
                cancelar = True
                break

                indice = -1

            # Primero busca por código
            for i in range(len(codigos)):
                if codigos[i].lower() == termino_busqueda.lower():
                    indice = i
                    break

            # Si no encontró por código, busca por nombre parcial
            if indice == -1:
                indice = buscar_perfume(termino_busqueda)

            if indice == -1:
                print(f"ALERTA: El producto '{termino_busqueda}' no existe en el catálogo. Intente nuevamente.")

            elif stock[indice] == 0:
                print(f"ALERTA: El perfume '{nombres_perfumes[indice]}' está AGOTADO (Stock: 0). Elija otro o escriba 'salir'.")

            else:
                print(f">> Perfume encontrado: [{codigos[indice]}] {nombres_perfumes[indice]}")
                encontrado = True
        
        if cancelar: continue
        
        if encontrado:
            while True:
                entrada_cant = input(f"Ingrese la cantidad solicitada (Stock disponible: {stock[indice]}) o 'salir': ")
                if entrada_cant.lower() == 'salir':
                    cancelar = True
                    break
                    
                try:
                    cantidad = int(entrada_cant)
                    if cantidad <= 0:
                        print("Error: La cantidad debe ser mayor a 0.")
                    elif cantidad > stock[indice]:
                        print(f"ALERTA: Stock insuficiente. Solo quedan {stock[indice]} unidades.")
                    else:
                        break 
                except ValueError:
                    print("Error: Ingrese un valor numérico para la cantidad.")
            
            if cancelar: continue
                
            stock[indice] -= cantidad
            total = cantidad * precios[indice]
            
            historial_cliente.append(nombre_cliente)
            historial_dni.append(dni_ingresado)
            historial_perfume.append(nombres_perfumes[indice])
            historial_cantidad.append(cantidad)
            historial_total.append(total)
            historial_fecha.append(fecha_pedido)
            
            if not cliente_existe:
                dni_cli.append(dni_ingresado)
                nombres_cli.append(nombre_cliente)
                print("\n>> Cliente guardado exitosamente en el directorio <<")

            guardar_datos() 
            
            print("=" * 50)
            print("========== COMPROBANTE DE VENTA ==========")
            print("=" * 50)
            print(f"Fecha: {fecha_pedido}")
            print(f"Cliente: {nombre_cliente}")
            print(f"DNI: {dni_ingresado}")
            print(f"Producto: [{codigos[indice]}] {nombres_perfumes[indice]}")
            print(f"Cantidad: {cantidad}")
            print(f"Total a pagar: S/ {total}")
            print("==========================================")
            print(">> Venta guardada en el historial <<")

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
        sub_opcion = input("Elija sub-opcion (o 'salir' para cancelar): ")

        if sub_opcion.lower() == 'salir':
            continue

        if sub_opcion == '1':
            cancelar = False
            nombre = input("Nombre del cliente (o 'salir'): ")
            if nombre.lower() == 'salir': continue

            while True:
                dni = input("DNI o Carnet de Extranjeria (o 'salir'): ")
                if dni.lower() == 'salir':
                    cancelar = True
                    break
                if (len(dni) == 8 or len(dni) == 12) and dni.isdigit():
                    break
                print("ERROR: El documento debe tener 8 o 12 digitos numericos.")
                
            if cancelar: continue

            if dni not in dni_cli:
                nombres_cli.append(nombre)
                dni_cli.append(dni)
                guardar_datos() 
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
        cancelar = False
        
        # --- LÓGICA DE AUTO-INCREMENTO DEL CÓDIGO ---
        if len(codigos) == 0:
            siguiente_numero = 1
        else:
            max_num = 0
            for c in codigos:
                # Partimos el código por el guión (ej: ["P", "005"])
                partes = c.split('-')
                if len(partes) == 2 and partes[1].isdigit():
                    num = int(partes[1])
                    if num > max_num:
                        max_num = num
            # Le sumamos 1 al número más alto encontrado
            siguiente_numero = max_num + 1
            
        # Formateamos el nuevo código para que tenga ceros a la izquierda (ej: P-009)
        nuevo_cod = f"P-{siguiente_numero:03d}"
        
        print(f"[*] Se generará automáticamente el código: {nuevo_cod}")
        
        while True:
            nuevo_nom = input("Nombre del perfume (o 'salir'): ")

            if nuevo_nom.lower() == 'salir':
                cancelar = True
                break

            if nuevo_nom.strip() == "":
                print("Error: El nombre no puede estar vacío.")
                continue

            # Verificar que no exista otro perfume con el mismo nombre
            duplicado = False

            for perfume in nombres_perfumes:
                if perfume.lower() == nuevo_nom.lower():
                    duplicado = True
                    break

            if duplicado:
                print("⚠ Error: Ya existe un perfume con ese nombre.")
                continue
            break

        if cancelar: continue

        while True:
            entrada_stock = input("Stock inicial (o 'salir'): ")
            if entrada_stock.lower() == 'salir':
                cancelar = True
                break
                
            entrada_precio = input("Precio unitario (o 'salir'): ")
            if entrada_precio.lower() == 'salir':
                cancelar = True
                break
                
            try:
                nuevo_stock = int(entrada_stock)
                nuevo_precio = float(entrada_precio)
                
                if nuevo_stock >= 0 and nuevo_precio > 0:
                    break
                else:
                    print("Error: El stock no puede ser negativo y el precio debe ser mayor a cero.")
            except ValueError:
                print("Error: El stock y el precio deben ser valores numéricos.")
        
        if cancelar: continue
            
        codigos.append(nuevo_cod)
        nombres_perfumes.append(nuevo_nom)
        stock.append(nuevo_stock)
        precios.append(nuevo_precio)
        
        guardar_datos() 
        print(f">> Perfume '{nuevo_nom}' agregado al catalogo exitosamente con el código [{nuevo_cod}] <<")

    elif opcion_menu == 5:
        print("\n--- BUSCAR EN HISTORIAL ---")
        print("1. Buscar por DNI del Cliente")
        print("2. Buscar por Código o Nombre del Perfume")

        tipo = input("Elija el tipo de busqueda (1 o 2) o 'salir': ")
        if tipo.lower() == 'salir': continue
        
        if tipo in ['1', '2']:
            encontrado = False
            cancelar = False
            
            while not encontrado:
                termino = input("Ingrese los datos correspondientes (o 'salir' para cancelar): ")
                
                if termino.lower() == 'salir':
                    cancelar = True
                    break 
                
                termino_perfume = termino.lower()
                if tipo == '2':
                    for c in range(len(codigos)):
                        if codigos[c].lower() == termino.lower():
                            termino_perfume = nombres_perfumes[c].lower()
                            break

                print("\n>> RESULTADOS DE LA BUSQUEDA <<")

                for i in range(len(historial_cliente)):
                    if (tipo == '1' and historial_dni[i] == termino) or \
                       (tipo == '2' and historial_perfume[i].lower() == termino_perfume):

                        print("-----------------------------------")
                        print(f"Comprador: {historial_cliente[i]}")
                        print(f"DNI      : {historial_dni[i]}")
                        print(f"Perfume  : {historial_perfume[i]}")
                        print(f"Cantidad : {historial_cantidad[i]}")
                        print(f"Costo    : S/ {historial_total[i]}")
                        print(f"Fecha    : {historial_fecha[i]}")

                        encontrado = True

                if not encontrado:
                    print("No se encontraron registros de ventas con ese dato. Inténtelo de nuevo.")
            
            if cancelar: continue
                    
        else:
            print("Opción de búsqueda no válida.")

    elif opcion_menu == 6:
        print("\n--- AÑADIR STOCK ---")
        cancelar = False
        
        print("\n" + "=" * 50)
        print("CATALOGO DISPONIBLE")
        print("=" * 50)
        for i in range(len(codigos)):
            print(f"[{codigos[i]}] {nombres_perfumes[i]} | Stock: {stock[i]} | Precio: S/ {precios[i]}")
        print("=" * 50)

        encontrado = False
        indice = -1
        
        while not encontrado:
            termino_busqueda = input("Ingrese el CÓDIGO o NOMBRE del perfume a recargar (o 'salir'): ")
            
            if termino_busqueda.lower() == 'salir':
                cancelar = True
                break
                
            for i in range(len(nombres_perfumes)):
                if nombres_perfumes[i].lower() == termino_busqueda.lower() or codigos[i].lower() == termino_busqueda.lower():
                    encontrado = True
                    indice = i
                    break
            
            if not encontrado:
                print("ALERTA: El producto no existe en el catálogo. Intente de nuevo.")
                
        if cancelar: continue
                
        if encontrado:
            print(f"Producto encontrado: [{codigos[indice]}] {nombres_perfumes[indice]} | Stock actual: {stock[indice]}")
            
            while True:
                entrada_agregar = input("Ingrese la cantidad de stock a añadir (o 'salir'): ")
                if entrada_agregar.lower() == 'salir':
                    cancelar = True
                    break
                    
                try:
                    cantidad_agregar = int(entrada_agregar)
                    if cantidad_agregar > 0:
                        stock[indice] += cantidad_agregar 
                        guardar_datos() 
                        print(f">> Stock actualizado exitosamente. Nuevo stock: {stock[indice]} <<")
                        break
                    else:
                        print("Error: La cantidad a añadir debe ser mayor a cero.")
                except ValueError:
                    print("Error: Ingrese un valor numérico válido.")
            
            if cancelar: continue

    elif opcion_menu == 7:
        guardar_datos() 
        print("Cerrando sistema... ¡Hasta pronto!")
        
    else:
        print("Opcion no valida. Por favor intente de nuevo.")