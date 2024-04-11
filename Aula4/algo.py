'''while condiçãoa: ação - se repete até que a condição se torne falsa
while é usado quando não se sabe a quantidade de laços
'''

#exemplo receber 10 números

x = 0
soma = 0
while x<10:
    n = float(input("Digite um número"))
    soma = soma + n
    x = x + 1

media = soma / 10
print(media)