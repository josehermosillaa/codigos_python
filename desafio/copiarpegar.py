#DESAFIO SOBRE FILTROS RELEVANTES
# ---------------------------------

precios = {'Notebook': 700000, 
    'Teclado': 25000, 
    'Mouse': 12000, 
    'Monitor': 250000, 
    'Escritorio': 135000, 
    'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral):
    #RECORRER EL DICC PARA VALORES SOBRE EL UMBRAL
    #---------------------------------------------
    filtro = {k:v for k, v in diccionario.items() if v == umbral}
    return filtro

print(filtrar(precios,12000))