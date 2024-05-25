from func import *

'''Menu para consultar cep chamando a função do arquivo func'''

controle = int(input("Deseja consultar um endereço?\nPara sim digite 1 \nPara não digite 2\n"))
while controle == 1:
    cep = input("Digite o cep: ")
    consulta(cep)
    controle = int(input("Deseja consultar outro endereço?\nPara sim digite 1 \nPara não digite 2\n"))
print("Programa encerrado")
