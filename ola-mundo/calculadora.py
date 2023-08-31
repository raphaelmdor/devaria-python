def somar(numero1, numero2):
    print(f'realizando soma de {n1} + {n2}')
    resultado = numero1 + numero2
    return resultado
def subtrair(numero1, numero2):
    print(f'realizando subtração de {n1} - {n2}')
    resultado = numero1 - numero2
    return resultado

def dividir(numero1, numero2):
    print(f'realizando divisão de {n1} / {n2}')
    resultado = numero1 / numero2
    return resultado

def multiplicar(numero1, numero2):
    print(f'realizando multiplicação de {n1} * {n2}')
    resultado = numero1 * numero2
    return resultado

if __name__ == '__main__':
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    op = input('Qual operação você quer fazer? (+, -, /, *):')
    resultado = 0

    if op == '+':
        resultado = somar(n1, n2)
    elif op == '-':
        resultado = subtrair(n1, n2)
    elif op == '/':
        resultado = dividir(n1, n2)
    elif op == '*':
        resultado = multiplicar(n1, n2)
    else:
        print('Operador incorreto.')
    print(f'O rsultado da operação é {resultado}')
