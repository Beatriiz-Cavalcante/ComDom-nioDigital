'''Escreva um algoritimo que solicite ao usuário a entrada de 5 nomes, e que exiba a lista desse nomes na tela.
Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa em que o usuário os digitou
linha por linha'''

Nomes = [''] * 30
print("Digite os nomes a serem guardados")
for c in range(len(Nomes)):
    Nomes[c] = input("")
print(f"\n{Nomes}\n")

for c in range(len(Nomes)-1, -1, -1):
    print(f"{Nomes[c]}\n")