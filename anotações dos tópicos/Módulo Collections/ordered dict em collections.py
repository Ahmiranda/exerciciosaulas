'''
Em um dicionário, a ordem de inserção dos elementos não é garantida.

OrderedDict -> é um dicionário que mantém a ordem de inserção dos elementos.
'''

from collections import OrderedDict
dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

for chave, valor in dicionario.items():
    print(chave, valor)

dicionario = OrderedDict(dicionario)

for chave, valor in dicionario.items():
    print(chave, valor)

dicionario2 = {
    'd': 4,
    'e': 5,
    'a': 1,
    'b': 2,
    'c': 3,

}

print(dicionario2 == dicionario)  # a ordem dos elementos não importa para os dicionários
dicionario2 = OrderedDict(dicionario2)  # ao ordenar os elementos, a ordem passa a importar
dicionario = OrderedDict(dicionario)
print(dicionario2 == dicionario)  # Os elementos são ordenados de acordo com a ordem de inserção
print(dicionario2)