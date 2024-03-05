# imc = 25.1

# if 18.5 < imc and imc<=25:
#     print("Se cumple la condicion!") 
def calcular_imc(peso, altura):
    imc = peso/(altura**2)

    print(imc)


perrito = float(input("ingrese su peso en kg"))
juanito = float(input("Ingrese su altura en cm"))

calcular_imc(perrito, juanito)