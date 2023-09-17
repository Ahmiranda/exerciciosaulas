# o que são expressões lambda e suas aplicações

# Expressões lambda são funções anônimas, ou seja, funções sem nome e que podem ser usadas em qualquer lugar
# onde uma função normal poderia ser usada, como por exemplo, em uma variável.

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# lambda (variável): (expressão)
lambda x: 3 * x + 1

# A expressão lambda acima é equivalente a função acima, porém, não possui nome, e pode ser usada em qualquer lugar
# onde uma função normal poderia ser usada, como por exemplo, em uma variável.
# Para usar a expressão lambda, basta atribuir a uma variável, como no exemplo abaixo:

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Expressões lambda podem ter mais de um parâmetro, como no exemplo abaixo:
# .strip() remove os espaços em branco no início e no final da string
# .title() deixa a primeira letra de cada palavra em maiúsculo e as demais em minúsculo
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('  marcos', '  silva'))

var1 = lambda x, y: x + y
var2 = lambda: 'Olá mundo!'
var3 = lambda s: s.upper()
var4 = lambda x, y, z: x + y + z

print(var1(2, 3))
print(var2())
print(var3('marcos'))
print(var4(2, 3, 4))

# obs: expressões lambda podem ser usadas como argumentos de outras funções, como no exemplo abaixo:

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)


def geradora_funcao_quad(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quad(2, 3, -5)  # retorna função lambda para coefs: a = 2, b = 3, c = -5
print(teste(2))

print(geradora_funcao_quad(3, 0, 1)(2))  # retorna função lambda para coefs: a = 3, b = 0, c = 1

# aplicações de expressões lambda
# 1. # ordenação de listas
# 2. # ordenação de dicionários
# comprehensions (list, dict, set)

