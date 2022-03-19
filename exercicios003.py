import math as m

salario = float(input('A empresa atualizará os salários dos funcionários com base na seguinte tabela:\n Até R$: 280,'
                      '00 retorna 20% \n De R$: 280 até R$: 700,00 retorna 15%\n De R$: 700 a R$: 1500,00 retorna '
                      '10%\n E R$:1500,00 em diante retornam 5%\n Insira o valor que você recebe para saber o seu '
                      'novo salário e informações adicionais: '))
ate_280 = salario < 280
ate_700 = 280 <= salario < 700
ate_1500 = 700 <= salario < 1500
alem_de_1500 = salario >= 1500

tabela_de_correcoes = [1.20, 1.15, 1.10, 1.05]

def calculadora_salario(salario):
    global indice, correcao
        if ate_280:
            indice = tabela_de_correcoes[1]
            correcao = salario * indice

        elif ate_700:
            indice = tabela_de_correcoes[2]
              correcao = salario * indice

        elif ate_1500:
            indice = tabela_de_correcoes[3]
            correcao = salario * indice

        elif alem_de_1500:
            indice = tabela_de_correcoes[4]
            correcao = salario * indice

        else:
            print('Erro na entrada do dos valores, tente novamente.')


print(''.format(salario,indice, correcao, )
