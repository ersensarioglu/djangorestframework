import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "my test"
}
post_response = requests.post(endpoint, json=data)

print(post_response.text)
print(post_response.json())
print(post_response.status_code)

