from pprint import pprint

import requests

_print = print
print = pprint

url = 'http://127.0.0.1:3001/tokens'

user_data = {
    "password": "rafa@12345",
    "email": "rafa@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print('Texto: ', response.text)
    print(response.content)
    print(response.json())

    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
