'''Ler 10 valores e escrever quantos desses valores lidos são negativos'''
resultado = 0
indice = 0
for c in range(1, 11):
    valor= int(input("Digite um valor: "))
    if valor < 0:
        indice = 1
        resultado += indice
print(resultado)
