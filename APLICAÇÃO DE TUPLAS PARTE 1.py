'''
TUPLAS: TUPLE

As tuplas são semelhantes às listas, as diferenças básicas são:
    1. as tuplas são representadas por parenteses. ()
    2. as tuplas são imutáveis, qualquer tentativa de modificação vai gerar uma nova tupla com as propriedades da modificação.

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

# DESEMPACOTAMENTO DE TUPLA
    tupla = 1, 2
    num1, num2 = tupla
OBS: o número de variáveis para o desempacotamento deve ser igual ao tamanho da tupla, senão retorna ValueError

# SOMA, VALOR MÁXIMO, VALOR MÍNIMO E TAMANHO
print(len(tuplas))
print(min(tuplas))
print(max(tuplas))
print(sun(tuplas))

# parada no min 26:16 do vídeo 33. tuplas

'''