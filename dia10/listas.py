"""
una lista siempre se define entre corchetes (parentesis cuadrados) y cada elemento 
se separa po coma
"""
lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
#         0  1  2  3  4  5  6  7  8


datos_varios = [1, "patata", True, 3.0]
#               0    1       2      3
print(datos_varios.__dir__())


lista_anidada = [1, "patata", ['perro', 'gato']]
#                0    1             2
"""indices negativos"""
lista_anidada = [1, "patata", ['perro', 'gato']]
#                -3        -2            -1      

animal = lista_anidada[2] #contiene la lista
# print(animal[0])

# print(lista_anidada[2][0]) # ['perro', 'gato']

"""PARa conocer el largo de una lista podemos utilizar la funcion len"""
# print(len(lista))
#                                0         1
# print(lista)
# print(type(lista))

# print(lista[8])
###  nombre[indice]

#en ingles la palabra list es resevada
#no se puede usar para ninguna operacion en el codigo
# list = 3
# print(list)
# for list in lista:
#     print(list)
""" 
disclaimer se puede usar la palabra list PERO NO SE RECOMIENDA
ES MALA PRACTICA
otras por ejemplo:
str
dict
len
pass
break
try
entre otras
for 
loop
"""