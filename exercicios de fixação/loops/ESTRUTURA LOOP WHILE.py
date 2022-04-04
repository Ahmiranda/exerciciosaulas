"""
LOOP WHILE
ITERAÇÕES SOBRE SEQUÊNCIAS

WHILE EXPRESSÃO_BOOLEANA:
    //EXECUÇÃO DO LOOP

o bloco while vai ser repetida enquanto a expressão booleana for verdadeira

"""
#EXEMPLO 1
num = 1
while num < 10:
    print(num, end = ' ')
    num = num + 1

#OBS: em um loop while é importante para que cuidemos do critério de parada, senão, ele vai ser eternamente repetido.

#EXEMPLO 2: condicionais para strings

resposta = ' '
while resposta != 'sim':
    resposta = str(input('já acabou Jéssica? '))