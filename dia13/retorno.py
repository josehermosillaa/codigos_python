def prueba_return():
    linea1 = "esta linea se retorna"
    linea2 = "esta linea se imprime"
    print(linea2)
    return linea1 #al momento de econtrar un retorno la funcion se detiene



# si yo no devuelvo nada por la funcion -> obtenemos None
a = prueba_return() #linea1
print(a)

# def elevado(x,y):
#     return x**y

def elevado(x,y):
    resultado = x**y
    return resultado 

resultado = elevado(2,2) * 2
print(resultado)

def cuadrado_cubo(base):
    cuadrado = base **2
    cubo = base**3

    return cuadrado, cubo, base
#(var1,var2) = (10, 3) desempaquetamiento
numero1, numero2, numero3 = cuadrado_cubo(4)
print(numero1)
print(numero2)
print(numero3)
