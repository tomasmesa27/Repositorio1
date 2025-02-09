# Ejercicio _ Aplicativo gestión de inventarios

inventario = {}

while True:
    print('\nAplicativo de gestión de inventarios')
    print('1. Agregar producto al inventario')
    print('2. Vender producto')
    print('3. Mostrar inventario')
    print('4. Salir')

    opcion = input('Elija una opción: ').strip()

    if opcion == '1':

        # Agregar producto
        producto = input('Ingrese el nombre del producto: ').strip()
        cantidad = int(input('Ingrese la cantidad: '))

        if producto in inventario:
            inventario[producto] += cantidad
        else:
            inventario[producto] = cantidad

        print(f'Se agregaron {cantidad} unidades del producto {producto} al inventario')

    elif opcion == '2':

        # Vender producto
        producto =  input('Ingrese el nombre del producto: ').strip()

        if producto not in inventario:
            print('El producto no está en el inventario.')
        else:  
            cantidad = int(input('Ingrese la cantidad: '))
            if cantidad > inventario[producto]:
                print('No hay suficiente stock')
            else:
                inventario[producto] -= cantidad
                print(f'Se vendieron {cantidad} unidades del producto {producto}')
                
                # Si la cantidad llegó a 0, eliminar del inventario
                if inventario[producto] == 0:
                    del inventario[producto]
    
    elif opcion == '3':

        # Mostrar inventario
        if not inventario:
            print('El inventario está vacío')
        else:
            print('\nInventario actual:')
            for producto,cantidad in inventario.items():
                print(f'{producto}:{cantidad}')

    elif opcion == '4':

        # Salir del menú
        print('Saliendo del programa.')
        break

    else:
        print('Opción no válida, intente de nuevo.')