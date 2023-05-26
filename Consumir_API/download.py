import requests

# url = 'https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg'

url = 'http://localhost:3001/images/1685042523045_17795.png'

nome_arquivo = url.split('/')[-1]

print(nome_arquivo)

response = requests.get(url)


if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)
else:
    # Erros
    print(response.status_code)
    print(response.reason)
