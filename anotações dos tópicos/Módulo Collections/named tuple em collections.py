'''
Named tuples -> são tuplas diferenciadas, onde cada elemento possui um nome.
'''

from collections import namedtuple
# FORMA 1 - Criando um named tuple
carro = namedtuple('carro', 'marca modelo ano')
# FORMA 2 - Criando um named tuple
carro2 = namedtuple('carro2', 'marca, modelo, ano')
# FORMA 3 - Criando um named tuple
carro3 = namedtuple('carro3', ['marca', 'modelo', 'ano'])

veiculo = carro3('Ford', 'Fiesta', 2015)

print(veiculo)
print(veiculo.marca)
print(veiculo.modelo)
print(veiculo.ano)

print(veiculo[0])
print(veiculo[1])
print(veiculo[2])

print(veiculo.index('Ford'))

