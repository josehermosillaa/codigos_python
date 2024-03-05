prefijo = ['La', 'EL', 'LA', 'EL']

frutas = ['manzana', 'platano', 'frutilla', 'tomate']

colores = ['verde', 'amarillo', 'roja', 'rojo', "azul"]
# (['La', 'manzana', 'verde], ['El', 'platano', 'amarillo']..........)
variable = zip(prefijo,frutas, colores)
print(variable)

for p, fruta, color in variable:
    print(f"{p} {fruta} es de color {color}")