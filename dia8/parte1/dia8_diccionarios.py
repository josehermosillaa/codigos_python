#primer diccionario
diccionario = {
    "Nombre":"Carlos",
    "Apellido":"Santana",
    "Ocupación":"Guitarrista",
    "Discos": ["inner Secrets", "Blue for Salvador"],
    "Vivo": True,
    "Edad": 76,
}
#formato Json
# [{},{}]

# print(diccionario["Nombre"])
# print(diccionario["Apellido"])
# print(diccionario["Ocupación"])
# print(diccionario["Discos"])
#dict
# for key, value in diccionario.items():
#     print(f" clave {key} - valor {value}")

texto = "nogatongamegalosomanjarchafafrinilofo"
for posicion, elemento in enumerate(texto) :   #cuando usamos enumerate contador, elemento
    print(f"la letra {elemento} esta en la posicion {posicion}")