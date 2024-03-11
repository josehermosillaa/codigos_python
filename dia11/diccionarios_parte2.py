# peliculas_marvel = {
# "Iron Man" : 2008,
# "The Incredible Hulk":2008,
# "Thor":2011,
# "The Avengers":2012
# }
# # metodos en los diccionarios
# #Keys

# claves = peliculas_marvel.keys()
# # for c in claves:
# #     print(c)
# # print(claves)

# valores = peliculas_marvel.values()

# # print(valores)

# items = peliculas_marvel.items()
# print(items)
# for elemento in items:
#     print(elemento)

# for clave, valor in peliculas_marvel.items():
#     print(clave)
#     print(valor)
    
# obtener = peliculas_marvel.get("Iron")

# print(obtener)



lista = ['Iron Man', 2008,'The Incredible Hulk', 2008]


tupla = ('Iron Man', 2008,'The Incredible Hulk', 2008)
#           0        1           2                3
#las tuplas tambien tienen un orden automatico
print(lista[0])
print(tupla[0])


# tupla = ('The Incredible Hulk', 2008,'Iron Man', 2008)
temporal = lista[2]
lista[2] = lista[0] # en este punto la lista cambio
lista[0] = temporal
print(lista)
# lista[0] = temporal
# print(lista)


# temporal = tupla[2]

# tupla[2] = tupla[0]
# tupla[0] = temporal
# print(tupla)

# tupla2 = 'Iron Man', 2008 #tupla
# tupla2 = ('Iron Man', 2008) #tupla

movie, year, cantidad_espectadores = 'Iron Man', 2008, 20000000   #unpacking de tuplas

print(movie)
print(year)
print(cantidad_espectadores)

peliculas_marvel = {
"Iron Man" : 2008,
"The Incredible Hulk":2008,
"Thor":2011,
"The Avengers":2012
}

items = peliculas_marvel.items()
print(items)

for elemento in items:
    print(elemento)

for  clave, valor in items:
    print(f"la clave es {clave}  y el valor es {valor}")

print(list(items))
print(items)