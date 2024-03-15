from consumir_api import request_json
from string import Template

url = "https://ghibliapi.vercel.app/films"
response = request_json(url)

# # print(response)
# for elemento in response:
#     print(elemento['image'])
lista_img = [(elemento['image'], elemento['title'],elemento['description'] ) for elemento in response]
nuevo_card =  """<div class="card" style="width: 18rem;">
                <img src="$url" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">$title</h5>
                    <p class="card-text">$desc</p>
                </div>
            </div>
    """
# img_template = Template('<img src="$url">')
img_template = Template(nuevo_card)
texto_img = ''
# imagen = img_template.substitute(url = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/kowo9E1e1JcWLXj9cCvAOFZcy5n.jpg')
for img, title, description in lista_img:
    texto_img += img_template.substitute(url = img, title = title, desc= description) + '\n'

# print(texto_img)


# print(imagen)
html_template = Template('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Estudio Ghibli</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1 class="text-center">Peliculas Estudio Ghibli</h1>
    <div class="container">
        <div class="row">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body = texto_img)

archivo = open('index.html', 'w+') 
archivo.write(html)
archivo.close()