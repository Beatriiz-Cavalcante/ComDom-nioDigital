'''Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10, 20]
(incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo
'''
cDentro = 0
cFora = 0

for c in range(1,11, 1):
    numero = int(input("Digite um número: "))
    if numero >= 10 and numero <=20:
        cDentro = cDentro + 1
        print("Michelle")
    else:
        cFora = cFora + 1
    print(cFora)
    print(cDentro)

print(f'Dos números dados. {cDentro} estão entre 10-20 e {cFora} estão fora')
