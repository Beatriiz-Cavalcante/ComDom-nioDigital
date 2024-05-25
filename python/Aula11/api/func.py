import requests #bilioteca para apis

'''função para consultar api do viacep '''
def consulta(cep):
    if len(cep) != 8:
        print('cep invalido!')
        exit()
    consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    dados = consulta.json()

    print(dados['cep'])
    print(dados['logradouro'])
    print(dados['bairro'])
    print(dados['localidade'])
    print(dados['uf'])