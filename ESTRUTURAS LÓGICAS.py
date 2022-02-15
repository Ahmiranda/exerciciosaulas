"""
ESTRUTURAS LÓGICAS AND(E), OR(OU), NOT (NÃO), IS(É)

OPERADORES UNÁRIOS
NOT
IS

OPERADORES BINÁRIOS
OR
AND

para o END ambos os valores precisam ser TRUE
para o OR, apenas um dos valores precisam ser TRUE
para o NOT, o valor booleano é invertido / NEGADO
para o IS, o valor é comparado com um segundo
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar a sua conta. Por favor, ative o seu e-mail.')

'ou também...'

if not ativo:
    print('Você precisa ativar a sua conta. Por favor, ative o seu e-mail.')
else:
    print('Bem-vindo, Usuário!')

print(not ativo)

'ou também...'

if ativo is True:
    print('Bem-vindo, Usuário!')
else:
    print('Você precisa ativar a sua conta. Por favor, ative o seu e-mail.')


