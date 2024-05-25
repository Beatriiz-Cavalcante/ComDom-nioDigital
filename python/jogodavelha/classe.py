'''Jogo da velha. Recebendo valores de dois jogadores e retornando o vencedor'''

class Jogador():
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

class JogoDaVelha(Jogador):
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro =   [
                                [' ', ' ', ' '],
                                [' ', ' ', ' '],
                                [' ', ' ', ' ']
                            ]

    def estrutura(self):
        print("Jogo da velha")
        print("  A B C")
        linha_num = 1
        for linha in self.tabuleiro:
            print(f"{linha_num} ", end='')
            for celula in linha:
                print(celula, end=' ')
            print()  
            linha_num += 1
        
    def jogada(self):