'''crie uma classe chamada forma, que possui os atributos area e perímetro
-Implemente as subclasses retangulo e triangulo, que devem conter os métodos calculaarea e calcula perimetros. A classe
triangulo deve ter também o atributo altura.
-No código de teste crie um objeto da classe triangulo e outro da classe retangulo, calcule q area de cada um
'''

class Forma():
    def __init__(self):
        self.area = 0.0
        self.perimetro = 0.0


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self,base, altura):
        self.area = (base * altura)/2
        print(f"A área do triangulo de base {base}e altura {altura} é {self.area}")

    def calcularPerimetro(self, base, altura):
        self.perimetro = 2 *(base+altura)
        print(f"O perímetro do triangulo de base {base}e altura {altura} é {self.perimetro}")

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, base, altura):
        self.area = base * altura
        print(f"A área do retangulo de base {base} e altura {altura} é {self.area}")

    def calcularPerimetro(self, base, altura):
        self.perimetro = 2 * (base + altura)
        print(f"O perímetro do retangulo de base {base}e altura {altura} é {self.perimetro}")
