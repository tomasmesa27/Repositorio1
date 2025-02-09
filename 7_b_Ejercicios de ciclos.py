# Ejercicio ciclo while
'''
valores = []
i = 1
while i <= 10:
    numero = int(input('Ingrese un número: '))
    valores.append(numero)
    i += 1
print(valores)

t = 0
sumatoria = 0
while t < 10:
    if t == 5:
        break
    sumatoria += valores[t]
    t += 1
print('La sumatoria es: ', sumatoria)

#suma = sum(valores)
#print(suma)
'''
'''
# Ejercicio ciclo for
# Mi respuesta
print('Este programa contiene las tablas de multiplicar')
y = int(input('Ingrese un número: '))
for x in range(0,y*11,y):
    print(int(x/y),'x',y,'=',x)

# Respuesta profe
tabla = int(input('Ingrese un número: '))
for i in range(1,11):
    print(i,'x',tabla,'=',i*tabla)
'''
# Ejercicio _ todas las tablas de multiplicar
for i in range(1,11):
    for j in range(1,11):
        print(i,'x',j,'=',i*j)