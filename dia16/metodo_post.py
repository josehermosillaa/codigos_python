import requests
url = "https://jsonplaceholder.typicode.com/posts"

payload = '''{"title": "Post 101",
"body": "Este es nuestro primer post"}'''

response = requests.post(url, data=payload)
print(response)
print(response.text)