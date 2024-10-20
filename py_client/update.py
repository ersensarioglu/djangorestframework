import requests

endpoint = "http://127.0.0.1:8000/api/products/6/update/"

data = {"title": "Hello world my friend",
        "price": 5}

get_response = requests.put(endpoint, json=data)

print(get_response.text)
print(get_response.json())
print(get_response.status_code)