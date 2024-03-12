
def pitatoria(lista):

    resultado = 1
    for numero in lista:
        resultado*=numero
    return resultado

def factorial(numero):
    # print(type(numero))
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = numero*factorial(numero-1)
        return resultado


def calcular(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        if (type(v) is int):
        
            fact = factorial(v)
            print(f"El factorial de {v} es {factorial(v)}")
        else:
            print(f"La productoria de {v} es {pitatoria(v)}")

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
print(pitatoria([3,6,4,2,8]))
"""
def calcular(*kwargs):
    #filtrar los datos de entrada

    argumento = {'fact_1': 5, 'prod_1': [3, 6, 4, 2, 8], 'fact_2': 6}
    for k, v in kwargs.items():
        if (type(v) is int) or (type(v) is list):
            #recien ejecuitariamos el codigo
            if type(v) is int:
                ejecutar factorial
            else:
                ejecutar productoria
        else:
            print(f"se ingreso un valor invalido : {v}")

def productoria(lista):
    resultado = 1
    for numero in lista:
        resultado = resultado *numero

    return resultado

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = numero*factorial(n-1)
        return resultado
"""