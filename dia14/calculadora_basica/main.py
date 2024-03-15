import suma
import resta as r
from input import tomar_datos

if __name__ == '__main__':
    print(__name__)
    bandera = True
    while bandera:
        opcion = input(
        """
        Esto es una calculadora:
        Que operacion le gustaria realizar?
        1. Suma
        2. Resta
        0. Salir
        """
        )
        if opcion == "1":
            x,y = tomar_datos()
            suma.suma(x,y)
            bandera = False

        elif opcion == "2":
            x,y = tomar_datos()
            r.resta(x,y)
            bandera = False

        elif opcion == "0":
            print("nos vemos en la proxima")
            bandera = False
        else:
            print("Opcion invalida")