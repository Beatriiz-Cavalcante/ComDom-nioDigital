from classes import *

p1 = Pessoa("Triz", 60, 22)
p2 = Pessoa("Bea", 64, 22)

#print(p1.nome) antes do ponto o nome do objeto e depois do ponto o atributo ou método a ser utilizado
print("Pessoa 1\n")
p1.comer("Coxinha", "coquinha")
p1.pararDeComer()
p1.falar()
p1.dormir()

print("\nPessoa 2\n")
p2.falar()
p2.dormir()
p2.comer("Uva", "água")