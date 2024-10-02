pergunta = {
    'Perguntas': 'Quantos anos tem Maria D.Arc?',
    'Opçõees': ['12', '25', '33', '48'],
    'Resposta': '25',
}


for perguntas in pergunta:
    print('Pergunta:', pergunta['Perguntas'])
    print()
    
    for i, opcao in enumerate(perguntas['Opções']):
        print(f'{i}', opcao)
    print()

    escolha = print('Escolha uma opção: ')
    escolha_int = None
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        ...

    print()

    break