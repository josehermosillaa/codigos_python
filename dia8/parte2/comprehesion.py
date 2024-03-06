# solicitamos el número de pares a generar
n = 10
# generamos una lista vacía para almacenar los pares
lista_par = []
#0 1 2 3 4 5 6 7 8 9
for i in range(n):
# podemos hacer append de los valoresgenerados
# en este caso partimos desde el 2
#los 10 primeros numeros pares
    lista_par.append(2*i + 2)
# mostramos el resultado
print(lista_par)

lista_par = [2*i+2 for i in range(n)]
print(lista_par)