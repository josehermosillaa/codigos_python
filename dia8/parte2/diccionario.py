claves = ['nombre','apellido','edad','altura']

valores = ['Juan','Pérez', 33, 1.75]


print({k:v for k,v in zip(claves, valores)})
# {'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 33, 'altura': 1.75}
