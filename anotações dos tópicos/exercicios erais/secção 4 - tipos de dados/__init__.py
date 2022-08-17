def quest1():
    inteiro = int(input('Digite um número inteiro: \n'))
    return inteiro


def quest2():
    real = float(input('Digite um número real: \n'))
    return real


def quest3():
    lista = []
    for i in range(3):
        entrada = int(input('Digite um número inteiro: \n'))
        print('O número inserido foi: {}'.format(entrada))
        lista.append(entrada)
    valor = sum(lista)
    print('A soma dos números é: {}'.format(valor), end='\n')
    return 0


def quest4():
    entrada = float(input('Digite um número real: \n'))
    return entrada ** 2


def quest5():
    entrada = float(input('Digite um número real: \n'))
    entrada = entrada * 1 / 5
    texto = ('A quinta parte do número {}, é: {} \n'.format(entrada * 5, entrada))
    return texto


def quest6():
    celsius = float(input('Digite a temperatura em graus Celsius: \n'))
    fahrenheit = celsius * 1.8 + 32
    texto = ('A temperatura em graus Fahrenheit é: {:.3f}ºF \n'.format(fahrenheit))
    return texto


def quest7():
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: \n'))
    celsius = (fahrenheit - 32) * 5 / 9
    texto = ('A temperatura em graus Celsius é: {:.3f}ºC \n'.format(celsius))
    return texto


def quest8():
    kelvin = float(input('Digite a temperatura em Kelvin: \n'))
    celsius = kelvin - 273.15
    texto = ('A temperatura em graus Celsius é: {:.3f}ºC \n'.format(celsius))
    return texto


def quest9():
    celsius = float(input('Digite a temperatura em graus Celsius: \n'))
    kelvin = celsius + 273.15
    texto = ('A temperatura em Kelvin é: {:.3f}K \n'.format(kelvin))
    return texto


def quest10():
    velocidade = float(input('Digite a velocidade em km/h: \n'))
    velocidade = velocidade * 10 / 36
    texto = ('A velocidade no SI é: {:.3f} m/s \n'.format(velocidade))
    return texto


def quest11():
    velocidade = float(input('Digite a velocidade em m/s: \n'))
    velocidade = velocidade * 36 / 10
    texto = ('A velocidade em km/h é: {:.3f} km/h \n'.format(velocidade))
    return texto


def quest12():
    distancia = float(input('Digite a distância em milhas: \n'))
    distancia = distancia * 1.609
    texto = ('A distância em km é: {:.3f} km \n'.format(distancia))
    return texto


def quest13():
    distancia = float(input('Digite a distância em km: \n'))
    distancia = distancia * 1 / 1.609
    texto = ('A distância em milhas é: {:.3f} milhas \n'.format(distancia))
    return texto


def quest14a():
    graus = float(input('Digite o ângulo em graus: \n'))
    radianos = graus * 3.14 / 180
    texto = ('O valor em radianos é: {:.3f} \n'.format(radianos))
    return texto


def quest14b():
    from math import radians
    graus = float(input('Digite o ângulo em graus: \n'))
    radianos = radians(graus)
    texto = ('O valor em radianos é: {:.3f} \n'.format(radianos))
    return texto


def quest15a():
    radianos = float(input('Digite o ângulo em radianos: \n'))
    graus = radianos * 180 / 3.14
    texto = ('O valor em graus é: {:.3f} \n'.format(graus))
    return texto


def quest15b():
    from math import degrees
    radianos = float(input('Digite o ângulo em radianos: \n'))
    graus = degrees(radianos)
    texto = ('O valor em graus é: {:.3f} \n'.format(graus))
    return texto


def quest16():
    polegada = float(input('Digite a polegada: \n'))
    centimetro = polegada * 2.54
    texto = ('A polegada em centímetros é: {:.3f} cm \n'.format(centimetro))
    return texto


def quest17():
    centimentros = float(input('Digite a distância em centímetros: \n'))
    polegada = centimentros / 2.54
    texto = ('A distância em polegadas é: {:.3f} pol \n'.format(polegada))
    return texto


def quest18():
    volumem3 = float(input('Digite o volume em m³: \n'))
    litros = volumem3 * 1000
    texto = ('O volume em litros é: {:.3f} L \n'.format(litros))
    return texto


def quest19():
    volumeL = float(input('Digite o volume em L: \n'))
    volumem3 = volumeL / 1000
    texto = ('O volume em m³ é: {:.3f} m³ \n'.format(volumem3))
    return texto


def quest20():
    massa = float(input('Digite a massa em kg: \n'))
    libra = massa * 2.205
    texto = ('A massa em libra é: {:.3f} lb \n'.format(libra))
    return texto


def quest21():
    libra = float(input('Digite a massa em libras: \n'))
    massa = libra * 0.4536
    texto = ('A massa em kg é: {:.3f} kg \n'.format(massa))
    return texto


def quest22():
    distancia_jardas = float(input('Digite a distância em jardas: \n'))
    metros = distancia_jardas * 0.91
    texto = ('A distância em metros é: {:.3f} m \n'.format(metros))
    return texto


def quest23():
    distancia_metros = float(input('Digite a distância em metros: \n'))
    distancia_jardas = distancia_metros / 0.91
    texto = ('A distância em jardas é: {:.3f} jardas \n'.format(distancia_jardas))
    return texto


def quest24():
    area_m2 = float(input('Digite a área em m²: \n'))
    area_acres = area_m2 * 0.000247105
    texto = ('A área em acres é: {:.3f} acres \n'.format(area_acres))
    return texto


def quest25():
    area_acres = float(input('Digite a área em acres: \n'))
    area_m2 = area_acres * 4046.86
    texto = ('A área em m² é: {:.3f} m² \n'.format(area_m2))
    return texto


#######################################################################################################


def sec5_quest1():
    a = int(input('Digite um número inteiro: \n'))
    b = int(input('Digite um número inteiro: \n'))

    if a > b:
        print('O número {} é maior que {}'.format(a, b))
    elif a < b:
        print('O número {} é menor que {}'.format(a, b))
    else:
        print('Os números são iguais')
    return 'Finalizado'


def sec5_quest2():
    a = float(input('Digite um valor: \n'))
    if a > 0:
        print('a raiz quadrada de {} é {}'.format(a, a ** (1 / 2)))
    else:
        print('Valor inválido, tente novamente')
    return 'Finalizado'


def sec5_quest3():
    a = float(input('Digite um valor: \n'))
    if a > 0:
        print('A raiz quadrada de {} é {}'.format(a, a ** (1 / 2)))
    else:
        print('O valor quadrático de {} é {}'.format(a, a ** 2))
    return 'Finalizado'


def sec5_quest4():
    a = float(input('Digite um valor: \n'))
    if a > 0:
        print('A raiz quadrada de {} é {}'.format(a, a ** (1 / 2)), end='')
        print(' e o valor quadrático de {} é {}'.format(a, a ** 2))
    else:
        print('valor inválido, tente novamente')
    return 'Finalizado'


def sec5_quest5():
    a = float(input('Digite um valor: \n'))
    if a % 2 == 0:
        print('O número {} é par'.format(a))
    else:
        print('O número {} é ímpar'.format(a))
    return 'Finalizado'


def sec5_quest6():
    a = int(input('Digite um valor: \n'))
    b = int(input('Digite um valor: \n'))
    if a > b:
        print('O maior número é {}'.format(a), end=' ')
        print('e a diferença entre os números é {}'.format(abs(a - b)))
    elif a < b:
        print('O maior número é {}'.format(b), end=' ')
        print('e a diferença entre os números é {}'.format(abs(a - b)))
    else:
        print('Os números são iguais')
    return 'Finalizado'


def sec5_quest7():
    from random import randint
    from collections import namedtuple
    a = [randint(0, 10) for _ in range(4)]
    notas = namedtuple('Semestre', ['nota1', 'nota2', 'nota3', 'nota4'])
    notas = notas(a[0], a[1], a[2], a[3])
    print(notas)
    if sum(a) / len(a) >= 7:
        print('O Aluno possui média {} e foi aprovado'.format(sum(a) / len(a)))
    elif 7 > sum(a) / len(a) >= 5:
        print('O Aluno possui média {} e foi de recuperação'.format(sum(a) / len(a)))
    else:
        print('O Aluno possui média {} e foi reprovado'.format(sum(a) / len(a)))
    return 'Finalizado'


def sec5_quest9():
    salario = float(input('Digite o salário: \n'))
    emprestimo = float(input('Digite o valor do empréstimo: \n'))
    if emprestimo <= salario * 0.25:
        print('O empréstimo pode ser concedido')
    else:
        print('O empréstimo não pode ser concedido')
    return 'Finalizado'


def sec5_quest10():
    altura = float(input('Digite a altura da pessoa: \n'))
    peso = float(input('Digite o peso da pessoa: \n'))
    sexo = input('Digite H p/ homem ou M para mulher: \n')
    if sexo == 'H' or sexo == 'h':
        peso_ideal = (72.7 * altura) - 58
        print('O peso ideal deste homem é: {} kg, com {} kg, a diferença atual é {} kg'.format(peso_ideal, peso,
                                                                                               abs(peso_ideal - peso)))
    elif sexo == 'M' or sexo == 'm':
        peso_ideal = (62.1 * altura) - 44.7
        print('O peso ideal desta mulher é: {} kg, com {} kg, a diferença atual é {} kg'.format(peso_ideal, peso,
                                                                                                abs(peso_ideal - peso)))
    else:
        print('Entrada inválida, tente novamente')

    return 'Finalizado'


def sec5_quest18():
    def switch():
        opcao = int(input('Digite 1 para adição, 2 para subtração, 3 para multiplicação ou 4 para divisão: \n'))
        if opcao == 1:
            return 'adição', '+'
        elif opcao == 2:
            return 'subtração', '-'
        elif opcao == 3:
            return 'multiplicação', '*'
        elif opcao == 4:
            return 'divisão', '/'
        else:
            return 'Opção inválida, tente novamente'

    a = float(input('Digite o primeiro número: \n'))
    b = float(input('Digite o segundo número: \n'))
    opcao, operacao = switch()
    print('{} {} {} = {}'.format(a, opcao, b, eval('a {} b'.format(operacao))))
    return 'Finalizado'


def sec5_quest11():
    numero = input('Digite um número: \n')
    if int(numero) > 0:
        print('A soma dos números de {}, é {}'.format(int(numero), sum(int(i) for i in list(numero))))
    else:
        print('Entrada inválida, tente novamente')
    return 'Finalizado'


def sec5_quest12():
    from math import log10
    numero = float(input('Digite um número: \n'))
    if numero > 0:
        print('O logaritmo de base decimal de {} é {}'.format(numero, log10(numero)))


def sec5_quest13():
    from numpy import array, dot

    notas = [float(input('Digite a nota {}: \n'.format(i + 1))) for i in range(3)]
    pesos = array([2, 3, 5])
    print('A média ponderada das notas é {}'.format((dot(notas, pesos) / sum(pesos))))
    return 'Finalizado'


def sec5_quest14():
    day = int(input('Dias da semana, digite o número correspondente ao dia da semana: \n'))

    def switch(dia):
        if dia == 1:
            return 'Domingo'
        elif dia == 2:
            return 'Segunda-feira'
        elif dia == 3:
            return 'Terça-feira'
        elif dia == 4:
            return 'Quarta-feira'
        elif dia == 5:
            return 'Quinta-feira'
        elif dia == 6:
            return 'Sexta-feira'
        elif dia == 7:
            return 'Sábado'
        else:
            return 'Entrada inválida, tente novamente'

    print('O dia da semana é {}'.format(switch(day)))
    return 'Finalizado'


def sec5_quest16():
    mes = int(input('Digite o número correspondente ao mês: \n'))
    switch = {1: "Janeiro", 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    print('O mês é {}'.format(switch.get(mes, 'Entrada inválida, tente novamente')))
    return 'Finalizado'


def sec5_quest17():
    base_menor = float(input('Digite a base menor: \n'))
    base_maior = float(input('Digite a base maior: \n'))
    if base_maior < 0 or base_menor < 0:
        print('Valores inválidos, tente novamente')
    else:
        altura = float(input('Digite a altura: \n'))
        area = (base_menor + base_maior) * altura / 2
        print('A área do trapézio é: ', area)
    return 'Finalizado'


def sec5_quest19():
    num = float(input('Digite um número: \n'))
    if num % 3 == 0 and num % 5 == 0:
        print('O número {} é múltiplo de 3 e 5.'.format(num))
    elif num % 3 == 0 and num % 5 != 0:
        print('O número {} é múltiplo de 3 mas não de 5.'.format(num))
    elif num % 3 != 0 and num % 5 == 0:
        print('O número {} é múltiplo de 5 mas não é de 3.'.format(num))
    else:
        print('O número {} não é múltiplo de 3 e nem de 5.'.format(num))
    return 'Finalizado'


def sec5_quest20():
    lados = [float(input('Digite o {}º de 3 lados para um triângulo \n'.format(i + 1))) for i in range(3)]
    lados.sort()
    a, b, c = lados

    def switch():
        if a == b == c:
            print('O triângulo é equilátero e possui lados: {}.'.format(a))
        elif a == b or a == c or b == c:
            print('O triângulo é isósceles e possui lados: {}, {} e {}. '.format(a, b, c))
        elif a != b and a != c and b != c:
            print('O triângulo é escaleno e possui lados: {}, {} e {}.'.format(a, b, c))
        else:
            print('Algo deu errado, tente novamente.')

    if abs(c - b) < a < abs(c + b):
        switch()
    else:
        print('Não existe triângulo com tais proporções, tente novamente.')
    return 'Finalizado'


def sec5_quest21():
    def switch(i):
        valores = [float(input('Digite os números: ')) for _ in range(2)]
        valores.sort()
        if i == 1:
            print('A soma de {} e {} é {}'.format(valores[0], valores[1], sum(valores)))
        elif i == 2:
            print('A diferença de {} e {} é {}.'.format(valores[1], valores[0], valores[1] - valores[0]))
        elif i == 3:
            print('O produto entre {} e {} é {}.'.format(valores[0], valores[1], valores[0] * valores[1]))
        elif i == 4:
            if valores[1] == 0 == valores[0]:
                print('Não é possível realizar divisão entre zeros, tente novamente')
            elif valores[1] == 0:
                print('O quociente entre {} [e {} é 0'.format(valores[1], valores[0]))
            elif valores[0] == 0:
                print('O quociente entre {} é {} é 0'.format(valores[0], valores[1]))
            else:
                print('O quociente entre {} e {} é {}.'.format(valores[1], valores[0], valores[0] / valores[1]))
        else:
            print('Operação não disponível, tente novamente.')

    print('Escolha uma opção: \n')
    print('1: Soma e 2 números \n2: Diferença entre 2 números (maior pelo menor)\n', end='')
    print('3: Produto entre dois números\n4: Divisão entre 2 números (denominador não nulo)')
    index = float(input('Digite sua escolha: \n'))
    if index % 1 == 0 and 1 <= index <= 4:
        switch(index)
    else:
        print('Digite uma entrada válida, tente novamente!!!!')
    return 'Finalizado'


def sec5_quest22():
    ano = int(input('Digite um ano qualquer para saber se ele é bissexto: \n'))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} não é bissexto.'.format(ano))
    return 'Finalizado'


def sec5_quest24():
    index_estados = {
        'MG': 0.07,
        'SP': 0.12,
        'RJ': 0.15,
        'MS': 0.08
    }
    infos_estados = [input('Digite a sigla do estado e o valor do produto na região: \n') for _ in range(2)]
    infos_estados.sort()
    taxas = index_estados.get(infos_estados[1].upper(), 'Entrada inválida, tente novamente')

    if type(taxas) == float:
        valor_final = (1 + taxas) * float(infos_estados[0])
        print('O valor final do produto em {0}, é R$: {1:.3f} '.format(infos_estados[1].upper(), valor_final))

    else:
        print(taxas)

    return 'Finalizado'


def sec5_quest25():
    from sympy import symbols, init_printing
    from numpy import array, dot, linspace
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    init_printing(use_latex='mathjax', latex_mode='equation*')
    x, y, delta = symbols('x y Δ')
    coeficientes = [float(input('Digite o {0}º coeficiente: \n'.format(i + 1))) for i in range(3)]
    dim_x = array([x ** 2, x, 1])
    y = dot(dim_x, coeficientes)
    delta = coeficientes[1] ** 2 - 4 * coeficientes[0] * coeficientes[2]
    if delta < 0:
        print('Não existe raízes reais para o polinômio.')
    else:
        x1 = (-coeficientes[1] + delta ** 0.5) / (2 * coeficientes[0])
        x2 = (-coeficientes[1] - delta ** 0.5) / (2 * coeficientes[0])
        print('As raízes do polinômio são: {0:.3f} e {1:.3f}'.format(x1, x2))

        fig = plt.figure(figsize=(16, 9))
        plt.style.use('seaborn-talk')
        space = linspace(-10 + x1, 10 + x2, 100)
        f = coeficientes[0] * space ** 2 + coeficientes[1] * space + coeficientes[2]
        plt.axvline(-coeficientes[1] / (2 * coeficientes[0]), color='green', linestyle='dashed', linewidth=1)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.plot(space, f, color='blue')
        plt.scatter([x1, x2], [0, 0], color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Polinômio de grau 2')
        eq = mpatches.Patch(color='blue', label='y = {0}x² + {1}x + {2}'.format(coeficientes[0], coeficientes[1], coeficientes[2]))
        raiz = mpatches.Patch(color='red', label='Raízes: {0:.3f} e {1:.3f}'.format(x1, x2))
        simetria = mpatches.Patch(color='green', label='Simetria: x = {0:.3f}'.format(-coeficientes[1] / (2 * coeficientes[0])))
        plt.legend(handles=[eq, raiz, simetria], bbox_to_anchor=(1.02, 0.95), loc=2, borderaxespad=0.)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    return 'Finalizado'


def sec5_quest30():
    numeros = [float(input('Digite o {0}º de três números: \n'.format(i + 1))) for i in range(3)]
    numeros.sort()
    print('Os números em ordem crescente são: \n', end='')
    print(*numeros, sep=', ')
    print('Os números em ordem decrescente são: \n', end='')
    print(*reversed(numeros), sep=', ')

    return 'Finalizado'


if __name__ == '__main__':
    print(sec5_quest25(), end='')
