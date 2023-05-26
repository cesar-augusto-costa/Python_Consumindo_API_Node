from pprint import pprint

import requests
from get_token import token

_print = print
print = pprint

url = 'http://127.0.0.1:3001/alunos'

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Luana 2",
    "sobrenome": "Vieira",
    "email": "luana2@email.com",
    "idade": "50",
    "peso": "80.04",
    "altura": "1.90"
}

response = requests.post(url=url, json=aluno_data, headers=headers)

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
