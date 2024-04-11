'''Ler 10 notas, calcular e escrever a média aritmética.
devem estar entre 0 - 10. Se não estiver nesse intervalo o valor não é considerado.
'''
soma = 0
divisor = 0
media = 0
for c in range (10):
    numero = float(input("Digite um número: "))
    if numero>=0 and numero<=10:
        divisor += 1
        soma += numero
        print(divisor)
        print(soma)
        media = soma / divisor

if divisor != 0:
   print(media)
else:
    print("notas inválidas")