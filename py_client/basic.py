import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"in":"hi"}, json={"out":"bye"})

print(get_response.text)
print(get_response.json())
print(get_response.status_code)