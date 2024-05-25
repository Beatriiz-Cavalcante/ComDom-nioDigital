'''faça um código wur trceba o valor de base e da altura de um triângulo e calcule a sua área. Usando a formula
a= (base x altura)/2'''

i = 0
while i !=3:
    i = int(input("Que fazer o calculo de qual forma geométrica?\n1-Triangulo\n2-Quadrado\n3-Encerrar o programa\n"))
    if i !=1 and i!=2 and i!=3:
        print("Número inválido. Tente outra vez!")
        i = int(input("Que fazer o calculo de qual forma geométrica?\n1-Triangulo\n2-Quadrado\n3-Encerrar o programa\n"))
    elif i == 1:
        print("Calculo da área do triângulo")
        altura = float(input("Digite o valor da altura: "))
        base = float(input("Digite o valor da base: "))
        areaT = (base * altura)/2
        print(f"A área do triangulo é: {areaT}")

    elif i == 2:
        print("Calculo da área do quadrado")
        lado = float(input("Digite o valor do lado: "))
        areaQ = lado ** 2
        print(f"A área do quadrado é {areaQ}")
    else:
        print("Programa encerrado")