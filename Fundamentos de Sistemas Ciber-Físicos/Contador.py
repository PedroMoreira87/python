print('CONTADOR...')
print('Experimente bases como 32   ;)  é divertido...')
print()
base = int(input('Digite a base de contagem (de 2 a 36): '))
limite = int(input('Total de valores gerados: '))


# Aqui eu aproveitei o código da aula anterior...
def converte(valor, base1):
    dividendo = valor
    divisor = base
    hexa_legal = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resposta = ''
    while True:
        quociente = dividendo // divisor
        resto = dividendo % divisor
        resposta = hexa_legal[resto] + resposta
        if quociente == 0:
            break
        dividendo = quociente
    return resposta


for i in range(limite):
    print(f'{i} -> {converte(i, base)} [{base}]')
