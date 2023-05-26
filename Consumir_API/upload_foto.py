from mimetypes import MimeTypes
from pprint import pprint

import requests
from get_token import token
from requests_toolbelt import MultipartEncoder

_print = print
print = pprint

mimetypes = MimeTypes()

nome_arquivo = 'logo.png'
mimetype_arquivo = mimetypes.guess_type(nome_arquivo)[0]

# print(mimetype_arquivo) # tipo arquivo

multipart = MultipartEncoder(fields={
    'aluno_id': '2',
    'foto': (nome_arquivo, open(nome_arquivo, 'rb'), mimetype_arquivo)
})


url = 'http://127.0.0.1:3001/fotos'


headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers, data=multipart)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()
    print(response_data)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
