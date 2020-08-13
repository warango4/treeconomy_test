import requests
import json

def get_products():
    url = 'https://testbankapi.firebaseio.com/products.json'
    r = requests.get(url)
    products = r.json()
    return products

def post_products(data):
    url = 'https://testbankapi.firebaseio.com/products.json'
    r = requests.post(url, data=json.dumps(data))
    return r

def put_products(data):
    identifier = "-Lh7-wuYbP7AwpipuxNx"
    url = 'https://testbankapi.firebaseio.com/products/-Lh7-wuYbP7AwpipuxNx.json'
    r = requests.put(url, data=json.dumps(data))
    return r

def delete_products(data):
    identifier = "-Lh7-wuYbP7AwpipuxNx"
    url = 'https://testbankapi.firebaseio.com/products/-Lh7-wuYbP7AwpipuxNx.json'
    r = requests.delete(url)
    return r
