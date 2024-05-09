def imprimeNome(nome):
    print(f"Nome:{nome}")

def repeticao(nuremoLimite):
    for c in range(nuremoLimite+1):
        for i in range(1,c+1):
            print(c, end=' ')
        print()

def repeticaoPorLinha(nuremoLimite):
    for c in range(1, nuremoLimite+1):
        for i in range(1,c+1):
            print(i, end=' ')
        print()

def contaVogal(texto):
    z = 0
    tamanho= len(texto)
    contador = 0
    for x in range(tamanho):
        print(texto[x], end=" ")
        if texto[x] == ' ':
            z=z+1
    print()
    print(f'Tamanho {tamanho}')
    print(f'Espaços em branco: {z}')
    print(f'Quantidade de caracteres: {tamanho-z}')
    '''for c in range(tamanho):
        if texto[c] == 'a' or texto[c] == 'A':
            contador = contador + 1
        elif texto[c] == 'e' or texto[c] == 'E':
             contador = contador + 1
        elif texto[c] == 'i' or texto[c] == 'I':
             contador = contador + 1
        elif texto[c] == 'o' or texto[c] == 'O':
             contador = contador + 1
        elif texto[c] == 'u' or texto[c] == 'U':
             contador = contador + 1'''
    #Maneira inteligente de fazer
    for c in texto:
        if c in "aeiuoAEIOU":
            contador = contador + 1
    print(f'Quantidade de vogais: {contador}')

