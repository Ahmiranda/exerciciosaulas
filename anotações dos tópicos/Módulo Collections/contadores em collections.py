'''

Módulo Collections - Contadores

Counter - recebe um iterável como parâmetro e cria um objeto do tipo collections counter, parecido com um
dicionário contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
deste elemento.


'''

from collections import Counter
import pandas as pd

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 2, 2, 4, 5, 5]

rest = Counter(lista)
data = pd.DataFrame(rest.items(), columns=['Número', 'Quantidade'])
print(data)
print(rest)
print(type(rest))

string = 'Geek University'
rest = Counter(string)
rest = sorted(rest.items())
print(rest)
data2 = pd.DataFrame(rest, columns=['Letra', 'Quantidade'])
print(data2)

texto ="""
    Ciro Gomes deu a declaração ao fazer um discurso na Universidade de Brasília (UnB), onde participou de encontro organizado pela Sociedade Brasileira para o Progresso da Ciência (SBPC).

Ex-governador do Ceará, Ciro Gomes disputa a Presidência pela quarta vez (também concorreu em 1998, 2002 e 2018) e nunca chegou ao segundo turno.

"Nós temos que colocar em perspectiva que o Brasil precisa discutir finalmente, de forma inadiável, o modelo econômico. Esta é a razão pela qual eu, pela quarta vez, tento ser presidente do Brasil. Claro que, desta vez, chega. Porque, se eu não ganho agora, vou botar a viola no saco porque eu virei o bico falante, o chato, o destemperado", declarou Ciro Gomes."""

palavras = texto.split()
rest = Counter(palavras)
print(rest.most_common(5))
'''rest = sorted(rest.items())
data3 = pd.DataFrame(rest, columns=['Palavra', 'Quantidade'])
print(data3.most_common(5))'''
