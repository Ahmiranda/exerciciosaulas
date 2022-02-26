# EXEMPLO DE LISTA UTILIZANDO ITERAÇÕES WHILE

carrinho = [] # lista vazia
produto = ''  # variável tipo string

while produto != 'sair':
    print("Adicione um produto ou digite 'sair' para sair.")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)


for produto in carrinho:
    print(produto)