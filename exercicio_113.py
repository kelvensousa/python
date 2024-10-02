
def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

valores = (2,3,4)
total = multiplicar(*valores)
print(f"O resutado da multiplicação é: {total}")

def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = 0
resultado = verificar_paridade(numero)
print(f'O número {numero} é {resultado}.')




