'''Altere o sistema anterior e faça um sistema de login, pedindo  senha do usuário e mostrando
seu nome e a mensagem, login efetuado com sucesso'''

Nome = ['','','','','']
Senha = ['','','','','']

for c in range (len(Nome)):
    Nome[c] = input("Nome do usuário: ")
    Senha[c] = input("Senha do usuário: ")
print("\nUsuários Cadastrados\n")

nomeL = input("Digite seu nome: ")
senhaL = input("Digite a senha: ")
if (nomeL == Nome[c]) and (senhaL == Senha[c]):
    print(f"Oi, {Nome[c]} :)\nLogin efetuado com sucesso!")
else:
    print("xô, racker")