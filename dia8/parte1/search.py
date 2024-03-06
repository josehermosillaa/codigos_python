import sys
import random

buscar = int(sys.argv[1]) #numero a buscar recordar : python search.py "numero a buscar"
# print(type(buscar))
lista = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista)
# print(lista)

for position, elemento in enumerate(lista):
    if elemento == buscar:
        print(f"Elemento encontrado, se termina el ciclo [posicion {position}]" )
        break
    else:
        print("elemento no encontrado")

print("salimos del for")

# if buscar in lista # True o False
