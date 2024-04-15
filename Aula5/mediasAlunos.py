'''Recebe a quantidade de alunos, pede as notas de todos os alunos e retorna a média de cada um'''

alunos = int(input("Informe a quantidade de alunos"))

mediaSala= 0
soma = 0
for c in range(alunos):
    n1 = float(input("Informe a primeira nota: "))
    while n1>10 or n1<0:
        n1 = float(input("Informe uma nota válida: "))

    n2 = float(input("Informe a segunda nota: "))
    while n2>10 or n2<0:
        n2 = float(input("Informe uma nota válida: "))

    media = (n1 + n2)/2
    print(media)
    soma = soma + media
   
mediaSala = soma / alunos
print(f"A média da turma é {mediaSala}")
