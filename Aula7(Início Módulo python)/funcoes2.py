'''Crie uma função que recebe o nome de um produto , a quantidade que tem no estoque e o valor unitário do produto.
 Retorne o valor total do produto em estoque'''

def valorEstoque(produto,quantidade,valorU):
    total = float(quantidade) * valorU
    print()
    print(f'O valor total em estoque para o produto {produto} é {total}')
    print()

#função com retorno
'''def valorEstoque(produto, quantidade, valorU):
    total = float(quantidade) * valorU
    return total
'''