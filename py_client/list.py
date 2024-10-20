import requests

endpoint = "http://127.0.0.1:8000/api/products/"

post_response = requests.get(endpoint)

print(post_response.text)
print(post_response.json())
print(post_response.status_code)

