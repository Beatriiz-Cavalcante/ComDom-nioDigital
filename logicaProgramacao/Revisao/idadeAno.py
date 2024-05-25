'''Crie um código que leia a idade de uma pessoa e diga em qual ano ela nasceu'''

repete = 's'
while repete == 's':
    idade= int(input("Digite a sua idade: "))

    anoAtual = 2024
    anoNascimento = anoAtual - idade
    p = input("Já fez aniversário esse ano?\n s ou n ")
    if p == 'n':
        print(anoNascimento-1)
    else:
        print(anoNascimento)
    repete=input("Deseja tentar outra vez? s ou n")