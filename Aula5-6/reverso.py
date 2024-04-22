'''faça um código para ler 5 números armazenar em um vetor. Após a leitura total dos 5 números, o código deve escrever
esses 5 lidos em ordem contrária'''

Vetor = [0, 0, 0, 0, 0]

for v in range(len(Vetor)):
    Vetor[v] = int(input("Número: "))
for c in range(len(Vetor)-1, -1, -1):
    print(Vetor[c])
