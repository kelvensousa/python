dictnary = {
    'name': 'Kelven',
    'idade': 22
    
    }
x = dictnary.get('name')
y = dictnary.get('idade')
for x in dictnary:
    x = input('Digite um nome: ')
    if x == 'Kelven':
        print(f'O nome {x} está orreto!')
        continue
    else:
        print(f'O nome {x} está falso')

    for y in dictnary:
        y = input('Digite um idade: ')
        if y == '22':
         print(f'O idade {y} está correto!')
         break
        else:
         print(f'O idade {y} está falso')
print(x, y)