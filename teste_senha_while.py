conta = input('Digite o usúario: ')
senha = input('Digite senha: ')
password = senha.isnumeric()
usuario = 'kelvensousa'
password = 12345
while True:
    if conta == usuario or senha == password:
        print('Senha correta!')
        break
    else:
        print('A conta ou senha estão incorretos!')
        print('Digite novamente')
        conta = input('Digite o usúario: ')
        senha = input('Digite senha: ')
print('Acabou')