### Definición de datos
import datetime

datos_local_comercial = {'nombre':'NetZapatillas','direccion':'Alte. Brown 540','telefono':'+543794432569'}

usuarios = [
			{'usuario': 'admin', 'contraseña': 'admin', 'permisos': 'admin'},
			{'usuario': 'user', 'contraseña': 'user', 'permisos': 'user'}
			]

categorias = [{'Zapatillas deportivas':0}, {'Zapatillas':0}, {'Remeras':0}, {'Pantalones':0}, {'Medias':0}]

productos = []

### Comienzo del Programa.
finalizar_programa = 0
while not finalizar_programa:
	preguntar_opcion = 1
	while preguntar_opcion:
		print("############ NET ZAPATILLAS ############")
		print()
		print()
		print('Seleccione una de las siguientes opciones: ')
		print()
		print('[0] Agregar una nueva venta.')
		print('[1] Consultar resumen de ventas del día.')
		print('[2] Editar datos del local comercial.')
		print('[3] Finalizar programa.')
		print()
		opcion_ingresada = input('Ingrese su opción: ')
		print()
		if (opcion_ingresada == '0'):
			### TRATAR NUEVA VENTA (LLEVAR A CABO LA FACTURACIÓN)
			monto_total = 0
			while preguntar_opcion:
				print('############# NUEVA VENTA #############')
				print()
				print('Seleccione una de las siguientes opciones: ')
				print()
				print('[0] Añadir producto a la factura.')
				print('[1] Imprimir Factura.')
				print('[2] Volver al menú principal.')
				print()
				print('Subtotal Facturas: %.2f' % monto_total)
				print()
				opcion_ingresada = input('Ingrese su opción: ')
				print()
				if opcion_ingresada == '0':
					print('------------- CARGAR UN PRODUCTO A LA FACTURA -------------')
					print()
					# AGREGAR LINEA FACTURA. SOLICITANDO DATOS DE PRODUCTO
					nombre_producto = input('Ingrese el nombre del producto: ')
					precio_unitario = float(input('Ingrese el precio unitario: '))
					cantidad_producto = int (input('Ingrese la cantidad del mismo producto a agregar: '))
					seguir_preguntando = 1
					while seguir_preguntando:
						print('Seleccione la categoría del producto: ')
						print()
						i=0
						for categoria_producto in categorias:
							for (clave,valor) in categoria_producto.items():
								print ('[' + str(i) +']' + clave)
							i+=1
						print()
						categoria_producto = int(input('Ingrese su opción: '))
						print()
						if categoria_producto >= len(categorias) and categoria_producto < 0:
							pass
						else:
							seguir_preguntando = 0
					print()
					monto_total += precio_unitario * cantidad_producto
					nueva_linea_factura = [nombre_producto, precio_unitario, cantidad_producto, categoria_producto]
					productos.append(nueva_linea_factura)
				elif opcion_ingresada == '1':
					# IMPRIMIR FACTURA
					print('#####################################################################################')
					print(datos_local_comercial['nombre'])
					print('Dirección: ' + datos_local_comercial['direccion'])
					print('Teléfono: ' + datos_local_comercial['telefono'])
					print('Fecha: ' + datetime.datetime.now().strftime("%d/%m/%Y - %H:%M"))
					print('#####################################################################################')
					print('PRODUCTO                              CANTIDAD      PRECIO UNITARIO      SUBTOTAL')
					print('#####################################################################################')
					for linea_producto in productos:
						subtotal_linea = (linea_producto[2] * linea_producto[1])
						for (clave,valor) in categorias[linea_producto[3]].items():
							categorias[linea_producto[3]][clave] += subtotal_linea
						cant_espacios_en_blanco = 38-len(linea_producto[0])
						espacio_en_blanco = ''
						for x in range(cant_espacios_en_blanco):
							espacio_en_blanco += ' '
						print(linea_producto[0], end=espacio_en_blanco)
						cant_espacios_en_blanco = 14-len(str(linea_producto[2]))
						espacio_en_blanco = ''
						for x in range(cant_espacios_en_blanco):
							espacio_en_blanco += ' '
						print(linea_producto[2], end=espacio_en_blanco)
						cant_espacios_en_blanco = 21-len(str(linea_producto[1]))
						espacio_en_blanco = ''
						for x in range(cant_espacios_en_blanco):
							espacio_en_blanco += ' '
						print(linea_producto[1], end=espacio_en_blanco)
						print(subtotal_linea)
					print('#####################################################################################')
					print('TOTAL FACTURA: %.2f' % monto_total)
					print('#####################################################################################')
					print()
					productos = []
					preguntar_opcion = 0
				elif opcion_ingresada == '2':
					# VOLVER AL MENU PRINCIPAL:
					preguntar_opcion = 0
		elif (opcion_ingresada == '1'):
			### TRATAR RESUMEN DE VENTAS 
			while preguntar_opcion:
				print()
				print('############# RESUMENES DE VENTAS #############')
				print()
				print('Seleccione el tipo de resumen a imprimir: ')
				print()
				print('[0] Resumen de ventas filtrado por categoría, ordenados en forma alfabética.')
				print('[1] Resumen de ventas filtrado por categoría, ordenados de mayor a menor según los importes de venta.')
				print('[2] Volver al menú principal.')
				print()
				opcion_ingresada = input('Ingrese su opción: ')
				print()
				if opcion_ingresada == '0':
					# MOSTRAR RESUMEN DE VENTAS POR CATEGORÍA, ORDENADO ALFABÉTICAMENTE.
					print('###### Resumen de Ventas - Filtrado por CATEGORIA - Orden ALFABÉTICO CRECIENTE. ######')
					categorias_ordenadas_alfab = []
					for categoria in categorias:
						for (clave,valor) in categoria.items():
							categorias_ordenadas_alfab.append(clave)
					categorias_ordenadas_alfab.sort()
					for categoria_ordenada in categorias_ordenadas_alfab:
						for categoria in categorias:
							for (clave,valor) in categoria.items():
								if clave == categoria_ordenada:
									print(clave,'= %.2f' % valor)
					print()
				elif opcion_ingresada == '1':
					# MOSTRAR RESUMEN DE VENTAS POR CATEGORÍA, ORDENADO POR IMPORTES DE VENTAS DE MAYOR A MENOR.
					print('###### Resumen de Ventas - Filtrado por CATEGORIA - Orden IMPORTE DE VENTAS DECRECIENTE. ######')
					categorias_ordenadas_ventas = []
					for categoria in categorias:
						for (clave,valor) in categoria.items():
							if not categorias_ordenadas_ventas.count(valor):
								categorias_ordenadas_ventas.append(valor)
					categorias_ordenadas_ventas.sort(reverse=True)
					for categoria_ordenada in categorias_ordenadas_ventas:
						for categoria in categorias:
							for (clave,valor) in categoria.items():
								if valor == categoria_ordenada:
									print(clave,valor)
									break
					print()
				elif opcion_ingresada == '2':
					# VOLVER AL MENU PRINCIPAL.
					preguntar_opcion = 0
		elif (opcion_ingresada == '2'):
			### EDITAR DATOS
			while preguntar_opcion:
				print('############# EDITAR DATOS DE FACTURACIÓN #############')
				print()
				print('Seleccione el dato que desea editar imprimir: ')
				print()
				print('[0] Editar Razón Social.')
				print('[1] Editar Dirección.')
				print('[2] Editar Teléfono.')
				print('[3] Volver al menú principal.')
				print()
				opcion_ingresada = input('Ingrese su opción: ')
				print()
				if opcion_ingresada == '0':
					# EDITAR NOMBRE DE LA EMPRESA.
					datos_local_comercial['nombre'] = input("Ingrese la nueva razón social: ") 
				elif opcion_ingresada == '1':
					# EDITAR DIRECCIÓN DE LA EMPRESA. 
					datos_local_comercial['direccion'] = input("Ingrese nueva dirección: ") 
				elif opcion_ingresada == '2':
					# EDITAR NUMERO DE TELÉFONO
					datos_local_comercial['telefono'] = input("Ingrese nuevo numero teléfonico: ") 
				elif opcion_ingresada == '3':
					# VOLVER AL MENU PRINCIPAL.
					preguntar_opcion = 0
				print()
		elif (opcion_ingresada == '3'):
			print('############# FINALIZAR PROGRAMA #############')
			print()
			input('Presione ENTER para finalizar. ')
			### FINALIZAR PROGRAMA
			finalizar_programa = 1
			preguntar_opcion = 0
		else:
			print("ERROR. INGRESE UNA OPCIÓN VÁLIDA. INTENTE NUEVAMENTE.")
			print()
