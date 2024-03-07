"""invierte la posicion de los elementos->al reves ( el ultimo pasa a ser el primero el penultimo el segun etc etc)"""
numeros = [1,2,3,4,5,6,7]
otro = [1,2,3,4]
colores  = ['rojo', 'verde', 'morado', 'amarillo']
print(zip(otro, colores))
for elemnto in zip(otro, colores):
    print(elemnto)
numeros.reverse()
colores.reverse()

print(numeros)
print(colores)

colores.sort()
print(colores)

ordenar = [100, -40, 500, 6, 13 ,14.5]
# ordenar.sort()
x = sorted(ordenar, reverse=True)
# print(ordenar, sorted(ordenar))
print(x)
# print(x.index(14.5))

nueva_lista = numeros+colores
# print(nueva_lista)
# print(nueva_lista*2)

especial = nueva_lista*2
especial.reverse()
# ordenada2 = sorted(especial) #me muestra error
# print(ordenada2)
print(especial)