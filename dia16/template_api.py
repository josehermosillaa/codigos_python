from consumir_api import request_json
from string import Template

url = "https://ghibliapi.vercel.app/films"
response = request_json(url)

# # print(response)
# for elemento in response:
#     print(elemento['image'])
lista_img = [elemento['image'] for elemento in response]
img_template = Template('<img src="$url">')
texto_img = ''
# imagen = img_template.substitute(url = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/kowo9E1e1JcWLXj9cCvAOFZcy5n.jpg')
for img in lista_img:
    texto_img += img_template.substitute(url = img) + '\n'

# print(texto_img)


# print(imagen)
html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html>
''')

html = html_template.substitute(body = texto_img)

archivo = open('index.html', 'w+') 
archivo.write(html)
archivo.close()