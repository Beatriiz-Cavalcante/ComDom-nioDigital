def soma(*num):
    print(num)
    soma=0
    for c in range(0,len(num)):
        soma = soma + num[c]
    print(soma)

def texto(bla):
    '''Conta caracteres e printa do final para o início'''
    tamanho = len(bla)
    vazio = 0
    caracteres = ",.;:!?"
    for x in range(tamanho):
        print(bla[x], end=" ")
        if bla[x] == ' ':
            vazio=vazio+1
        elif bla[x] in caracteres:
            vazio = vazio + 1
    tamanhof = tamanho - vazio
    print(f'\n{tamanhof}')
    for x in range(len(bla)-1,-1,-1):
        print(bla[x], end=' ')

def novaLista(lista):
    '''faça um função que recebe uma lista como argumento e crie uma nova lista, somente com números únicos.'''
    novaL=[]
    print(lista)
    for c in lista:
        if c not in novaL:
            novaL.append(c)
    print(novaL)

def unico(n):
    novaLista=set(n)
    #set é uma variável composta chamada de conjunto. Que ordena naturalmente os números crescentemente e sem repetições
    print(novaLista)

def primos(num):
    '''Faça uma função que recebe um número como parâmetro e verifique se este número é primo'''
    if num==1:
        return num,"Não é primo"
    elif num==2:
        return num, "É primo"
    else:
        for x in range(2,num):
            if num%x==0:
                return num, "Não é primo"
        return num, "É primo"
