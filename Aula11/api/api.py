import requests #bilioteca para apis

#dessa forma retorna tudo o que foi definido na própria api
print('Verificando o endereço')
cep = input('Digite o cep: ')
if len(cep) !=8:
    print('cep invalido!')
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(consulta.json())

#dessa forma retorna o que for pedido
print('Verificando o endereço')
cep = input('Digite o cep: ')
if len(cep) !=8:
    print('cep invalido!')
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
dados = consulta.json()

print(dados['cep'])
print(dados['logradouro'])
print(dados['bairro'])
print(dados['localidade'])
print(dados['uf'])