import re

def verificar_senha(senha):
    # Critérios de validação da senha
    comprimento_minimo = 8
    min_maiusculas = 1
    min_minusculas = 1
    min_numeros = 1
    min_caracteres_especiais = 1

    # Contadores de verificação
    count_maiusculas = 0
    count_minusculas = 0
    count_numeros = 0
    count_caracteres_especiais = 0

    # Loop para verificar cada caractere da senha
    for char in senha:
        if char.isupper():  # Indica se o caractere Unicode especificado é categorizado como uma letra maiúscula.
            count_maiusculas += 1 
        elif char.islower():  # Determina se o caractere mais à esquerda de uma string é uma letra minúscula.
            count_minusculas += 1
        elif char.isdigit():  # É uma função embutida na linguagem de programação Python que verifica se uma determinada cadeia de caracteres (string) contém apenas dígitos numéricos.
            count_numeros += 1
        elif re.match(r'[!@#$%^&*(),.?":{}|<>]', char):  # É uma estrutura de controle de fluxo que permite comparar uma variável com diferentes valores ou padrões de forma mais organizada e legível do que as tradicionais estruturas if/elif/else.
            count_caracteres_especiais += 1

    # Verificação dos critérios
    if (len(senha) >= comprimento_minimo and  # A função len , quando aplicada a um string, retorna o número de caracteres no string (ou seja, o seu comprimento).
        count_maiusculas >= min_maiusculas and
        count_minusculas >= min_minusculas and
        count_numeros >= min_numeros and
        count_caracteres_especiais >= min_caracteres_especiais):
        return True
    else:
        return False

# Entrada de senha pelo usuário
senha_usuario = input("Digite sua senha: ")

# Verifica se a senha é forte
if verificar_senha(senha_usuario):
    print("Senha forte!")
else:
    print("Senha fraca. Por favor, siga as diretrizes de segurança.")

'''Poderia no final utilizar um comando de repetição para quando a senha não seguir o padrão de critérios, entraria no laço até que seja comprida o comando satisfatório da função.'''
