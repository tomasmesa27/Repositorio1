lista = [1,2,3,4,5]

def suma(a):
    suma = sum(a)
    print(suma)

suma(lista)

def promedio(a):
    cantidad = len(a)
    suma = sum(lista)
    promedio = suma/cantidad
    print(promedio)

promedio(lista)

def mostrar(a):
    for x in a:
        print(x)

mostrar(lista)

