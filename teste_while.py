condicao = float(input('Digite um numero de 0 a 10: '))

while condicao:
    if condicao < 10.99:
        print('Número aceito!')
        break
    else:
        print('Tente novamente!.')
        condicao = float(input('Digite um numero de 0 a 10: '))
print('Acabou')

