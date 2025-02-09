# TUPLAS

# Ordered and unchangeable

# Las tuplas son con paréntesis
frutas = ("fresa","papaya","naranja","papaya")
frutas2 = ["fresa","papaya","naranja"]
print(frutas)

print(type(frutas))
print(type(frutas2))

# (.count) cuenta las veces que sale una palabra en la tupla
print(frutas.count("papaya"))

# (.index) la posición del elemento
print(frutas.index("papaya"))

# cambiamos la tupla a una lista
temporal = list(frutas)
print(frutas)
print(temporal)

temporal.pop(2)
print(temporal)

frutas = tuple(temporal)
print(frutas)

#print("Hello","World")
