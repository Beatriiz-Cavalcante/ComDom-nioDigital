'''Faça um código que receba 4 números e realize a soma deles e a média entre eles e mostre os resultados'''
soma=0
for c in range(4):
    numero = float(input(f"Informe o número {c+1}: "))
    soma += numero
media = soma/4
print(media)