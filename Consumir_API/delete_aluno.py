from pprint import pprint

import requests
from get_token import token

_print = print
print = pprint

url = 'http://127.0.0.1:3001/alunos/3'

headers = {
    'Authorization': token
}

response = requests.delete(url=url, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print('Texto: ', response.text)
    # print(response.content)
    print(response.json())

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
