# Ciclo while

'''
i = 1
while i <= 10:
    print(i)
    i += 1
print('por aquí continúa el flujo')
'''

'''
x = int(input('Diga un número del 1 al 10: '))
y = 1
while y <= 10:
    print(y,'x',x,'=',x*y)
    y += 1
print('Fin')
'''
'''
lista = []
i = 0
while i<5:
    n = int(input('Escriba un número: '))
    lista.append(n)
    i = i+1
print(lista)
'''
# suma de una lista, opción 1
# suma = sum(lista)

# suma de una lista, opción 2
'''
print('Ahora vamos a empezar a sumar los elementos')
i = 0
suma = 0
while i<5:
    suma = suma+lista[i]
    i = i+1
print('El resultado es: ',suma)
'''
'''
print('Ahora vamos a multiplicar los elementos')
i = 0
múltiplo = 1
while i<5:
    múltiplo = múltiplo * lista[i]
    i = i+1
print('El resultado es: ',múltiplo)
'''

# Ciclo for

frutas = ['fresa','papaya','manzana','pera']
#for x in frutas:
#    print(x)

# Ahora vamos a hacer lo mismo con el ciclo while
'''
i = 0
while i<=3:
    print(frutas[i])
    i += 1
'''

persona = {'Nombre':'Carlos','Apellido':'Fadul','Cédula':'15327605'}
palabra = 'Murciélago'

