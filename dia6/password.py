from getpass import getpass

password = getpass("Ingrese un Password: ")
# password = input("Ingrese su Password: ")
# print(password.strip()) #quita espacios en blanco del principio y final
# if password == "12345":
#     print("El Password es incorrecto")
# elif len(password)<6:
#     print("El Password ingresado es muy corto!")

# else:
#     print("el password se ingreso correctamente")


if len(password)<6:
    print("El Password ingresado es muy corto!")
elif password == "12345":
    print("El Password es incorrecto")

else:
    print("el password se ingreso correctamente")