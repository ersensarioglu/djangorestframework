import requests

endpoint = "http://127.0.0.1:8000/api/products/157685846546878"

get_response = requests.get(endpoint)

print(get_response.text)
print(get_response.json())
print(get_response.status_code)

