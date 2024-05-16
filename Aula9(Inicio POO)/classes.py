#Nomeclatura padrão
'''
classes pascalcase - PrimeiroNome
métodos camelcase  - primeiroNome
Criação
classe tem a palabra reservada class + nome:
constutores tem a palavra reservada __init__
'''

class Pessoa():
    def __init__(self, nome, peso, idade, comendo=False, dormindo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def comer(self, comida, bebida):
        self.comendo = True
        if self.comendo == True:
            print(f"{self.nome} foi comer {comida} e tomar {bebida}")
        elif self.dormindo == True:
            print("Você não pode comer domindoo")
        elif self.falando == True:
            print("Para de falar e depois coma!")
        else:
            print("Não estou comendo")

    def dormir(self):
        self.dormindo == True
        if self.comendo == True:
            print("Você tem que parar de comer para dormir!")
        elif self.falando == True:
            print("Você tem que parar de falar para dormir")
        else:
            print(f"{self.nome} está no maior ronco")
    def falar(self):
        self.falando == True
        if self.comendo == True:
            print("Eca, não fale de boca cheia!")
        elif self.dormindo == True:
            print("Caraca, você é sonambulo")
        else:
            print(f"{self.nome} não gosta muito de falar.")