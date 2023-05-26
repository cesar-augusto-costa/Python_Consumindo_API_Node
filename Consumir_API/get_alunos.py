from pprint import pprint

import requests
from get_token import token

_print = print
print = pprint

url = 'http://127.0.0.1:3001/alunos'

response = requests.get(url=url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)
    # print('Texto: ', response.text)
    # print(response.content)
    # print(response.json())
    response_data = response.json()
    print(response_data)

    for aluno in response_data:
        print(aluno)

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
