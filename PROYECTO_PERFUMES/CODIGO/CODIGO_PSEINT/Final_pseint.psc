Algoritmo Sistema_Ventas_Perfumes_Mejorado
	// =========================================================
	// VARIABLES GENERALES Y CONTADORES
	// =========================================================
	Definir opcion_menu, sub_opcion, i, indice, cantidad, num_val, max_num, siguiente_numero Como Entero
	Definir total_productos, total_clientes, total_ventas Como Entero
	Definir fecha_pedido, dni_ingresado, nombre_cliente, termino_busqueda, entrada_texto, nuevo_cod, nuevo_nom Como Cadena
	Definir total, nuevo_precio, nuevo_stock Como Real
	Definir cancelar, cliente_existe, encontrado, perfume_existe, duplicado Como Lógico
	// ARREGLOS DE INVENTARIO (Capacidad 100)
	Dimensionar codigos(100), nombres_perfumes(100), stock(100), precios(100)
	// ARREGLOS DE CLIENTES (Capacidad 100)
	Dimensionar nombres_cli(100), dni_cli(100)
	// ARREGLOS DE HISTORIAL (Capacidad 200)
	Dimensionar historial_cliente(200), historial_dni(200), historial_perfume(200), historial_fecha(200)
	Dimensionar historial_cantidad(200), historial_total(200)
	// CARGA DE DATOS POR DEFECTO
	codigos[1] <- 'P-001'
	nombres_perfumes[1] <- 'Stronger with You Intensely'
	stock[1] <- 10
	precios[1] <- 420.0
	codigos[2] <- 'P-002'
	nombres_perfumes[2] <- 'Valentino Uomo Born In Roma Intense'
	stock[2] <- 5
	precios[2] <- 520.0
	codigos[3] <- 'P-003'
	nombres_perfumes[3] <- 'Sauvage EDT'
	stock[3] <- 0
	precios[3] <- 200.0
	codigos[4] <- 'P-004'
	nombres_perfumes[4] <- 'Erba Pura'
	stock[4] <- 2
	precios[4] <- 840.0
	total_productos <- 4
	total_clientes <- 0
	total_ventas <- 0
	opcion_menu <- 0
	// =========================================================
	// BUCLE PRINCIPAL DEL SISTEMA (MENÚ)
	// =========================================================
	Mientras opcion_menu<>7 Hacer
		Escribir ''
		Escribir '=================================================='
		Escribir '========== SISTEMA DE VENTAS - PERFUMES =========='
		Escribir '=================================================='
		Escribir '1. Registrar nueva venta'
		Escribir '2. Ver estado del inventario'
		Escribir '3. Guardar y ver directorio de clientes'
		Escribir '4. Agregar nuevo perfume al catalogo'
		Escribir '5. Buscar en Historial de Ventas'
		Escribir '6. Añadir stock a un perfume existente'
		Escribir '7. Salir'
		Escribir '=================================================='
		Escribir 'Elija una opcion: '
		Leer opcion_menu
		Según opcion_menu Hacer
			1:
				Escribir ''
				Escribir '--- REGISTRAR VENTA ---'
				cancelar <- Falso
				fecha_pedido <- '07/07/2026'
				// VALIDACION DE DNI
				Repetir
					Escribir 'Ingrese DNI del cliente (8 o 12 digitos, o escriba salir): '
					Leer dni_ingresado
					Si Minusculas(dni_ingresado)='salir' Entonces
						cancelar <- Verdadero
					SiNo
						Si Longitud(dni_ingresado)<>8 Y Longitud(dni_ingresado)<>12 Entonces
							Escribir 'ERROR: El documento debe tener 8 o 12 digitos.'
						FinSi
					FinSi
				Hasta Que cancelar=Verdadero O Longitud(dni_ingresado)=8 O Longitud(dni_ingresado)=12
				Si  NO cancelar Entonces
					cliente_existe <- Falso
					nombre_cliente <- ''
					Si total_clientes>0 Entonces
						Para i<-1 Hasta total_clientes Hacer
							Si dni_cli[i]=dni_ingresado Entonces
								cliente_existe <- Verdadero
								nombre_cliente <- nombres_cli[i]
							FinSi
						FinPara
					FinSi
					Si cliente_existe=Falso Entonces
						Escribir '>> Cliente nuevo detectado <<'
						Repetir
							Escribir 'Ingrese nombre del cliente (o escriba salir): '
							Leer nombre_cliente
							Si Minusculas(nombre_cliente)='salir' Entonces
								cancelar <- Verdadero
							FinSi
						Hasta Que cancelar=Verdadero O nombre_cliente<>''
					SiNo
						Escribir '>> Cliente frecuente reconocido <<'
					FinSi
				FinSi
				Si  NO cancelar Entonces
					Escribir ''
					Escribir '=================================================='
					Escribir 'CATALOGO DISPONIBLE'
					Escribir '=================================================='
					Para i<-1 Hasta total_productos Hacer
						Escribir '[', codigos[i], '] ', nombres_perfumes[i], ' | Stock: ', stock[i], ' | Precio: S/ ', precios[i]
					FinPara
					Escribir '=================================================='
					encontrado <- Falso
					indice <- -1
					Repetir
						Escribir 'Ingrese el CODIGO o NOMBRE del perfume a vender (o escriba salir): '
						Leer termino_busqueda
						Si Minusculas(termino_busqueda)='salir' Entonces
							cancelar <- Verdadero
						SiNo
							perfume_existe <- Falso
							Para i<-1 Hasta total_productos Hacer
								Si Minusculas(codigos[i])=Minusculas(termino_busqueda) Entonces
									perfume_existe <- Verdadero
									indice <- i
								SiNo
									Si Longitud(termino_busqueda)<=Longitud(nombres_perfumes[i]) Entonces
										Si Minusculas(Subcadena(nombres_perfumes[i],1,Longitud(termino_busqueda)))=Minusculas(termino_busqueda) Entonces
											perfume_existe <- Verdadero
											indice <- i
											Escribir '>> Perfume encontrado: [', codigos[indice], '] ', nombres_perfumes[indice]
										FinSi
									FinSi
								FinSi
							FinPara
							Si  NO perfume_existe Entonces
								Escribir 'ALERTA: El producto no existe en el catalogo.'
							SiNo
								Si stock[indice]=0 Entonces
									Escribir 'ALERTA: El perfume ', nombres_perfumes[indice], ' esta AGOTADO (Stock: 0).'
								SiNo
									encontrado <- Verdadero
								FinSi
							FinSi
						FinSi
					Hasta Que cancelar=Verdadero O encontrado=Verdadero
				FinSi
				Si  NO cancelar Entonces
					Repetir
						Escribir 'Ingrese la cantidad solicitada (Stock: ', stock[indice], ') o 0 para salir: '
						Leer cantidad
						Si cantidad=0 Entonces
							cancelar <- Verdadero
						SiNo
							Si cantidad<0 Entonces
								Escribir 'Error: La cantidad debe ser mayor a 0.'
							SiNo
								Si cantidad>stock[indice] Entonces
									Escribir 'ALERTA: Stock insuficiente. Solo quedan ', stock[indice], ' unidades.'
								FinSi
							FinSi
						FinSi
					Hasta Que cancelar=Verdadero O (cantidad>0 Y cantidad<=stock[indice])
				FinSi
				Si  NO cancelar Entonces
					stock[indice] <- stock[indice]-cantidad
					total <- cantidad*precios[indice]
					total_ventas <- total_ventas+1
					historial_cliente[total_ventas] <- nombre_cliente
					historial_dni[total_ventas] <- dni_ingresado
					historial_perfume[total_ventas] <- nombres_perfumes[indice]
					historial_cantidad[total_ventas] <- cantidad
					historial_total[total_ventas] <- total
					historial_fecha[total_ventas] <- fecha_pedido
					Si cliente_existe=Falso Entonces
						total_clientes <- total_clientes+1
						dni_cli[total_clientes] <- dni_ingresado
						nombres_cli[total_clientes] <- nombre_cliente
						Escribir '>> Cliente guardado exitosamente en el directorio <<'
					FinSi
					Escribir '=================================================='
					Escribir '========== COMPROBANTE DE VENTA =========='
					Escribir '=================================================='
					Escribir 'Fecha: ', fecha_pedido
					Escribir 'Cliente: ', nombre_cliente
					Escribir 'DNI: ', dni_ingresado
					Escribir 'Producto: [', codigos[indice], '] ', nombres_perfumes[indice]
					Escribir 'Cantidad: ', cantidad
					Escribir 'Total a pagar: S/ ', total
					Escribir '=================================================='
					Escribir '>> Venta guardada en el historial <<'
				FinSi
			2:
				Escribir ''
				Escribir '=============  ESTADO DEL INVENTARIO ============='
				Para i<-1 Hasta total_productos Hacer
					Escribir 'Cod: ', codigos[i], ' | Prod: ', nombres_perfumes[i], ' | Stock: ', stock[i], ' | Precio: S/ ', precios[i]
					Si stock[i]=0 Entonces
						Escribir '   -> ALERTA: STOCK AGOTADO'
					FinSi
				FinPara
			3:
				Escribir ''
				Escribir '====== DIRECTORIO DE CLIENTES ======'
				Escribir '1. Agregar nuevo cliente manualmente'
				Escribir '2. Ver lista de clientes'
				Leer sub_opcion
				Si sub_opcion=1 Entonces
					cancelar <- Falso
					Escribir 'Nombre del cliente (o escriba salir): '
					Leer nombre_cliente
					Si Minusculas(nombre_cliente)<>'salir' Entonces
						Repetir
							Escribir 'DNI (8 o 12 digitos): '
							Leer dni_ingresado
							Si Longitud(dni_ingresado)<>8 Y Longitud(dni_ingresado)<>12 Entonces
								Escribir 'ERROR: Documento invalido.'
							FinSi
						Hasta Que Longitud(dni_ingresado)=8 O Longitud(dni_ingresado)=12
						cliente_existe <- Falso
						Para i<-1 Hasta total_clientes Hacer
							Si dni_cli[i]=dni_ingresado Entonces
								cliente_existe <- Verdadero
							FinSi
						FinPara
						Si cliente_existe=Falso Entonces
							total_clientes <- total_clientes+1
							nombres_cli[total_clientes] <- nombre_cliente
							dni_cli[total_clientes] <- dni_ingresado
							Escribir '>> Cliente guardado exitosamente <<'
						SiNo
							Escribir 'ERROR: Ya existe un cliente registrado con ese DNI.'
						FinSi
					FinSi
				SiNo
					Si sub_opcion=2 Entonces
						Si total_clientes=0 Entonces
							Escribir 'No hay clientes registrados aun.'
						SiNo
							Escribir 'LISTA DE CLIENTES:'
							Para i<-1 Hasta total_clientes Hacer
								Escribir i, '. ', nombres_cli[i], ' - DNI: ', dni_cli[i]
							FinPara
						FinSi
					FinSi
				FinSi
			4:
				Escribir ''
				Escribir '--- AGREGAR NUEVO PERFUME ---'
				cancelar <- Falso
				// LOGICA DE AUTO-INCREMENTO
				max_num <- 0
				Para i<-1 Hasta total_productos Hacer
					num_val <- ConvertirANumero(Subcadena(codigos[i],3,Longitud(codigos[i])))
					Si num_val>max_num Entonces
						max_num <- num_val
					FinSi
				FinPara
				siguiente_numero <- max_num+1
				Si siguiente_numero<10 Entonces
					nuevo_cod <- 'P-00'+ConvertirATexto(siguiente_numero)
				SiNo
					Si siguiente_numero<100 Entonces
						nuevo_cod <- 'P-0'+ConvertirATexto(siguiente_numero)
					SiNo
						nuevo_cod <- 'P-'+ConvertirATexto(siguiente_numero)
					FinSi
				FinSi
				Escribir '[*] Se generara automaticamente el codigo: ', nuevo_cod
				Repetir
					Escribir 'Nombre del perfume (o escriba salir): '
					Leer nuevo_nom
					Si Minusculas(nuevo_nom)='salir' Entonces
						cancelar <- Verdadero
					SiNo
						Si nuevo_nom='' Entonces
							Escribir 'Error: El nombre no puede estar vacio.'
						SiNo
							duplicado <- Falso
							Para i<-1 Hasta total_productos Hacer
								Si Minusculas(nombres_perfumes[i])=Minusculas(nuevo_nom) Entonces
									duplicado <- Verdadero
								FinSi
							FinPara
							Si duplicado Entonces
								Escribir '? Error: Ya existe un perfume con ese nombre en el catalogo.'
								nuevo_nom <- ''
							FinSi // Forza a repetir el ciclo
						FinSi
					FinSi
				Hasta Que cancelar=Verdadero O (nuevo_nom<>'' Y duplicado=Falso)
				Si  NO cancelar Entonces
					Escribir 'Stock inicial: '
					Leer nuevo_stock
					Escribir 'Precio unitario: '
					Leer nuevo_precio
					Si nuevo_stock>=0 Y nuevo_precio>0 Entonces
						total_productos <- total_productos+1
						codigos[total_productos] <- nuevo_cod
						nombres_perfumes[total_productos] <- nuevo_nom
						stock[total_productos] <- nuevo_stock
						precios[total_productos] <- nuevo_precio
						Escribir '>> Perfume agregado al catalogo con codigo [', nuevo_cod, '] <<'
					SiNo
						Escribir 'Error: Datos numericos invalidos. El stock no puede ser negativo y el precio debe ser mayor a 0.'
					FinSi
				FinSi
			5:
				Escribir ''
				Escribir '--- BUSCAR EN HISTORIAL ---'
				Escribir '1. Buscar por DNI del Cliente'
				Escribir '2. Buscar por Codigo o Nombre del Perfume'
				Escribir 'Elija el tipo de busqueda (1 o 2): '
				Leer sub_opcion
				Si sub_opcion=1 O sub_opcion=2 Entonces
					Escribir 'Ingrese el termino de busqueda:'
					Leer termino_busqueda
					encontrado <- Falso
					Escribir '>> RESULTADOS DE LA BUSQUEDA <<'
					Si sub_opcion=2 Entonces
						Para i<-1 Hasta total_productos Hacer
							Si Minusculas(codigos[i])=Minusculas(termino_busqueda) Entonces
								termino_busqueda <- nombres_perfumes[i]
							FinSi
						FinPara
					FinSi
					Para i<-1 Hasta total_ventas Hacer
						perfume_existe <- Falso
						Si sub_opcion=1 Y historial_dni[i]=termino_busqueda Entonces
							perfume_existe <- Verdadero
						SiNo
							Si sub_opcion=2 Y Longitud(termino_busqueda)<=Longitud(historial_perfume[i]) Entonces
								Si Minusculas(Subcadena(historial_perfume[i],1,Longitud(termino_busqueda)))=Minusculas(termino_busqueda) Entonces
									perfume_existe <- Verdadero
								FinSi
							FinSi
						FinSi
						Si perfume_existe Entonces
							Escribir '-----------------------------------'
							Escribir 'Comprador: ', historial_cliente[i], ' (DNI: ', historial_dni[i], ')'
							Escribir 'Perfume  : ', historial_perfume[i]
							Escribir 'Cantidad : ', historial_cantidad[i]
							Escribir 'Costo    : S/ ', historial_total[i]
							Escribir 'Fecha    : ', historial_fecha[i]
							encontrado <- Verdadero
						FinSi
					FinPara
					Si  NO encontrado Entonces
						Escribir 'No se encontraron registros de ventas con ese dato.'
					FinSi
				FinSi
			6:
				Escribir ''
				Escribir '--- AÑADIR STOCK ---'
				cancelar <- Falso
				encontrado <- Falso
				indice <- -1
				Repetir
					Escribir 'Ingrese el CODIGO o NOMBRE del perfume a recargar (o escriba salir): '
					Leer termino_busqueda
					Si Minusculas(termino_busqueda)='salir' Entonces
						cancelar <- Verdadero
					SiNo
						Para i<-1 Hasta total_productos Hacer
							Si Minusculas(codigos[i])=Minusculas(termino_busqueda) Entonces
								encontrado <- Verdadero
								indice <- i
							SiNo
								Si Longitud(termino_busqueda)<=Longitud(nombres_perfumes[i]) Entonces
									Si Minusculas(Subcadena(nombres_perfumes[i],1,Longitud(termino_busqueda)))=Minusculas(termino_busqueda) Entonces
										encontrado <- Verdadero
										indice <- i
									FinSi
								FinSi
							FinSi
						FinPara
						Si  NO encontrado Entonces
							Escribir 'ALERTA: El producto no existe en el catalogo. Intente de nuevo.'
						FinSi
					FinSi
				Hasta Que cancelar=Verdadero O encontrado=Verdadero
				Si encontrado Y  NO cancelar Entonces
					Escribir 'Producto: [', codigos[indice], '] ', nombres_perfumes[indice], ' | Stock actual: ', stock[indice]
					Repetir
						Escribir 'Ingrese la cantidad a añadir (o 0 para salir): '
						Leer cantidad
						Si cantidad=0 Entonces
							cancelar <- Verdadero
						SiNo
							Si cantidad>0 Entonces
								stock[indice] <- stock[indice]+cantidad
								Escribir '>> Stock actualizado exitosamente. Nuevo stock: ', stock[indice], ' <<'
							SiNo
								Escribir 'Error: La cantidad debe ser mayor a cero.'
							FinSi
						FinSi
					Hasta Que cancelar=Verdadero O cantidad>0
				FinSi
			7:
				Escribir 'Cerrando sistema... ¡Hasta pronto!'
			De Otro Modo:
				Escribir 'Opcion no valida. Por favor intente de nuevo.'
		FinSegún
	FinMientras
FinAlgoritmo
