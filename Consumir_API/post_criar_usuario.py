from pprint import pprint

import requests

# _print = print
# print = pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "rafa",
    "password": "rafa@12345",
    "email": "rafa@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status Code: ', response.status_code)
    print('Reason: ', response.reason)
    # print('Texto: ', response.text)
    print('Bytes: ', response.content)
    print('JSON: ', response.json())
else:
    # Erros
    print('Status Code: ', response.status_code)
    print('Reason: ', response.reason)
    print('Texto: ', response.text)
