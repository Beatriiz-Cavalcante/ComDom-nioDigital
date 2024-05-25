'''Crie um algoritmo que çeia um número e diga se ele é par ou impar'''

repete = 0

while repete != -99:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f'{numero} é par')
    elif numero!=-99:
        print(f'{numero} é impar')
    else:
        print("Programa encerrado")


