# n = int(input('Qual o valor de n? '))
# f = 1
# print(f'Calculando {n}! = ', end='')
# while n > 0:
#     print(n, end='')
#     print(' X ' if n > 1 else ' = ', end='')
#     f *= n
#     n -= 1
# print(f)


n = int(input('Qual o valor de n? '))
f = 1
print(f'Calculando {n}! = ', end='')
for n in range(n, 0, -1):
    print(n, end='')
    print(' X ' if n > 1 else ' = ', end='')
    f *= n
print(f)
