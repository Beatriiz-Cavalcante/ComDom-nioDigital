'''Ler 10 valores, calcular e escrever a média aritmética desses valores lidos'''

soma = 0
for c in range(10):
    c += 1
    numero = int(input("Digite um número: "))
    soma += numero
    #print(soma)
media = soma /10
print(media)
