# Dicionários - mapas (em outras linguagens)
# dicionários são coleções do tipo chave-valor

print(type({}))  # retorna a classe dict

paises = {'br': "Brasil", 'US': "Estados unidos", 'JP': "Japão", 'UK': "Reino Unido"}
print(paises)
print(type(paises))
print(paises['br'])
print(paises['US'])
# os dicionários possuem estrutura 'chave':'valor'
# não há limitações sobre as categorias de dados empregados
# podemos misturar categorias de dados
# se tentamos acessar uma chave que não existe, o programa retorna um erro (KeyError)

# forma recomendada para acessar um dicionário

print(paises.get('br'))  # retorna o valor da chave 'br'
print(paises.get('ru'))  # retorna None (não existe a chave 'ru')
print(paises.get('ru', 'Não encontrado'))  # retorna 'Não encontrado' (não existe a chave 'ru')

# o método get() é utilizado para acessar um dicionário
# o método get() recebe como parâmetro a chave que desejamos acessar
# se a chave existir, o método retorna o valor associado à chave
# se a chave não existir, o método retorna o valor padrão passado como segundo parâmetro
# se não passarmos um segundo parâmetro, o método retorna None

print('br' in paises)  # retorna True (existe a chave 'br')
print('ru' in paises)  # retorna False (não existe a chave 'ru')
print('Estados unidos' in paises)  # retorna False (não existe a chave 'Estados unidos')

# o método keys() retorna um objeto do tipo set
# o método keys() retorna um conjunto de chaves do dicionário
# o método keys() não recebe nenhum parâmetro

print(paises.keys())  # retorna um conjunto de chaves do dicionário
print(type(paises.keys()))  # class 'dict_keys'

localidades = {
    ('br', 'SP'): 'São Paulo',
    ('br', 'RJ'): 'Rio de Janeiro',
    ('br', 'MG'): 'Minas Gerais',
    ('br', 'BA'): 'Bahia'
}
localidades2 = {
    (35.6875, -5.8): 'Tanger',
    (40.4167, 6.645): 'Madrid',
    (41.3833, 2.1833): 'Barcelona',
}
print(localidades)
print(localidades2)

receita = {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 250} # ADICIONANDO DADOS AO DICIONÁRIO
# forma 1 - MAIS COMUM
receita['mai'] = 500
print(receita)

# forma 2 - MAIS EFICIENTE
receita.update({'jun': 450, 'jul': 600})
print(receita)

# conclusão 1: a forma de adicionar elementos ou atualizar dados é a mesma
# conclusão 2: Em dicionários, não podemos adicionar chaves duplicadas
# conclusão 3: O método update() recebe como parâmetro um dicionário
# conclusão 4: O método update() não retorna nada

# remover dados de um dicionário
# o método pop() remove um elemento do dicionário
# o método pop() recebe como parâmetro a chave do elemento que desejamos remover
# o método pop() retorna o valor associado à chave removida

retorno = receita.pop('jan')
# OBS 1: se tentarmos remover um elemento que não existir, o programa retorna um erro (KeyError)
# OBS 2: ao remover um elemento, o valor associado é retornado.
print(retorno)
# OBS 3: ao remover um elemento já removido, o programa retorna um erro (KeyError)

del receita['fev']
# OBS 3: Neste caso. não há um retorno do método
print(receita)

# o método clear() remove todos os elementos do dicionário
receita.clear()
print(receita)

# o método copy() retorna uma cópia do dicionário
b = localidades.copy()
print(b)

# o método fromkeys() retorna um dicionário com chaves e valores padrão
# o método fromkeys() recebe como parâmetro um iterável e um valor padrão
c = dict.fromkeys(['a', 'b', 'c'], 'valor padrão')
print(c)
