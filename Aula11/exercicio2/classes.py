'''Crie uma classe chamada ingresso, que possui um valor em reais e um método imprimeValor()
Crie uma classe vip, que herda de ingresso e possui um valor adicional. Crie um método que retorno o valor do ingresso
vip (com o adicional incluido)'''

class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"O valor do ingresso é {self.valor}")


class IngressoVip(Ingresso):
    def __init__(self, valor):
        self.valor = valor
        super().__init__(valor)

    def imprimeValor(self):
        self.valorAdicional = self.valor + (self.valor * 0.5)
        print(f"O valor do ingresso vip é {self.valorAdicional}")