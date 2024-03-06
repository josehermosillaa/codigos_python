#Mexico 70 , Chile 50, Argentina 55
#  convertir en diccionario
#filtrar los paises con menos de 60 usuarios 

#diccionario key    Pais  value cant usuarios

paises = {
    "Mexico": 70,
    "Chile": 50,
    "Argentina":55
}

filtrado = {}

for k, v in paises.items():
    if v<60:
        filtrado[k] = v

print(filtrado)
