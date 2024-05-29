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
        self.jogador_atual = jogador1

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
        #para atualizar o tabuleiro com a jogada
        while True:
            posicao = int(input(f"{self.jogador_atual.nome}, em qual posição você quer jogar?\n0- A1,\n1- B1,\n2- C1,\n3- A2,\n4- B2,\n5- C2,\n6- A3,\n7- B3,\n8- C3\nSua resposta em número: ")) 
            if 0 <= posicao < 9:
                linha = posicao // 3
                coluna = posicao % 3
                if self.tabuleiro[linha][coluna] == ' ':
                    self.tabuleiro[linha][coluna] = self.jogador_atual.simbolo
                    break
                else:
                    print("Posição já ocupada. Tente novamente.")
            else:
                print("Posição inválida. Tente novamente.")
        #para alternar entro os jogadores
        if self.jogador_atual == self.jogador1:
             self.jogador_atual = self.jogador2
        else:
            self.jogador_atual = self.jogador1

    def retornaVencedor(self):
        combinacoesParaVencer = [
            [(0, 0), (0, 1), (0, 2)],  # Linha 1
            [(1, 0), (1, 1), (1, 2)],  # Linha 2
            [(2, 0), (2, 1), (2, 2)],  # Linha 3
            [(0, 0), (1, 0), (2, 0)],  # Coluna 1
            [(0, 1), (1, 1), (2, 1)],  # Coluna 2
            [(0, 2), (1, 2), (2, 2)],  # Coluna 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal Principal
            [(0, 2), (1, 1), (2, 0)]   # Diagonal Secundária
        ]

        for combinacao in combinacoesParaVencer:
            a, b, c = combinacao
            if self.tabuleiro[a[0]][a[1]] == self.tabuleiro[b[0]][b[1]] == self.tabuleiro[c[0]][c[1]] != ' ':
                print(f"{self.jogador_atual.nome} ganhou!")
                return

        print("Ainda não foi :(")

