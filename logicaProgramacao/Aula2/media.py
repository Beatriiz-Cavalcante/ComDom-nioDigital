nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2)/2

if media>=5:
    if media >=7:
            print("Situação aprovado")
    else:
        print("Recuperação")   
else:
    print("Situação Reprovado")
