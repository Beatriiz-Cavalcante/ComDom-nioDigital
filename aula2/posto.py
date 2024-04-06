print("Qual o combustível escolhido?\n1-Gasolina\n2-Etanol")
combustivel = int(input(""))

if combustivel == 1:
    combustivel = 'gasolina'
    litros_gasolina = float(input("Quantos litros de gasolina foi comprado? "))
    precoG = litros_gasolina * 5.80
    print(f'O preço da {combustivel} é R$5.80. Logo sua conta é: R${precoG}')
elif combustivel == 2:
    combustivel = 'etanol'
    litros_etanol = float(input("Quantos litros de etanol foi comprado?"))
    precoE = litros_etanol * 4.90
    print(f'O preço da {combustivel} é R$5.80. Logo sua conta é: R${precoE}')
elif combustivel !=1 and combustivel!=2:
    print('Número inválido!')