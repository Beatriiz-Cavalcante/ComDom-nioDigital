#Nomeclatura padrão
'''
classes pascalcase - PrimeiroNome
métodos camelcase  - primeiroNome
Criação
classe tem a palabra reservada class + nome:
constutores tem a palavra reservada __init__
'''

'''Fazer a classe pessoa de um modo que os métodos não possam ser chamados simultâneamente'''

class Pessoa():
    def __init__(self, nome, peso, idade, comendo=False, dormindo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.dormindo = dormindo
        self.falando = falando
#ativar
    def comer(self, comida, bebida):
        if self.dormindo == False and self.falando == False:
            self.comendo = True
            print(f"{self.nome} foi comer {comida} e tomar {bebida}")
        elif self.dormindo == True:
             print("Você não pode comer domindoo")
        elif self.falando == True:
            print("Para de falar e depois coma!")
            
    def dormir(self):
        if self.comendo == False and self.falando == False:
            self.dormindo = True
            print(f"{self.nome} está no maior ronco")
        elif self.comendo == True:
            print("Você tem que parar de comer para dormir!")
        elif self.falando == True:
            print("Você tem que parar de falar para dormir")

    def falar(self):
        if self.comendo == False and self.dormindo == False:
            self.falando = True
            print(f"{self.nome} não gosta muito de falar.")
        elif self.comendo == True:
            print("Eca, não fale de boca cheia!")
        elif self.dormindo == True:
            print("Caraca, você é sonambulo??")
            

#desativar
    def pararDeComer(self):
        if self.comendo == True:
            print("Já to acabando")
            self.comendo = False
        else:
            print("Quê? Mas eu não estou comendo...")

    def pararDeDormir(self):
        if self.dormindo == True:
            print("Calma, minha alma ta voltando para o corpo")
            self.dormindo = True
        else:
            print("To acordado. Só to descansando a vista")

    def pararDeFalar(self):
        if self.falando == True:
            print("Não ta mais aqui quem falou...")
            self.falando = False
        else:
            print("QUê? Mas eu estou calado!")