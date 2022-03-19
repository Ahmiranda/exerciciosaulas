"""
TUPLAS: TUPLE

As tuplas são semelhantes às listas, as diferenças básicas são: 1. As tuplas são representadas por parenteses. () 2.
as tuplas são imutáveis, qualquer tentativa de modificação vai gerar uma nova tupla com as propriedades da modificação.

OBS: escrever:
    tupla1 = (1, 2, 3, 4, 5, 6, 7)
    tupla2 = 1, 2, 3, 4, 5, 6, 7
    dá na mesma, o compilador vai reconhecer ambos como tuplas

# cuidado: tuplas com 1 elemento
    tupla3 = (4) # isso não é uma tupla, é um inteiro
    tupla4 = (4,) #isso é uma tupla.
# conclusão: podemos definir que tuplas são definidas pela vírgula, e não o uso do parenteses
    (4) não é tupla
    (4,)    é tupla
    4,      é tupla

# Podemos gerar uma tupla dinamicamente com o range.
tuplas = tuple(range(11)) gera uma tupla com elementos de 0 a 10

# DESEMPACOTAMENTO DE TUPLA:
    tupla = 1, 2
    num1, num2 = tupla
OBS: o número de variáveis para o desempacotamento deve ser igual ao tamanho da tupla, senão retorna ValueError

# SOMA, VALOR MÁXIMO, VALOR MÍNIMO E TAMANHO
print(len(tuplas))
print(min(tuplas))
print(max(tuplas))
print(sun(tuplas))

# combinação de tuplas
se tupla1 = 1, 2, 3
tupla2 = 4, 5, 6
tupla3 = tupla1 + tupla2
tupla3 = 1, 2, 3, 4, 5, 6


#iterando em tuplas
tuplas = 1, 2, 3, 4, 5, 6
for n in tuplas:
    print(n)

for indice, valor in enumerate(tuplas):
    print(indice, valor)

 #iteração com while
i = 0
meses = (
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro',
    'dezembro')
while i < len(meses):
    print(meses[i])
    i = i + 1


# contagem de elementos em uma tupla

tupla = ('a','b','c','d','e','f','a','a','f')
print(tupla.count('f'))

# contagem de elementos em uma tupla
escola = tuple('escola de matemática física e química')
print(escola)
print(escola.count('a'))

#dicas na utilização de tuplas

# devemos utilizar tuplas sempre em que a base de dados não deve ser modificada, exemplos meses = ('janeiro',
'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
dias_da_semana = ('domingo','segunda','terça','quarta','quinta','sexta','sábado')

print(meses.index('junho',3))

# porque utilizar tuplas?

1. tuplas são mais rápidas que as listas
2. o seu código fica mais seguro ao utilizar tuplas

tuplas não geram shallow copy, ou seja
tupla(1, 2, 3, 4)
nova = tupla

# essa operação com tuplas não gera um vínculo entre a anterior e a nova tupla

"""
