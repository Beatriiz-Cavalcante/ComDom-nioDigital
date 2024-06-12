import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="DesafioC"
)

#exercício 1
'''meucursor = banco.cursor()
pesquisa = 'select * from Alunos;'
meucursor.execute(pesquisa)

#fetchall recebe tudo dda pesquisa e retorna através de uma tupla
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

#inserindo dados

nome1 = input("Digite o nome: ")
telefone1 = input("Digite o telefone: ")
cursor = banco.cursor()
sql = "insert into Alunos (nome, telefone) values (%s, %s)"
data = (nome1, telefone1)
cursor.execute(sql, data)
banco.commit()'''


#exercício 2
'''cursor = banco.cursor()

menu = int(input("-Mostrar os dados\n2-Inserir dados\n3-Encerrar o programa\nQual opção você deseja:"))
while menu >=1 and menu<3:
    if menu == 1:
        pesquisa = 'select * from Alunos;'
        cursor.execute(pesquisa)
        resultado = cursor.fetchall()
        for x in resultado:
            print(x)
    else:
        nome1 = input("Digite o nome: ")
        telefone1 = input("Digite o telefone: ")
        cursor = banco.cursor()
        sql = "insert into Alunos (nome, telefone) values (%s, %s)"
        data = (nome1, telefone1)
        cursor.execute(sql, data)
    menu = int(input("1-Mostrar os dados\n2-Inserir dados\n3-Encerrar o programa\nQual opção você deseja:"))
print("Programa encerrado")
cursor.close()
banco.close()'''

#exercício 3

meucursor = banco.cursor()
pesquisa = 'select * from Alunos;'
meucursor.execute(pesquisa)

#fetchall recebe tudo dda pesquisa e retorna através de uma tupla
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

#inserindo dados

#tabela Alunos
nome1 = input("Digite o nome: ")
cursor = banco.cursor()
sql = "insert into Alunos (nome) values (%s)"
data1 = (nome1)
cursor.execute(sql, data1)
banco.commit()

#tabela telefone
userid= cursor.lastrowid
telefone1 = input("Digite o telefone: ")
cursor = banco.cursor()
sql2 = "insert into telefone (matricula, numero) values (%s, %s)"
data2 = (userid,telefone1)
cursor.execute(sql2, data2)
banco.commit()
