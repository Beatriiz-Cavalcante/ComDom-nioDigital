'''Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido,
caso o segundo valor digitado, seja zero, solicite novamente p valor, informando que só aceitaremos
valores diferentes de zero'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

while n2 == 0:
    n2 = int(input("Número inválido. Digite um valor diferente de zero: "))

divisao = n1 / n2
print(divisao)