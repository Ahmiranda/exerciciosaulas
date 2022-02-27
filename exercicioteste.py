lista = []
nota = 0
while nota != 'sair':
    nota = float(input('digite a nota{} do aluno ou digite "sair" para sair: '.format((len(lista)+1))))
    lista.append(nota)
    if len(lista) > 3:
        break

nota = 0
for elemento in lista:
    nota = nota + elemento

print('A média das notas é {}'.format(nota/4))

