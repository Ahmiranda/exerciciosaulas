"""
filter

filter() -> Serve para filtrar dados de uma determinada coleção.

"""

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f'Média: {media}', "de", dados)

filter(lambda x: x > media, dados)
filtro = (filter(lambda x: x > media, dados))
print(f'Valores acima da média: {list(filtro)} de {dados}, {type(filtro)}')

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
print(list(res) , "sem lambda")

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res), "com lambda")


# exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios, "lista de dicionários")

# Filtrar os usuários que estão inativos no Twitter

# Forma 1

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos, "forma 1")   # forma 1

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos, "forma 2")   # forma 2

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome};', filter(lambda nome: len(nome) < 5, nomes)))
print(lista[0], "combinando filter e map")