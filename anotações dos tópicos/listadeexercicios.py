"""
questão 1) 
Faça um Programa que mostre a mensagem "Alo mundo" na tela.
resposta:

print('olá mundo')

questão 2)
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

n1 = input('Digite um número')
print('o número informado foi: {}'.format(n1))

questão 3)
Faça um Programa que peça dois números e imprima a soma.

n1 = float(input('Dgite um valor para ser somado: '))
n2 = float(input('Digite um segundo número: '))
print('o valor da soma de {} e {} é: {}'.format(n1,n2,n1+n2))

questão 4)
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

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

Questão 5)
Faça um Programa que converta metros para centímetros.

n1 = float(input('Digite o valor de medida a ser convertido em metros: \n'))
n1 = n1*100
print('O valor inserido é de {} cm'.format(n1))

questão 6)
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi as pi
r = float(input('Digite o raio do circulo em metros: \n'))
A = pi*pow(r,2)
print('A área do círculo com raio {0} m é: {1:.3f} m²'.format(r,A))

questão 7)
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

a = float(input('Digite o tamanho da aresta do quadrado em metros: \n'))
A = pow(a,2)
print('O dobro da área do quadrado de aresta {} m é {:.2f} m².'.format(a,2*A))

questão 8)
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Qual o valor pago por hora trabalhada? \n'))
horas_mensais = int(input('Quantas horas são trabalhadas no mês?\n'))
salario = valor_hora*horas_mensais
print('Trabalhando {} horas no mês com R$: {:.2f} de pagamento por hora gera um salário de R$: {:.2f}'.format(horas_mensais,valor_hora,salario))
print('\nSão {:.2f} horas trabalhadas na semana, {:.2f} horas trabalhadas por dia.'.format(horas_mensais/4,horas_mensais/22))

questão 9)
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


