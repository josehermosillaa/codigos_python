# from getpass import getpass


contrasena_valida = "holamundo"
condicion = True
contador = 1
while condicion and contador<4:
    password = input("Ingrese la clave secreta: ")
    
    if password == contrasena_valida:
        print("correcto")
        condicion = False
    else:
        print("Contraseña incorrecta!\n")
        # contador = contador +1
        contador+=1

if contador >3 :
    print("Su tarjeta a sido bloqueeada")