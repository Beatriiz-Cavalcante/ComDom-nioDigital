'''Usando a função estoque que acabamos de criar, faça um código que cadastre os nomes dos produtos num array produtos, 
valor unitário em um array valorunitário e o retoro da função estoque no array valortotal. Depois print os 3 arrays 
para mostrar que tudo foi registado'''


produtos = []
valor_unitario = []
valor_total = []
def valorEstoque(produto, quantidade, valorU):
    cadastro = 1
    while cadastro ==1:
        produto = input("Digite o nome do produto: ")
        valorU = input("Digite o nome do produto: ")
        quantidade = int (input("Digite a quantidade: "))
        produtos.append(produto)
        valor_unitario.append(valorU)
        valorT = valorU * quantidade
        valor_total.append(valorT)
        return valor_total

