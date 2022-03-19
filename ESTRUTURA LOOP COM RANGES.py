"""
PRECISAMOS ENTEDNER O LOOP FOR PARA USAR OS RANGES
PRECISAMOS ENTENDER OS RANGES PARA TRABALHAR MELHOR COM LOOP FOR

RANGERS são utilizados para gerar sequências numéricas de forma não aleatória,
mas sim de maneira controlada e especificada

formas gerais:

range(valor_de_parada)
OBS: valor de parada não é incluso do intervalo
(inicio padrão 0, passo a cada 1)

"""

# forma 1
amplitude = 11

for num in range(amplitude):
    print(num, end=' ')
print('\n')
# FORMA 2 range(valor_de_inicio, valor_de_parada)
for num in range(1, amplitude):
    print(num, end=' ')

# FORMA 3 range(valor_de_inicio, Valor_de_parada, passo)
# OBS: valor_de_parada inclusive (inicio especificado pelo utilizador, passo especificado pelo utilizador)
print('\n')
for num in range(1, amplitude, 2):  # imprime valores ímpares
    print(num, end=' ')

print('\n')
for num in range(0, amplitude, 2):  # imprime valores pares
    print(num, end=' ')

# FORMA 4: (INVERSA) semelhante à forma 3, mas invertendo a ordem das instruções
# range(valor_inicial, valor_de_parada, passo)
print('\n')
for num in range(amplitude, 0, -1):
    print(num, end=' ')
print('\n')
lista = list(range(15))
print(lista)
