import operator

def calcularadora():
    operacoes = {
        '1': ('Adição', operator.add),
        '2': ('Subtração', operator.sub),
        '3': ('Multiplicação', operator.mul),
        '4': ('Divisão', operator.truediv)
    }
    print('Selecione a operação: ')
    for chave, (nome, _) in operacoes.items():
        print(f'{chave}. {nome}')
    escolha = input('Digite sua escolha (1/2/3/4): ')

    if escolha in operacoes:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        nome, operacao = operacoes[escolha]

        try:
            resultado = operacao(num1, num2)
            print(f'{num2} {nome} {num2} = {resultado}')
        except ZeroDivisionError:
            print('Erro: Divisão por zero não é permitida.')
    else:
        print('Escolha inválida!')

calcularadora()