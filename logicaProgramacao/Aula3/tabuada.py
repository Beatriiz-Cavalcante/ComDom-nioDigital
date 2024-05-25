'''Ler uma variável de número inteiro e mostrar a tabuada de multiplicação desse número (1-10)'''

numero = int(input("Digite um número: "))
multiplicacao = 0
for c in range(1,11, 1):
    multiplicacao = numero * c
    print(f'{numero} x {c} = {multiplicacao}')