from random import randint
# frase = "hola"

# print(type(frase))

#primer uso toma todos los valores  desde el 0 hasta el valor que se pasa como argumento,
#sin considerar ese valor
# for i in range(11):
#     print(i)


# numero = randint(1,10)
# # print(numero)
# for i in range(numero):
#     print(i)

#segundo uso de la funcion range
#        range(inicio, final)
# for i in range(4, 10,1):  # [4,10 [
#     print(i)

# """range(4,10)->  4, 5, 6, 7, 8, 9"""
#        range(inicio, fin, incremento)     {step}  
# for i in range(4, 10, 2):
#     print(i)
# """range(4,10,2)->  4, 6, 8"""
# """range(4,10,3)->  4, 7"""

""" LISTAS """
#estructura de datos 
lista = [ 1, 4, 5, 6, 8, 0] # es iterable
    #     0  1  2  3  4  5
# textos = ["perro","gato","iguana","serpientes"]
    #      0         1     2         3
otros = [1, "perro", True]
    #    0    1       2


# for elemento in "nogatongamegalosomanjarchafafrinilofo":
#     print(elemento)
textos = ["perro","gato","iguana","serpientes"]
        #    0      1        2          3
# print(textos[2])

#contando al cantidad de elementos de la lista
cantidad = len(textos)
print(cantidad) # la cantidad es 4
#range(4) -> 0, 1 ,2 ,3
for i in range(cantidad):
    print(textos[i])
#iteracion por indice en una lista

# for elemento in textos:
#     print(elemento)