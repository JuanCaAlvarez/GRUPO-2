Algoritmo Sistema_Ventas_Perfumes
    // =========================================================
    // VARIABLES GENERALES Y CONFIGURACION DE ARREGLOS
    // =========================================================
    Definir opcion_menu, sub_opcion, i, j, k, indice_perfume, tipo_busqueda Como Entero
    Definir cantidad_solicitada, total_clientes, total_productos, total_ventas Como Entero
    Definir nombre_ingresado, fecha_pedido, nombre_cliente_venta, termino_busqueda Como Caracter
    Definir total_pagar Como Real
    Definir encontrado, venta_encontrada, cliente_existe Como Logico
    
    // ARREGLOS DE INVENTARIO (Capacidad 20)
    Dimension codigos[20]
    Dimension nombres_perfumes[20]
    Dimension stock[20]
    Dimension precios[20]
    
    codigos[1] <- "P-001"
    nombres_perfumes[1] <- "Perfume Floral"
    stock[1] <- 10
    precios[1] <- 150.00
    
    codigos[2] <- "P-002"
    nombres_perfumes[2] <- "Locion Citrus"
    stock[2] <- 5
    precios[2] <- 120.00
    
    codigos[3] <- "P-003"
    nombres_perfumes[3] <- "Extracto Maderas"
    stock[3] <- 0 
    precios[3] <- 200.00
    
    total_productos <- 3 
    
    // ARREGLOS DE CLIENTES RECURRENTES
    Dimension telefonos_cli[10]
    Dimension nombres_cli[10]
    total_clientes <- 0
    
    // =========================================================
    // NUEVOS ARREGLOS: HISTORIAL DE VENTAS (Capacidad 50)
    // =========================================================
    Dimension historial_cliente[50]
    Dimension historial_perfume[50]
    Dimension historial_cantidad[50]
    Dimension historial_total[50]
    Dimension historial_fecha[50]
    total_ventas <- 0
    
    opcion_menu <- 0
    
    // =========================================================
    // BUCLE PRINCIPAL DEL SISTEMA (MENÚ)
    // =========================================================
    Mientras opcion_menu <> 6 Hacer
        Escribir "=========================================="
        Escribir "       SISTEMA DE VENTAS - PERFUMES       "
        Escribir "=========================================="
        Escribir "1. Registrar nueva venta"
        Escribir "2. Ver estado del inventario"
        Escribir "3. Guardar y ver directorio de clientes"
        Escribir "4. Agregar nuevo perfume al catalogo"
        Escribir "5. Buscar en Historial de Ventas"
        Escribir "6. Salir"
        Escribir "=========================================="
        Escribir "Elija una opcion: "
        Leer opcion_menu
        
        Si opcion_menu = 1 Entonces
            // --- RF01: REGISTRAR VENTA (CON GUARDADO AUTOMATICO DE CLIENTE) ---
            Escribir "--- REGISTRAR VENTA ---"
            Escribir "Ingrese fecha de la venta (Ej. 24/06): "
            Leer fecha_pedido
            Escribir "Ingrese el nombre del cliente que compra: "
            Leer nombre_cliente_venta
            
			// --- NUEVO: VERIFICAR SI EL CLIENTE YA EXISTE EN EL DIRECTORIO ---
            cliente_existe <- Falso
            Si total_clientes > 0 Entonces
                Para j <- 1 Hasta total_clientes Hacer
                    Si nombres_cli[j] = nombre_cliente_venta Entonces
                        cliente_existe <- Verdadero
                    Fin Si
                Fin Para
            Fin Si
            
            Si cliente_existe = Falso Entonces
                Escribir ">> Cliente nuevo detectado <<"
                Si total_clientes < 10 Entonces
                    total_clientes <- total_clientes + 1
                    nombres_cli[total_clientes] <- nombre_cliente_venta
                    Escribir "Ingrese el telefono para guardarlo en el directorio de clientes: "
                    Leer telefonos_cli[total_clientes]
                    Escribir ">> Cliente guardado exitosamente en el directorio <<"
                Sino
                    Escribir "ALERTA: El directorio esta lleno, no se guardo el contacto."
                Fin Si
            SiNo
                Escribir ">> Cliente frecuente reconocido <<"
            Fin Si
            Escribir "------------------------------------------"
            
            // --- CONTINUA LA VENTA NORMAL ---
            Escribir "Ingrese el NOMBRE del perfume a vender (Ej. Perfume Floral): "
            Leer nombre_ingresado
            
            encontrado <- Falso
            indice_perfume <- 0
            
            // Buscar el producto por NOMBRE exacto
            Para i <- 1 Hasta total_productos Hacer
                Si nombres_perfumes[i] = nombre_ingresado Entonces
                    encontrado <- Verdadero
                    indice_perfume <- i
                Fin Si
            Fin Para
            
            Si encontrado = Verdadero Entonces
                Escribir "Stock actual: ", stock[indice_perfume]
                Escribir "Ingrese la cantidad solicitada: "
                Leer cantidad_solicitada
                
                Si cantidad_solicitada <= stock[indice_perfume] Entonces
                    // Actualizar inventario
                    stock[indice_perfume] <- stock[indice_perfume] - cantidad_solicitada
                    total_pagar <- cantidad_solicitada * precios[indice_perfume]
                    
                    // GUARDAR EN EL HISTORIAL DE VENTAS
                    total_ventas <- total_ventas + 1
                    historial_cliente[total_ventas] <- nombre_cliente_venta
                    historial_perfume[total_ventas] <- nombres_perfumes[indice_perfume]
                    historial_cantidad[total_ventas] <- cantidad_solicitada
                    historial_total[total_ventas] <- total_pagar
                    historial_fecha[total_ventas] <- fecha_pedido
                    
                    Escribir "=========================================="
                    Escribir "           COMPROBANTE DE VENTA           "
                    Escribir "=========================================="
                    Escribir "Fecha: ", fecha_pedido
                    Escribir "Cliente: ", nombre_cliente_venta
                    Escribir "Producto: ", nombres_perfumes[indice_perfume]
                    Escribir "Cantidad: ", cantidad_solicitada
                    Escribir "Total a pagar: S/ ", total_pagar
                    Escribir "=========================================="
                    Escribir ">> Venta guardada en el historial <<"
                Sino
                    Escribir "ALERTA: Stock insuficiente. Solo quedan ", stock[indice_perfume], " unidades."
                Fin Si
            Sino
                Escribir "ALERTA: El perfume ", nombre_ingresado, " no existe en el catalogo."
            Fin Si
            
        SiNo
            Si opcion_menu = 2 Entonces
                // --- RF04: VER INVENTARIO ---
                Escribir "--- ESTADO DEL INVENTARIO ---"
                Para i <- 1 Hasta total_productos Hacer
                    Escribir "Cod: ", codigos[i], " | Prod: ", nombres_perfumes[i], " | Stock: ", stock[i], " | Precio: S/ ", precios[i]
                Fin Para
                
            SiNo
                Si opcion_menu = 3 Entonces
                    // --- RF05: DIRECTORIO DE CLIENTES ---
                    Escribir "--- DIRECTORIO DE CLIENTES ---"
                    Escribir "1. Agregar nuevo cliente manualmente"
                    Escribir "2. Ver lista de clientes"
                    Leer sub_opcion
                    Si sub_opcion = 1 Entonces
                        Si total_clientes < 10 Entonces
                            total_clientes <- total_clientes + 1
                            Escribir "Nombre del cliente: "
                            Leer nombres_cli[total_clientes]
                            Escribir "Telefono: "
                            Leer telefonos_cli[total_clientes]
                            Escribir ">> Cliente guardado exitosamente <<"
                        Fin Si
                    SiNo
                        Si total_clientes = 0 Entonces
                            Escribir "No hay clientes registrados aun."
                        SiNo
                            Escribir "LISTA DE CLIENTES RECURRENTES:"
                            Para j <- 1 Hasta total_clientes Hacer
                                Escribir j, ". ", nombres_cli[j], " - Cel: ", telefonos_cli[j]
                            Fin Para
                        Fin Si
                    Fin Si
                    
                SiNo
                    Si opcion_menu = 4 Entonces
                        // --- RF06: AGREGAR NUEVO PRODUCTO ---
                        Escribir "--- AGREGAR NUEVO PERFUME ---"
                        Si total_productos < 20 Entonces
                            total_productos <- total_productos + 1 
                            Escribir "Codigo (Ej. P-004): "
                            Leer codigos[total_productos]
                            Escribir "Nombre del perfume: "
                            Leer nombres_perfumes[total_productos]
                            Escribir "Stock inicial: "
                            Leer stock[total_productos]
                            Escribir "Precio unitario: "
                            Leer precios[total_productos]
                            Escribir ">> Perfume agregado al catalogo <<"
                        Fin Si
                        
                    SiNo
                        Si opcion_menu = 5 Entonces
                            // --- RF07: BUSCAR EN HISTORIAL DE VENTAS ---
                            Escribir "--- BUSCAR EN HISTORIAL ---"
                            Escribir "1. Buscar por Nombre del Cliente"
                            Escribir "2. Buscar por Nombre del Perfume"
                            Escribir "Elija el tipo de busqueda (1 o 2): "
                            Leer tipo_busqueda
                            
                            Escribir "Escriba el nombre exacto a buscar:"
                            Leer termino_busqueda
                            
                            venta_encontrada <- Falso
                            Escribir ""
                            Escribir ">> RESULTADOS DE LA BUSQUEDA <<"
                            
                            Para k <- 1 Hasta total_ventas Hacer
                                Si (tipo_busqueda = 1 Y historial_cliente[k] = termino_busqueda) O (tipo_busqueda = 2 Y historial_perfume[k] = termino_busqueda) Entonces
                                    Escribir "-----------------------------------"
                                    Escribir "Comprador: ", historial_cliente[k]
                                    Escribir "Perfume  : ", historial_perfume[k]
                                    Escribir "Cantidad : ", historial_cantidad[k]
                                    Escribir "Costo    : S/ ", historial_total[k]
                                    Escribir "Fecha    : ", historial_fecha[k]
                                    venta_encontrada <- Verdadero
                                Fin Si
                            Fin Para
                            
                            Si venta_encontrada = Falso Entonces
                                Escribir "No se encontraron registros de ventas con ese nombre."
                                Escribir "-----------------------------------"
                            Fin Si
                            
                        SiNo
                            Si opcion_menu = 6 Entonces
                                Escribir "Cerrando sistema..."
                            Fin Si
                        Fin Si
                    Fin Si
                Fin Si
            Fin Si
        Fin Si
        Escribir "" 
    Fin Mientras
FinAlgoritmo