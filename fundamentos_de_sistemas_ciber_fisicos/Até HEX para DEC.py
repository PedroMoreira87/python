num = input('Digite o valor de entrada: ')
base = int(input('Digite a base deste número: '))

hexa_legal = '0123456789ABCDEF'

if len(num) == 2:
    dig1 = hexa_legal.find(num[0])
    dig2 = hexa_legal.find(num[1])
    resultado = dig1 * (base ** 1) + dig2 * (base ** 0)
    print(f'{resultado}')
elif len(num) == 3:
    dig1 = hexa_legal.find(num[0])
    dig2 = hexa_legal.find(num[1])
    dig3 = hexa_legal.find(num[2])
    resultado = dig1 * (base ** 2) + dig2 * (base ** 1) + dig3 * (base ** 0)
    print(f'{resultado}')
elif len(num) == 4:
    dig1 = hexa_legal.find(num[0])
    dig2 = hexa_legal.find(num[1])
    dig3 = hexa_legal.find(num[2])
    dig4 = hexa_legal.find(num[3])
    resultado = dig1 * (base ** 3) + dig2 * (base ** 2) + dig3 * (base ** 1) + dig4 * (base ** 0)
    print(f'{resultado}')
elif len(num) == 5:
    dig1 = hexa_legal.find(num[0])
    dig2 = hexa_legal.find(num[1])
    dig3 = hexa_legal.find(num[2])
    dig4 = hexa_legal.find(num[3])
    dig5 = hexa_legal.find(num[4])
    resultado = dig1 * (base ** 4) + dig2 * (base ** 3) + dig3 * (base ** 2) + dig4 * (base ** 1) + dig5 * (base ** 0)
    print(f'{resultado}')
elif len(num) == 6:
    dig1 = hexa_legal.find(num[0])
    dig2 = hexa_legal.find(num[1])
    dig3 = hexa_legal.find(num[2])
    dig4 = hexa_legal.find(num[3])
    dig5 = hexa_legal.find(num[4])
    dig6 = hexa_legal.find(num[5])
    resultado = dig1 * (base ** 5) + dig2 * (base ** 4) + dig3 * (base ** 3) + dig4 * (base ** 2) + dig5 * (base ** 1) + dig6 * (base ** 0)
    print(f'{resultado}')
