'''Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada
lista em um array diferente, após completar a digitação, imprimir, nome, senha e 
posição dos dados no array'''

Nome = ['','','','','']
Senha = ['','','','','']

for c in range (len(Nome)):
    Nome[c] = input("Nome do usuário: ")
    Senha[c] = input("Senha do usuário: ")

for c in range (len(Nome)):
    print(f"{c} - {Nome[c]} - {Senha[c]}")