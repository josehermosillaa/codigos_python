
preguntas = ['Ingrese su Nombre completo', 'Cuanta gente vive aqui?', 'maximo nivel de estudios']

def encuesta(lista):
    respuestas = []
    for pregunta in lista:
        print(pregunta)
        print("Ingrese su respuesta")
        respuestas.append(input('> '))
    print('sus respuestas fueron')
    print(respuestas[0])
    print(respuestas[1])
    print(respuestas[2])


encuesta(preguntas)


# print(preguntas[0])
# print("Ingrese su respuesta")
# respuestas.append(input('> '))

# print(preguntas[1])
# print("Ingrese su respuesta")
# respuestas.append(input('> '))

# print(preguntas[2])
# print("Ingrese su respuesta")
# respuestas.append(input('> '))


