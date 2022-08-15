'''
Módulo Collections - Default dict

    DefaultDict - Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda para isso. Este valor default é utilizado quando não houver um valor para uma chave específica.
    se uma chave não existir, o valor default é retornado e a chave é criada.


OBS: funções lambda são funções anônimas, ou seja, não possuem nome, que podem ou não receber parâmetros de entrada e retornar valores.

'''

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
