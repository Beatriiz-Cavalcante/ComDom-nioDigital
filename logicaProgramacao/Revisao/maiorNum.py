'''Crie um algoritmo que receba 3 números e informe qual o maior numero entre eles'''

n1 = int(input("Informe um número"))
n2 = int(input("Informe outro número"))
n3 = int(input("Informe outro número"))

if n1>n2:
    if n1>n3:
        print(f"{n1} é o maior número")
    else:
        print(f"{n3} é o maior número")
else:
    if n2>n3:
        print(f"{n2} é o maior número")
    else:
        print(f"{n3} é o maior número")
