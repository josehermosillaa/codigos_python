"""
diccionarios versus listas
"""

lista = [25, 31, "hola"]
# print(lista[2])
diccionario = {
    'a':25 ,
    'b':31 ,
    'c': "hola"
}
diccionario['a'] = 'hola mundo'
diccionario['d'] = True
# print(diccionario['c'])
# print(diccionario)

vacio = {}

vacio["nombre"] = "Gabriel"
vacio["apellido"] = "Garrido"
vacio["edad"] = 66
vacio["estado_civil"] = "Divorciado"
print(vacio)
vacio["estado_civil"] = "Casado"
print(vacio)
#ejemplo mmetodo pop
eliminado = vacio.pop("estado_civil") # el pop retirna el valor eliminado
# eliminado = vacio.pop("","no encontrado") # el pop retirna el valor eliminado

#puedo tomar el valor y usarlo ( en una variable etc)
print(eliminado)
# print("uno\n")
# print("")
# print("dos")

del vacio["edad"] #este metodo retorna SUPRIMIR

# del vacio["edad"] #este metodo retorna None
print(vacio)

# print(vacio['RUT']) ## no existe la clave ERROR (KeyError)

diccionario.update(vacio)

print(diccionario)

print("uno\n")
print("")
print("dos")

#docstring
mucho_texto =f""" hola soy un texto
mas largo que puedo imprimir
respetando 
los es      pacios
                    eso 
                    {diccionario}"""

print(mucho_texto)