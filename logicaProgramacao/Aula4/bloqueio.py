'''Faça um código para ler a senha de um usuário e após 3 tentativas erradas, sair do programa,
informando que a senha está bloqueada'''

senhaG = '123'
senhaR = input("Digite a senha: ")
c = 0

if senhaR != senhaG:
    while c<2:
        senhaR = input("Senha incorreta. tente outra vez: ")
        c = c + 1
        if senhaR != senhaG and c==2:
            print("Senha bloqueada!")
        elif senhaR == senhaG:
            print("Senha correta :)")
else:
    print("Senha correta  :)")



