'''faça um algoritmo quen receba 2 notas e calcule a media aritmética'''

soma = 0
for c in range(2):
    nota = int(input(f"Informe a nota {c+1}: "))
    while nota<0 or nota>10:
        nota = int(input("Informe a nota válida: "))
    soma = soma + nota

media = soma /2

print(f'A média é: {media}')