"""
MAP

com o "map" fazemos mapeamento de valores para a função

"""
from math import pi


def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return pi * (r ** 2)

values = [2, 5.3]

print(area(2))
print(area(5.3))

# forma comum
areas = []
for r in values:
    areas.append(area(r))

print(areas, "forma 1")

print(list(map(area, values)), "forma 2")

# Forma 2 - Map com lambda
print(list(map(lambda r: pi * (r ** 2), values)), "forma 3")
print(list(map(lambda r: pi * (r ** 2), [2, 5.3])), "forma 4", "tudo em uma linha")
# OBS: após utilizar a função map() depois da primeira utilização do resultado, ele zera

# Para fixar - Map
# Temos dados iteráveis:
# dados: a1, a2, ..., an



# conversão para fahrenheit

cidades = {
    'São Paulo': 32,
    'Rio de Janeiro': 25,
    'Curitiba': 13,
    'Salvador': 28,
    'Porto Alegre': 18,
    'Belo Horizonte': 21,
    'Fortaleza': 26,
    'Brasília': 29
}


def converter(temp):
    return (temp * 9/5) + 32


print(converter(cidades['São Paulo']))

print(list(map(converter, cidades.values())))
print(list(map(lambda temp: (temp * 9/5) + 32, cidades.values())))

print(list(map(lambda local, temp: [local, (temp * 9/5) + 32], cidades.keys(), cidades.values())))

