import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"in":"hi"}, json={"out":"bye"})

print(get_response.text)
print(get_response.json())
print(get_response.status_code)

post_response = requests.post(endpoint + "post", json={"title":"hello", "price": "yes"})

print(post_response.text)
print(post_response.json())
print(post_response.status_code)