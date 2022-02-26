"""
UTILIZAÇÃO DE 'BREAK's
é um recurso para quebrar ‘loops’ com o comando 'break'
é igual ao C, java e ao matlab

"""

#EXEMPLO 1

for num in range(1,11):
    if num == 6:
        break
    else:
        print(num, end = ' ')
print('Saiu do loop')

#EXEMPLO 2
while True:
    comando = str(input('digite um comando pra sair: '))
    if comando  == 'sair':
        break
