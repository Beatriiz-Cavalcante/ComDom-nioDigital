'''Ler um valor N e imprimir todos os valores inteiros entre 1 e N.
Considere que o N será sempre maior que zero'''

n = int(input("Digite um número: "))
if n == 0:
    print("ERRO")
else:
    for c in range(1, n+1, 1):
        print(c)