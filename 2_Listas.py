# LISTAS

# Ordered and changeable

# cantidad de elementos en la lista

frutas = ["naranja", "papaya", "pera"]
tamaño = len(frutas)
print(frutas)

# (.append) agrega elementos al final de la lista
frutas.append("manzana")
print(frutas)

# aquí se sobreescribió el valor de la variable
valor = 5
print(valor)
valor = 9
print(valor)

# reemplazar un elemento por otro especificando la posición
frutas[1]="fresa"
print(frutas)

# (.insert) inserta un objeto en la posición indicada
frutas.insert(1,"mandarina")
print(frutas)

# (.clear) borra todos los elementos de las lista
"""frutas.clear()
print(frutas)"""

# (del) borra por completo la lista
"""del frutas
print(frutas)"""

# (.copy()) copia la lista
frutas2 = frutas.copy()
print(frutas2)

# si en lugar de sacar una copia se asigna una lista a otra con el símbolo =, las dos se modifican en simultáneo
frutas2.append("durazno")
print(frutas)
print(frutas2)
#frutas3 = frutas
#frutas3.append("mango")
#print(frutas3)
#print(frutas)

# (.count) dice cuántas veces está el elemento en la lista
cantidad = frutas.count("fresa")
print(cantidad)

# (.extend) une los elementos de dos listas
carros = ["renault", "mazda", "chevrolet"]
frutas.extend(carros)
print(frutas)

# (.index) especifíca en qué posición se encuentra un elemento de la lista
indice = frutas.index("pera")
print(indice)

# (.pop) elimina el último elemento de la lista
frutas.pop()
print(frutas)
frutas.pop(4)
print(frutas)

# (.remove) elimina el elemento que se le indique, si hay varios iguales elimina el primero de ese elemento
frutas.remove("pera")
print(frutas)

# (.reverse) invierte la lista
frutas.reverse()
print(frutas)

# (.sort) ordena la lista si contiene un mismo tipo de elemento
frutas.sort()
print(frutas)

# imprime la lista con los elementos desde el elemento 1 hasta el 4 en este caso
print(frutas[1:5])

# imprime la lista con los elementos desde el uno hasta adelante
print(frutas[1:])

# imprime la lista desde el inicio hasta el elemento 4
print(frutas[:5])


# ingresar elementos a una lista
lista1 = []
precio = int(input("ingrese el precio: "))
lista1.append(precio)
print(lista1)
nombre = input("Ingrese el nombre: ")
lista1.append(nombre)
print(lista1)

# indexación dentro de cadenas de caracteres
palabra = "amigos"
print(palabra[0])
print(len(palabra))
#print(palabra[2:5])