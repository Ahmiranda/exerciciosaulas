"""
ESTRUTURA LOOP FOR
Loop -> é uma estrutura de repetição
For -> é um tipo de estrutura de repetição

em C

for (int i=0; i< limitador; i++) {
    //estrutura ou instrução
}

em javascript

for (let i = 0; i < limitador; i++) {
    // estrutura ou instrução
}
#estrutua loop em python:

for item iterável:
    // estrutura ou instrução de repetição do loop


utilizamos loop para iterar sobre sequências ou valor iterável
ex: strings
    nome = 'curso de python'

listas
    lista = [1, 3, 5 ,7 ,9]

Range
    numeros = range(1, 10)

outros exemplos: contadores, ponteiros, vetores e matrizes

"""

nome = 'curso de python'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

#EXEMPLO 1 - iterando sobre uma string
for letra in nome:
    print(letra)

print('\n \n')
#EXEMPLO 2 - iterando sobre uma lista
for numero in lista:
    print(numero)

print('\n \n')
#EXEMPLO 3 - interando sobre um range
for numero in range(1, 10):
    print(numero)
# obs, quando trabalhamos com range, o valor inicial é incluido mas no valor final, não,
# strings podem ser mostradas neste formato, também


print('\n \n')
for i, v in enumerate(nome):
    print(nome[i])
"""
enumerate 
(0, 'c'), (1, 'u'), (2, 'r'), (3, 's'), ...
"""

# outra forma para reescrever o loop do for com o enumerate
print('\n \n')
for _, letra in enumerate(nome):
    print(letra)

"""
Quando não precisamos de um valor em uma instrução, podemos descartar-lo utilizando um underline '_'
"""
#impressão da tupla

for valor in enumerate(nome):
    print(valor)

print('\n \n')
quant = int(input('Quantas vezes o loop deve rodar?'))

for i in range(1, quant + 1):
    print('imprimindo{}'.format(i), end=' ')


