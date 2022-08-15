'''
Módulo Collections - Deque
O deque se comporta como uma lista, porém com melhor performace
'''

from collections import deque

deq = deque('Geek University')
print(deq)

deq.append('a')

print(deq)

deq.appendleft('b')

print(deq)

# removendo elementos

print(deq.pop())  # remove o último elemento e retorna o valor removido
print(deq.popleft())  # remove o primeiro elemento e retorna o valor removido





