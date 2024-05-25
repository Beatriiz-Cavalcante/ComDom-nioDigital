'''Criar um array tamanho 5 preencher com os np,es dpss 5 alunos, informados pelo usuários'''

Alunos = ['','','','','']
for x in range(len(Alunos)):
    Alunos[x] = input("Digite o nome do aluno: ")
for x in range(len(Alunos)):
    print(Alunos[x], end = " ")


'''Incrementar o exercício acima, mostrando também o índice'''
Alunos = ['','','','','']
for x in range(len(Alunos)):
    Alunos[x] = input("Digite o nome do aluno: ")
for x in range(len(Alunos)):
    print(x+1, ":",Alunos[x])