from classe import *

print("Jogo da velha")
nome1 = input("Informe o nome do jogador 1: ")
simbolo1 = input("Vai jogar com x ou o? ")
jogador1 = Jogador(nome1, simbolo1)

nome2 = input("Informe o nome do jogador 2: ")
simbolo2 = input("Vai jogar com x ou o? ")
jogador2 = Jogador(nome2, simbolo2)

partida = JogoDaVelha(jogador1, jogador2)
partida.estrutura()

while True:
    partida.jogada()
    partida.retornaVencedor()
    # Verifica se houve um vencedor após cada jogada
    if partida.retornaVencedor():
        break  # Encerra o loop se houver um vencedor