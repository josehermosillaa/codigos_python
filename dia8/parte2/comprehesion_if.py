valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)

divisibles = ['Divisible' if valor%2==0 else 'No divisible' for valor in valores]


print(divisibles)
