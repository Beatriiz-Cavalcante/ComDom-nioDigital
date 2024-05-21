'''para herança se coloca a classe mãe como parâmentro da classe filha. Nesse exemplo isso indica que gato e as demais classes
são subclasses da classe animal. O super é usado para que os métodos também possam ser acessados e herdados'''

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"O {self.nome} foi miando...")

#Complete esse exercício sobre herança, criando as classes cachorro, ccoelho e vaca, herdando da classe animal

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} foi latindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def grunhir(self):
        print(f"O {self.nome} foi grunhindo...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"O {self.nome} foi mugindo...")