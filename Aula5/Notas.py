'''Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor, calcular a média
da turma e contar quantos alunos obtiveram a  nota acima desta média calculada. Escrever a média da turma e o
resultado da contagem'''

Notas = [0, 0, 0, 0, 0]
soma = 0
media = 0
aprovado = 0

for i in range(len(Notas)):
    Notas[i] = int(input("Nota do aluno: "))
for c in range(len(Notas)):
    soma = soma + Notas[c]
    media = soma / len(Notas)
for c in range(len(Notas)):
    if Notas[c] > media:
        aprovado = aprovado + 1

print(media)
print(aprovado)
