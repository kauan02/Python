import requests

def test_shold_get_list_of_products():
    r = requests.get('http://localhost:8000/products')
    response = r.json()
    print(response)
    
test_shold_get_list_of_products()