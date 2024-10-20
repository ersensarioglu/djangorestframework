import requests

product_id = input("What is the product id you want to use?\n")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')
    product_id = None
    
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)

    print(get_response.text or "Deleted")
    print(get_response.status_code)

