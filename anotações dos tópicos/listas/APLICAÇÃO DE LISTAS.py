"""
APLICAÇÃO DE LISTAS

As listas em python são vetores e matrizes (arrays) são dinâmicas,
ou seja, não há limitação quanto ao tipo dos dados.

Linguagem C/java: Arrays
    - Possuem tamanho e categoria de dado fixo:
    Ou seja, nestas linguagens, a criação de arrays terá tipo int. E 5 ‘bytes’ de memória ocupados

Python:
    O alocamento da memória é dinâmico, pois não possui tamanho fixo
    Ou seja, apenas criamos a lista e adicionamos elementos
    Esta característica dispensa, exemplo, a necessidade da função 'malloc' do C.

    Qualquer categoria de dado: ou seja, pode ser ‘strings’, inteiros, floats e booleanos.
"""

lista1 = [1, 99, 5, 8, 23, 4, 1, 44, 43, 38]
lista2 = ['g', 'e', 'k', ' ', 'u', 'M', 'h', 'V', 'R', 'S', 'i', 'T']
lista3 = []
lista4 = [True, False, False, True, True, True, False, True]

print(type(lista1))
print(type(lista2))
print(type(lista3))
print(type(lista4))
i = int(input('digite um valor de 1 a 4: \n'))

if i == 1:
    j = int(input('digite quantos termos da lista devem ser mostrada: \n'))
    for num in range(0,j):
        if j >= len(lista1):
            print('o valor em questão é maior que os {} termos da lista{}, tente novamente.'.format(len(lista1),i))
            break
        print(lista1[num], end = '; ')

elif i == 2:
    j = int(input('quantos termos acessar? \n'))
    for num in range(0,j):
        if j >= len(lista2):
            print('o valor em questão é maior que os {} termos da lista{}, tente novamente.'.format(len(lista2),i))
            break
        print(lista2[num], end = '; ')

elif i == 3:
    j = int(input('quantos termos acessar? \n'))
    for num in range(0,j):
        if j >= len(lista3):
            print('o valor em questão é maior que os {} termos da lista{}, tente novamente.'.format(len(lista3),i))
            break
        print(lista3[num], end = '; ')

elif i == 4:
    j = int(input('quantos termos acessar? \n'))
    for num in range(0,j):
        if j >= len(lista4):
            print('o valor em questão é maior que os {} termos da lista{}, tente novamente'.format(len(lista4),i))
            break
        print(lista4[num], end = '; ')

else:
    print('digite outro valor e tente novamente \n')