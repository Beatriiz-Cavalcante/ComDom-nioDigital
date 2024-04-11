'''faça um código que recebe o número de alunos de uma sala de aula e depois solicite as notas
desses alunos e depois solicite as notas desses alnos, no final, mostre a média aritmética da turma'''

numeroAlunos = int(input("Digite a quantidade de alunos da turma: "))
x = 0
soma = 0
while x<numeroAlunos:
    notas = float(input("Diga a nota de cada aluno: "))
    soma = soma + notas
    x = x + 1
media = soma / numeroAlunos
print(f'A média da turma é {media}')