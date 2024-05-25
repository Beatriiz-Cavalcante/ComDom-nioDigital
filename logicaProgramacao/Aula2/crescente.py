#Receba dois números do usuário e mostro eles em ordem crescente

n1 = float(input("informe um número: "))
n2 = float(input("informe outro número: "))

if n1>n2:
    print(f'A ordem crescente dos números é: {n1},{n2}')
else:
    print(f'A ordem crescente dos números é: {n2},{n1}')    