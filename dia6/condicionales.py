
edad = int(input("Ingrese su edad (Ingresar solo numeros enteros): "))
hijos = 1 
estado_civil = "Soltero"
trabajo = True

# if edad < 0:
#     print("Ingrese un valor valido")
if edad > 18 :
    print("usted es mayor a 18 años")
elif edad == 18:
    print("usted tiene exactamente 18 años")
elif edad == 15:
    print("usted tiene 15 años")
else:
    print("es menor de 18 años")

print("Ejecucion terminada")