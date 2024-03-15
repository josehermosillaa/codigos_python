import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"

# # payload = {}
# # headers = {}
# # response = requests.request("GET", url, headers=headers, data=payload)
# response = requests.get(url)
# result = json.loads(response.text)
# print(type(response.text))
# print(type(result))

# print(result[0]['title'])
# print([post['title'] for post in result])

def request_json(url):
    return json.loads(requests.get(url).text)

data = request_json('https://jsonplaceholder.typicode.com/photos')[0:10]

# print(data)