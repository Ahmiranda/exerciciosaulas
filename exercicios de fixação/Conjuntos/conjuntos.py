'''
Conjuntos

os conjuntos em python são chamados de Sets.
possuem as mesmas propriedades que os conjuntos na matemática e se estendem a todas as linguagens de programação.

1. Sets não possuem valores duplicados.
2. Sets não possuem valores ordenados.
3. Elementos não são acessados por índices, OU SEJA, Sets não são indexados.
4. Sets possuem qualquer tipo de dado.
5. Sets são iteráveis.
6. Sets são mutáveis.


Conjuntos são bons para armazenar valores que não precisam de ordenação.

os conjuntos em python são definidos com chaves {}

as diferenças entre conjuntos (Sets) e dicionários (Maps) são:
    - um dicionário possui chaves e valores
    - um conjunto (Set) possui apenas valores'''

# definindo um conjunto:
conjunto = {1, 2, 3, 4, 5, 1, 4, 7, 10}
print(conjunto)
print(type(conjunto))  # retorna um objeto do tipo set

# OBS: os conjuntos não possuem valores duplicados, se eles tiverem valores duplicados, o valor extra será removido.

string = 'abcdefghijklmnopqrstuvwxyz'
a = set(string)  # cria um conjunto a partir de uma string
print(a)
print(type(a))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = set(lista)  # cria um conjunto a partir de uma lista
print(b)
print(type(b))


tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
c = set(tupla)  # cria um conjunto a partir de uma tupla
print(c)
print(type(c))

if 3 in c:
    print('3 está no conjunto')
else:
    print('3 não está no conjunto')


lista = [143, 2, 3, 4, 55, 6, 7, 55, 8, 9, 10]
print(f'lista: {lista} com {len(lista)} elementos')
tupla = 143, 2, 3, 4, 55, 6, 7, 55, 8, 9, 10
print(f'tupla: {tupla} com {len(tupla)} elementos')
conjunto = {143, 2, 3, 4, 55, 6, 7, 55, 8, 9, 10}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos')
dicionario = dict.fromkeys([143, 2, 3, 4, 55, 6, 7, 55, 8, 9, 10], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')



cidades = ['São Paulo', 'Belém', 'Boa Vista', 'Belo Horizonte', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Curitiba', 'Recife', 'Porto Alegre', 'Rio de Janeiro', 'Belo Horizonte', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Curitiba', 'Recife', 'Porto Alegre', 'Rio de Janeiro']
# quantas cidades únicas existem nesse cadastro?
print(f'Quantidade de cidades únicas: {len(set(cidades))}')
print(f'total de citações de cidades: {len(cidades)}')
cidades_unicas = set(cidades)
print(f'cidades únicas: {sorted(cidades_unicas)}')
cidades_unicas.add('São José dos Campos') # adiciona um elemento ao conjunto
print(f'cidades únicas: {sorted(cidades_unicas)}')
cidades_unicas.remove('São José dos Campos') # remove um elemento do conjunto. Nenhum valor é retornado.
print(f'cidades únicas: {sorted(cidades_unicas)}')
# cidades_unicas.remove('Ananindeua') # remove um elemento que não existe, retorna keyerror
cidades_unicas.discard('Ananindeua') # remove um elemento que não existe, não retorna erro
print(f'cidades únicas: {sorted(cidades_unicas)}')


# copiando um conjunto para outro:
# FORMA 1 - DEEP COPY
cidades_set = set(cidades)
novo = cidades_set.copy()
novo.add('São José dos Campos')
print(f'cidades: {novo}')
print(f'cidades_set: {cidades_set}')

# FORMA 2 - SHALLOW COPY

NOVO2 = cidades_set
NOVO2.add('Blumenau')
print(f'cidades: {NOVO2}')
print(f'cidades_set: {cidades_set}')

# removendo elementos do conjunto
# todos os elementos do conjunto são removidos
NOVO2.clear()
print(f'cidades: {NOVO2}')
print(f'cidades_set: {cidades_set}')


cidades = ['São Paulo', 'Belém', 'Boa Vista', 'Belo Horizonte', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Curitiba', 'Recife', 'Porto Alegre', 'Rio de Janeiro', 'Belo Horizonte', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Curitiba', 'Recife', 'Porto Alegre', 'Rio de Janeiro']


# métodos matemáticos do conjunto:

estudantes_python = {'João', 'Maria', 'Pedro', 'João', 'José', 'Maria', 'José', 'Pedro', 'João'}
estudantes_java = {'Fernando', 'Maria', 'Gabriel', 'Alan', 'João'}

# intersecção:
estudantes_python_e_java = estudantes_python & estudantes_java
print(f'intersecção fazem os 2: {estudantes_python_e_java}')

# união:
estudantes_python_com_java = estudantes_python | estudantes_java
print(f'união todos:{estudantes_python_com_java}')

# diferença:
estudantes_so_python = estudantes_python - estudantes_java
print(f'diferença python - java:{estudantes_so_python}')

# diferença simétrica:
estudantes_so_java = estudantes_java - estudantes_python
print(f'diferença java - python:{estudantes_so_java}')

# complemento:
estudantes_maximos_python = estudantes_python ^ estudantes_java
print(f'complemento de java em python:{estudantes_maximos_python}')
estudantes_maximos_java = estudantes_java ^ estudantes_python
print(f'complemento de python em java:{estudantes_maximos_java}')
print(estudantes_maximos_python == estudantes_maximos_java)
# conjunto vazio:
estudantes_vazio = set()
print(estudantes_vazio)

