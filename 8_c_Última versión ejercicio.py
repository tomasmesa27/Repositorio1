while True:
    print('Bienvenido al sistema de gestion de estudiantes (SGE)')
    print('a continuacion elija lo que desea realizar:')
    print('1. Agregar o actualizar estudiante')
    print('2. mostrar todas las calificaciones')
    print('3. Promedio')
    print('4. Buscar estudiante')
    print('5. Eliminar registro')
    print('6. Salir')
    opcion=int(input('ingresa la opcion a elegir:'))
    
    if opcion==1: #comparacion para decidir
        nombre=input('ingrese el nombre del estudiante')
        if nombre!='': #esto es para que ejecute si no deja la casilla en blanco, me dio pereza determinar que hacer si la dejaba en blanco tbh
            calificacion=float(input(f'igrese la calificacion del estudiante {nombre}:')) #ese f me sirve para poder llamar la variable
        datos_alumnos[nombre]= calificacion #estoy agregando la informacion al dicc
        print(f'la calificacion de {nombre}, fue actaulizada correctamente')
        continuar=input('\n presione enter para continuar el programa') #enconmtre que el \n me servia para que el menu no se ejecutara inmediatamente luego de cumplir un condicional, ya que se ve muy feo
        print(datos_alumnos)
    elif opcion==2:
        if len(datos_alumnos)>0: #usa len para ver que la lista no está vacía
            lista_estudiantes=list(datos_alumnos.keys()) #contador sería el index y, 0 el elemento 1
            contador=0 #contador es lo mismo que cuando ponemos i, solo que le pongo asi porque me confundo
            while contador< len(lista_estudiantes):
                nombre=lista_estudiantes[contador]
                calificacion=datos_alumnos[nombre]
                if calificacion>=3.0:
                    nota=('aprobado')
                else:
                    nota=('reprobado')
                print(f'El estudiante{nombre} tiene una calificación de {calificacion} y está {nota}')
                contador+=1
        else:
            print('La lista de estudiantes está vacía')
        continuar=input('\n presione enter para continuar el programa')
    elif opcion==3:
        if len(datos_alumnos)>0:
            lista_calificaciones=list(datos_alumnos.values()) #list sirve para modificar, agregar, organizar,etc
            suma_notas=0
            contador=0
            while contador< len (lista_calificaciones):
                suma_notas+=lista_calificaciones[contador]
                contador+=1
                promedio=suma_notas/len(lista_calificaciones)
                print(f'el promedio de calificaciones es: {promedio}')
        else:
            print('no hay estudiantes registrados')
        continuar=input('\n presione enter para continuar el programa')
    elif opcion==4:
        nombre=input('Ingresa el nombre del estudiante que deseas buscar:')
        if nombre in datos_alumnos:
            calificacion=datos_alumnos[nombre]
            if calificacion>=3.0:
                nota=('aprobado')
            else:
                nota=('reprobado')
            print(f'La calificacin de {nombre} es: {calificacion}')
        else:
            print('El estudiante no registra en base de datos')
        continuar=input('\n presione enter para continuar con el programa')
    elif opcion==5:
        registro_eliminar = input('Ingrese el alumno a eliminar: ')
        datos_alumnos.pop(registro_eliminar)
        print(datos_alumnos)
    elif opcion==6:
        print('Programa Finalizado')
        break
    else:
        print('Opcion Invalida')