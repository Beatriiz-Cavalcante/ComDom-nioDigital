from funcoes import imprimeNome, repeticao, repeticaoPorLinha, contaVogal
from funcoes2 import valorEstoque

'''para chamar funções de outro arquivo é necessário importar a função e dizer em qual arquivo ele está, como no exemplo acima'''
'''Se colocar * importa todas as funções que estiverem dentro do arquivo'''

x = input("Qual o seu nome? ")
imprimeNome(x)

numero = int(input("Digite o número limite: "))
repeticao(numero)
print( )
repeticaoPorLinha(numero)

recebeTexto = input("Digite um texto")
contaVogal(recebeTexto)

recebeProduto = input("Digite o nome do produto: ")
recebeQuantidade = int(input("Digite a quantidade do produto em estoque: "))
recebeValor = float(input("Digite o valor do produto: "))
valorEstoque(recebeProduto,recebeQuantidade,recebeValor)

#para o caso de função com retorno
'''retornoEstoque = valorEstoque(recebeProduto,recebeQuantidade,recebeValor)
print(retornoEstoque)'''
