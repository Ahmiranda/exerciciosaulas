# variáveis em listas
'''
numeros = [1, 2, 3, 4, 5]
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
print(cores[-2])  # branco
print(cores[1])  # verde
print(cores[-1])  # lilás
# o indice dos elementos na lista é ciclico, se for além da quantidade, passa a repetir os elementos

# o comando list(enumerate(cores))) gera uma lista onde cada elemento é uma dupla ordenada da posição
# e o elemento da posição da lista
print(list(enumerate(cores)))

# apresentando o indice e o valor na posição do vetor sem o recurso da lista
# utilizando ‘loop’ for
for indice, cor in enumerate(cores):
    print(indice, cor)

# encontrar o indice de um elemento em uma lista

numeros = [5, 6, 8, 9, 10, 7]
print(numeros.index(6))
print(numeros.index(7))

# com o comando index, ele vai indicar o conteúdo da posição indicada
# caso a posição indicada não esteja definida na lista, ela retorna erro
print(numeros.index(8))  # valueError: 17 is not in list

# o comando index retorna o primeiro elemento encontrado na lista, podendo haver repetições adiante
# podemos buscar em um range na lista, com indices de onde encontrar e terminar a busca

print(numeros.index(10, 1))  # busca o elemento 10 a partir do indice 1
print(numeros.index(10, 2))  # busca o elemento 10 a partir do indice 2
# caso a posição indicada não esteja definida na lista, ela retorna erro

# esse material foi parado no vídeo 32.listas no tempo 1:50:04 de 2:21:37

('\n'
 'resumo\n'
 '\n'
 'REVISÃO DE SLICING\n'
 'lista[inicio, fim, passo]\n'
 'range[inicio, fim, passo]\n'
 '\n'
 'lista = [1, 2, 3, 4]\n'
 '\n'
 'print(lista[::])  # inicia do indice 0 até o último termo\n'
 '\n'
 'print(lista[:2]) # começa do zero e vai até o indice 2\n'
 '\n'
 'print(lista[:4]) # começa do zero e vai até o indice 4\n'
 '\n'
 'print(lista[1:3]) # começa do indice 1 até o 3\n'
 '\n'
 '# é possível passar valores negativos pois as listas funcionam de maneira ciclica\n'
 '\n'
 'print(lista[-1]) equivale a print(lista[3])\n'
 '\n'
 '# é possível controlar o passo de avanço\n'
 '\n'
 'print(lista[1::2]) pula de 2 em 2 a partir do indice 1. vai mostrar os termos com indice impar\n'
 '\n'
 'print(lista[::2]) pula de 2 em 2 a partir do indice 0. mostra os termos de indice par\n'
 '\n'
 'print(lista[::-1] pula de -1 em -1 na lista, mostrando a mesma de trás para frente\n'
 '\n')
 
 'se uma lista possui valores de tipo ponto flutuante ou interios podemos encontrar \n'
 soma           : print(sum(lista))
 valor máximo   : print(max(lista))
 valor mínimo   : print(min(lista))
 tamanhho       : print(len(lista))
 
 'conversão de uma lista em tuplas \n'
 lista = [1, 2, 3, 4 , 5, 6]\n
 print(type(lista))\n
 print(lista)
 
 tupla = tuple(lista)
 print(type(tupla)
 print(tupla)
 

### desempacotamento de listas

num1, num2, num3 = lista
OBS: o numero de variáveis para desempacotamento deve ser igual ao tamanho da lista, senão haverá ValueError no processo


# copiando uma lista para a outra: Shallow Copy e Deep Copy

# forma 1: deep copy
lista2 = [1, 2, 3]

print(lista2)

nova = list.copy(lista2)
print(nova)
nova.append(4)
print(nova)
print(lista2)
# OBS: A utilização do comando .copy() gera uma lista nova e independente, sem vínculos com a anterior
# em Python, tal recurso é chamado Deep Copy


# forma 2: Shallow Copy
lista = [1, 2, 3]
print(lista)
nova = lista #copia
print(nova)
nova.append(4)
print(nova)
print(lista)

# OBS: ao utilizar a copia via atribuição, copiamos os dados da lista anterior para a nova, porém, ao realizar
# modificações em uma das listas, isto infere na outra lista.
# tal comportamento é chamado em python de shallow copy

'''


