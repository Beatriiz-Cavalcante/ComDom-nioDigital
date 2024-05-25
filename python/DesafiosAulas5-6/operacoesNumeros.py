'''Faça um algoritmo que leia 30 valores do tipo inteiro e armazene-os em um vetor.
A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no vetor;
(2) o menor e o maior valor existente no vetor;
(3) quantos dos valores do vetor são maiores que a média desses valores:'''

Numeros = [0] * 30
maior = 0
soma = 0
media = 0
qtdAcimaMedia = 0

print("Digite os números a serem guardados:")

#recebendo valores e já fazendo o calculo da média
for c in range(len(Numeros)):
    Numeros[c] = int(input(" "))
    soma += Numeros[c] 
media = soma / len(Numeros)

#precisou ser definido depois de receber os valores do vetor, para guuardar o valor que está no índice 0
menor = Numeros[0]

print("Os números pares da lista são:")
for c in range(len(Numeros)):
    #verificando os números pares
    if Numeros[c] % 2 == 0:
        print(Numeros[c], end=" ")
    #verificadno maior numero    
    if Numeros[c] > maior:
        maior = Numeros[c] 
    #verificando menor numero    
    if Numeros[c] < menor:
        menor = Numeros[c]
    #verificando os numeros maiores do que a média
    if Numeros[c] > media:
        qtdAcimaMedia += 1 

#retorno item 2
print(f"\nO maior número da lista é: {maior}\nO menor número da lista é: {menor}")

#retorno item 3
print(f"\nA média da lista é: {media}")
print(f"{qtdAcimaMedia} números da lista estão acima da média")



