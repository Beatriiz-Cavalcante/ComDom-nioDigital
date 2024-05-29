class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo

class JogoDaVelha:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogador_atual = jogador1
        self.tabuleiro = [' '] * 9

    def estrutura(self):
        print("Jogo da velha")
        print("  A B C")
        for i in range(3):
            print(f"{i + 1} {self.tabuleiro[i * 3]} {self.tabuleiro[i * 3 + 1]} {self.tabuleiro[i * 3 + 2]}")

    def jogada(self):
        while True:
            posicao = input(f"{self.jogador_atual.nome}, em qual posição você quer jogar? (ex: A1, B2): ").upper()
            coluna = ord(posicao[0]) - ord('A')
            linha = int(posicao[1]) - 1
            indice = linha * 3 + coluna

            if 0 <= indice < 9:
                if self.tabuleiro[indice] == ' ':
                    self.tabuleiro[indice] = self.jogador_atual.simbolo
                    break
                else:
                    print("Posição já ocupada. Tente novamente.")
            else:
                print("Posição inválida. Tente novamente.")

        self.jogador_atual = self.jogador2 if self.jogador_atual == self.jogador1 else self.jogador1

    def verifica_vencedor(self):
        # Checar linhas, colunas e diagonais
        combinacoes_vencedoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]

        for combinacao in combinacoes_vencedoras:
            if self.tabuleiro[combinacao[0]] == self.tabuleiro[combinacao[1]] == self.tabuleiro[combinacao[2]] != ' ':
                return True

        return False

    def jogo(self):
        while True:
            self.estrutura()
            self.jogada()
            if self.verifica_vencedor():
                self.estrutura()
                vencedor = self.jogador2 if self.jogador_atual == self.jogador1 else self.jogador1
                print(f"Parabéns, {vencedor.nome}! Você venceu!")
                break
            if all(cell != ' ' for cell in self.tabuleiro):
                self.estrutura()
                print("Empate!")
                break
