import requests #bilioteca para apis

#dessa forma retorna tudo o que foi definido na própria api
'''print('Verificando o endereço')
cep = input('Digite o cep: ')
if len(cep) !=8:
    print('cep invalido!')
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
print(consulta.json())'''

#dessa forma retorna o que for pedido

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="DesafioC"
)

nome = input('Informe o seu nome: ')
print('Verificando o endereço')
cep = input('Digite o cep: ')
if len(cep) !=8:
    print('cep invalido!')
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
dados = consulta.json()
cep = dados['cep']
logradouro = dados['logradouro']
bairro = dados['bairro']
localidade = dados['localidade']
uf=dados['uf']

cursor = banco.cursor()
sql = "insert into endereco (nome, cep, logradouro, bairro, localidade, uf) values (%s, %s, %s, %s, %s, %s)"
data1 = (nome,cep, logradouro, bairro, localidade, uf)
cursor.execute(sql, data1)
banco.commit()
cursor.close()
banco.close()