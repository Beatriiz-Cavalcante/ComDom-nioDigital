'''crie um código que leia um número diferente de zero de diga se este número é positivo ou negativo'''

repete = 's'

while repete == 's' or repete == 'S':
    n1 = int(input("Digite um número: "))

    while n1 == 0:
        n1 = int(input("Digite um número válido: "))

    if n1 > 0:
        print(f'{n1} é um número positivo')
    else:
        print(f'{n1} é um número negativo')
    repete = input("Quer tentar outra vez? s ou n ")