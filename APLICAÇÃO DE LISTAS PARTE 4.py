# variáveis em listas

numeros = [1, 2, 3, 4 , 5]
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
print(numeros)
numeros = [n1, n2, n3, n4, n5]
print(numeros)


# fazemos acessos de forma indexada nas listas, posição 0, 1, 2, 3
cores = ['azul', 'verde', 'amarelo', 'branco', 'lilás']
print(cores[2])  # amarelo
print(cores[-2]) # branco
print(cores[1])  # verde
print(cores[-1]) # lilás
# o indice dos elementos na lista é ciclico, se for além da quantidade, passa a repetir os elementos

# o comando list(enumerate(cores))) gera uma lista onde cada elemento é uma dupla ordenada da posição
# e o elemento da posição da lista
print(list(enumerate(cores)))

# apresentando o indice e o valor na posição do vetor sem o recurso da lista
# utilizando ‘loop’ for
for indice, cor in enumerate(cores):
    print (indice, cor)

# encontrar o indice de um elemento em uma lista

numeros = [5, 6, 8, 9, 10, 7]
print(numeros.index(6))
print(numeros.index(7))

# com o comando index, ele vai indicar o conteúdo da posição indicada
# caso a posição indicada não esteja definida dentro da lista, ela retorna erro
print(numeros.index(8)) # valueError: 17 is not in list

# o comando index retorna o primeiro elemento encontrado dentro da lista, podendo haver repetições adiante
# podemos buscar em um range na lista, com indices de onde encontrar e terminar a busca

print(numeros.index(10, 1)) # busca o elemento 10 a partir do indice 1
print(numeros.index(10, 2)) # busca o elemento 10 a partir do indice 2
# caso a posição indicada não esteja definida na lista, ela retorna erro

# esse material foi parado no vídeo 32.listas no tempo 1:50:04 de 2:21:37
