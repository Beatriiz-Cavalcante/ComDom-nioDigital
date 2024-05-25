'''Escreva um código para ler as notas da 1a e 2a avaliações de um aluno, calcule e imprima a média desse aluno.
Só devem ser aceitos valores válidos durante a leitura, (0 a 10) para cada nota'''

#implementar o deseja realizar um novo um calculo


reinicia = 1
while reinicia == 1:
    n1 = float(input("Informe a primeira nota: "))
    while n1>10 or n1<0:
        n1 = float(input("Informe uma nota válida: "))

    n2 = float(input("Informe a segunda nota: "))
    while n2>10 or n2<0:
        n2 = float(input("Informe uma nota válida: "))

    media = (n1 + n2)/2
    print(media)

    reinicia = int(input("Deseja realizar um novo calculo:\n1-Sim\n2-Não\n"))

print("fim")
