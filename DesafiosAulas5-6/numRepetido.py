'''Faça um código para ler um vetor de 30 números. Após isto, ler mais um número qualquer,
calcular e escrever quantas vezes esse número aparece no vetor'''

Vetor= [0] * 4
repeticao = 0

for c in range(len(Vetor)):
    Vetor[c] = int(input("Digite um número: "))

numeroComparacao = int(input("Digite o número a ser consultado: "))
for c in range(len(Vetor)):
    if numeroComparacao == Vetor[c]:
        repeticao += 1 
print(repeticao)