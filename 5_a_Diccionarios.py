persona = {'nombre':'Tomás',
            'apellido':'Mesa',
            'cédula':'1001773737',
            'edad':21,
            'numhijos':0,
            1:'cualquier vaina'}
# se puede repetir el contenido asociado a una llave, pero no una misma llave

'''lista  = [5,6,7,5,3]
print(lista[2])
print(persona['cédula'])
print(persona[1])
'''

# (.clear) borra el contenido del diccionario
#persona.clear()

# (.copy) copia el contenido del diccionario
'''dic2 = persona.copy()
print(dic2)
'''

# (.fromkeys)
'''tupla = ('a','b','c')
x = 8
a = dict.fromkeys(tupla,x)
print(a)
'''

# (.get) devuelve el contenido asociado a una llave
print(persona.get('nombre'))
nombreEmpleado = persona.get('nombre')
print(nombreEmpleado)

print(persona['nombre']) # esto es lo mismo, sirve para acceder al contendio de la llave

# el diccionario es modificable
persona['nombre'] = 'Juan'
print(persona)

# (.items) devuelve el contenido del diccionario como parejas dentro de tuplas que están dentro de una lista
a = persona.items()
print(a)

# (.keys) devuelve las llaves
print(persona.keys())

# (.values) devuelve los valores
print(persona.values())

# (.pop) elimina la llave indicada
persona.pop('numhijos')
print(persona)

# (.popitem) elimina el último elemento
persona.popitem()
print(persona)

persona.update({'numhijos':0})
print(persona)

