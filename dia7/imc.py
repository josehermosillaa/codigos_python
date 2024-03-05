""" 
Calcular IMC
IMC = W/H**2
con H en cm
W en Kg

< 18.5 Bajo Peso
[ 18.5, 25 [ Adecuado
[ 25, 30 [ Sobrepeso
[ 30, 35[ Obesidad Grado I
[ 35, 40 [ Obesidad Grado II
> 40 Obesidad Grado III
"""

print("Bienvenido a la calculadora de IMC \n")


W = input("Ingrese su peso en [Kg]: ")
W = float(W)
H = float(input("Ingrese su altura en centimetros [cm]:"))/100

imc = W/((H)**2)
print(f"Su IMC es : {imc:.2f}")

if imc < 18.5 :
    print("La Clasificación OMS es: Bajo Peso ")
elif imc >= 18.5 and imc < 25:
    print("La Clasificación OMS es: Adecuado ")
elif imc >= 25 and imc < 30:
    print("La Clasificación OMS es: Sobrepeso")
elif imc >= 30 and imc < 35:
    print("La Clasificación OMS es: adecuado ")
elif imc >= 35 and imc < 40:
    print("La Clasificación OMS es: adecuado ")
elif imc >= 40:
    print("La Clasificación OMS es: adecuado ")

