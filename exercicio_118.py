def duplicar(numero): # Função que duplica o número
    return numero * 2

def triplicar(numero): # Função que triplica o número
    return numero * 3

def quadruplicar(numero): # Função que quadruplica o número
    return numero * 4

def operar_complexo(numero, operacao):
    if operacao == 'duplicar':
        return duplicar(numero)
    elif operacao == 'triplicar':
        return triplicar(numero)
    elif operacao == 'quadruplicar':
        return quadruplicar(numero)
    else:
        return "Operação desconhecida"

numero_complexo = 3 + 4
print(f"Duplicar: {operar_complexo(numero_complexo, 'duplicar')}")
print(f"Triplicar: {operar_complexo(numero_complexo, 'triplicar')}")
print(f"Quadruplicar: {operar_complexo(numero_complexo, 'quadruplicar')}")


'''print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))'''

# Função que duplica o número
def duplicar(numero):
    return numero * 2

# Função que triplica o número
def triplicar(numero):
    return numero * 3

# Função que quadruplica o número
def quadruplicar(numero):
    return numero * 4

# Função principal que recebe a entrada do usuário e aplica a operação escolhida
def main():
    numero = float(input("Digite um número: "))
    operacao = input("Escolha a operação (duplicar, triplicar, quadruplicar): ").strip().lower()

    if operacao == 'duplicar':
        resultado = duplicar(numero)
    elif operacao == 'triplicar':
        resultado = triplicar(numero)
    elif operacao == 'quadruplicar':
        resultado = quadruplicar(numero)
    else:
        print("Operação desconhecida.")
        return

    print(f"O resultado da operação {operacao} é: {resultado:.1f}")

# Executa a função principal
if __name__ == "__main__":
    main()

