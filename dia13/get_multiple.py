x =100
def get_multiple(diccionario, *claves):
    print(x)
    return {clave: diccionario[clave] for clave in claves}


diccionario_prueba = {
    'manzana':'verde',
    'platano':'amarillo',
    'frutilla':'roja'
    }

resultado = get_multiple(diccionario_prueba, 'manzana','platano')
print(resultado)