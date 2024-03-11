# def f(*args):
#     return args

# output = (f(1,[1,2],"string",{'clave':[4]}))
# print(type(output))
# print(output)

# def suma(*args):
#     print("ingrese solo numeros")
#     resultado = 0
#     for numero in args:
#         resultado = resultado + numero
#         # resultado+=numero
#     return resultado

# print(suma(1,5,10,100,2000, -4))

#los **kwargs

def f(**kwargs):
    return kwargs

output = f(valor =1, texto = 'hola', lista = [1,2,3,4,5])
print(output)
print(type(output))