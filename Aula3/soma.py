'''escrevaa um algorítmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números'''

soma = 0
for c in range(1,11, 1):
    numero = int(input("Digite um número: "))
    soma += numero

print(soma)