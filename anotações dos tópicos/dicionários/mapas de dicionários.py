receita = {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 250}

'''
Mapas -> Conhecidos em Python como dicionários

iteraveis -> são objetos que podem ser iterados
iterações sobre dicionários -> percorremos os pares chave-valor

# printa a chave
for chave in receita:
    print(chave)

# printa o valor
for chave in receita:
    print(receita[chave])

# printa todas as chaves.
for chave in receita.keys():
    print(chave)

# printa todos os valores.
for value in receita.values():
    print(value)
'''

print(receita.items())  # retorna um objeto do tipo list

for chave, valor in receita.items():
    print(chave, valor)

# soma, valor máximo, valor mínimo e tamanho

print(sum(receita.values()))

print(max(receita.values()))

print(min(receita.values()))

print(len(receita))
