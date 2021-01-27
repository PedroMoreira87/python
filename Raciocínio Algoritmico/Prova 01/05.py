# Entrada de dados
from math import acos, degrees
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
# Verificar se os lados A, B e C formam um triângulo
if a < b + c and b < a + c and c < a + b:
    if a != b and a != c and b != c:
        print('Triângulo Escaleno')
    elif a == b and a == c and b == c:
        print('Triângulo Equilátero')
    else:
        print('Triângulo Isósceles')

else:
    print('Não formam um triângulo')
