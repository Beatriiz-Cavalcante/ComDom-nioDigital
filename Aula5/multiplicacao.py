'''Preencher um vetor A com 10 números. Logo em seguida, ler mais um número e guardar em uma variável x
Armazenar em um vetor M o resultado dde cada elemento de A multiplicado pelo valor de x
No final imprimir o vetor M'''

A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
M = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(A)):
    A[i] = int(input("Informe um número: "))

x = int(input("\nInforme o multiplicador: "))

for i in range(len(M)):
    M[i] = A[i] * x
print(M)