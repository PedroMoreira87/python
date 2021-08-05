dividendo = int(input('Digite o valor decimal: '))
divisor = int(input('Digite o valor divisor: '))

hexa_legal = '0123456789ABCDEF'

resposta = ''

while True:
    quociente = dividendo // divisor
    resto = dividendo % divisor
    resposta = hexa_legal[resto] + resposta
    if quociente == 0:
        break
    dividendo = quociente

print(resposta)
