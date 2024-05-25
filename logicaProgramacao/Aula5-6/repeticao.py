numero = int(input("Digite um número: "))
for c in range (1,numero+1,1):
    for c2 in range(1, c+1):
        print(c, end=" ")

#outra forma de fazer (manipulaçao de string)

n = int(input("\nDigite um número"))
for x in range(1,n+1):
    print( x * str(x), end=" \n")

#brincando com as linhas
numero = int(input("\nDigite um número: "))
for c in range (1,numero+1,1):
    for c2 in range(c):
        print(c, end=" ")
    print()