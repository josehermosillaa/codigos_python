from random import choice

# import random
# random.choice()
condicion = True
print("Bienvenido al Cachipun \n")
marcador_pc = 0
marcador_jugador = 0
while condicion:

    
    jugador = input("Ingrese su eleccion [piedra, papel, tijera]:\n").lower()
    if jugador == "tijera" or jugador == "papel" or jugador == "piedra":
        computadora = choice(["papel", "piedra", "tijera"])

        print(f"La computadora jugó: {computadora}")
        if jugador == computadora:
            print(" HAS EMPATADO ")
            print(f"jugador {marcador_jugador}-{marcador_pc} computadora")

        elif jugador == "tijera" and computadora == "papel":
            print("HAS GANADO")
            marcador_jugador = marcador_jugador + 1
            print(f"jugador {marcador_jugador}-{marcador_pc} computadora")

        elif jugador == "piedra" and computadora == "tijera":
            print("HAS GANADO")
            marcador_jugador = marcador_jugador + 1
            print(f"jugador {marcador_jugador}-{marcador_pc} computadora")

        elif jugador == "papel" and computadora == "piedra":
            print("HAS GANADO")

            marcador_jugador = marcador_jugador + 1
            print(f"jugador {marcador_jugador}-{marcador_pc} computadora")

        else:
            print("La computadora Gana")
            marcador_pc = marcador_pc + 1
            print(f"jugador {marcador_jugador}-{marcador_pc} computadora")
    elif jugador == "salir":
        print("JUEGO TERMINADO....\n")
        print(f"El marcador final es de: jugador {marcador_jugador}-{marcador_pc} computadora")
        condicion = False
    # elif marcador_jugador or marcador_pc 
    else:
        print("La opción ingresada no es valida....\n") 

        print("Ejecucion terminada")


