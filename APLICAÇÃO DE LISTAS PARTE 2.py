lista5 = list('geek university')
lista1 = [1, 99, 5, 8, 23, 4, 1, 44, 43, 38]
if 'e' in lista5:
    print('encontrei o "e"')
else:
    print('Não encontrei o "e"')

# Ordenar uma lista com o comando sort

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Podemos também contar o número de ocorrências de um valor dentro de uma lista
print('Há {} números 1'.format(lista1.count(1)))
print('Há {} letras "e"'.format(lista5.count('e')))

# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append
"""

lista1.append(42)
print(lista1)

# o comando append adiciona apenas um elemento por vez
# fazer o comando append([1, 2, 3]) adiciona a lista como elemento, e não os elementos

lista1.extend([123, 44, 67])
print(lista1)
# o comando extend adiciona os elementos da lista que possui no argumento à lista em que este é associado
# a adição de elementos é feita de maneira individual

# podemos inserir um novo elemento na lista informando a posição na lista, também.

lista1.insert(2,'novo valor')
print(lista1)
# o comando insert não substitui valores, ele insere o novo valor na posição da lista e desloca os demais para a direita

# podemos também juntar duas listas em conjunto, da seguinte forma:
lista6 = lista1 + lista5
print(lista6)
lista7 = lista5 + lista1
print(lista7)
# a ordem da soma das listas é a ordem em que serão inseridas na nova lista
lista1.extend(lista5)
print(lista1)
# é recomendável que a soma seja usada para a criação de nvoas listas, enquanto o comando extend
# seja utilizado para a incrementação / atualização de listas já declaradas

# forma 1
lista1.reverse()
lista5.reverse()
print('lista 1:\n {}\n lista 2:\n{}\n '.format(lista1,lista5))

# forma 2
# segunda forma de reverter a lista: comando slice (essa coisa veio de strings)
print(lista1[::-1])
print(lista5[::-1])
# este passo a cima, reverteu o comando reverse da instrução anterior

#comando para copiar lista: copy
print('lista copiada')
lista4 = lista5.copy()
print(lista4)

# identificar o tamanho da lista
print('tamanho da lista')
print(len(lista4))

# podemos remover o último elemento de uma lista comando: pop
print('remoção de elemento')
print(lista4)
lista4.pop()
print(lista4)
print(lista4.pop())
# OBS: o comando pop não só remove o último elemento mas também o retorna que elemento foi removido
# podemos remover o elemento pelo indice na lista
print('operação com a lista 5')
print(lista5)
print(lista5.pop(2))
print(lista5)

# podemos remover todos os elementos
print('nova operação lista 6')
print(lista6)
lista6.clear()
print(lista6)

# podemos repetir elementos dentro de uma lista
print('nova lista')
novalista = [1,2,3]
novalista = novalista * 3
print(novalista)

# conversão de string para lista
curso = 'curso de programação em python'
print('exemplo 1 do split')
print(curso)
print(type(curso))
curso = curso.split()
print(type(curso))
print(curso)

# exemplo 2
print('exemplo 2 do split')
curso2 = 'curso,de,programação,em,python'
print(curso2)
curso2 = curso2.split(',') #digo que o separador é a virgula
print(curso2)
# este recurso do comando split é interessante para trabalhar com arquivos .text .csv e .json
# esse material foi parado no vídeo 32.listas no tempo 1:07:00 de 2:21:37

# convertendo uma lista em string (processo contrário do comando split)

# vai colocar espaço entre cada elemento da lista e juntar numa string

# comando join
print('comando join')
curso = ' '.join(curso2)
print (curso)

stringdalista2 = '$'.join(curso2)
print(stringdalista2)
# esse material foi parado no vídeo 32.listas no tempo 1:15:00 de 2:21:37

# uma lista suporta qualquer tipo de dado no seu interior, inclusive misturando dados
lista3 = [1, 2.45, True, 'Geek', 'd', [1,2,3], 563434]

print(lista3)
print(type(lista3))

# iterando sobre listas
# exemplo 1
lista1 = [1, 99, 5, 8, 23, 4, 1, 44, 43, 38]
soma = 0
for elemento in lista1:
    soma = soma + elemento
    print(soma)

