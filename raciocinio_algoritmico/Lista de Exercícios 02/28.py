# Entrada de dados
from math import acos, degrees
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
# Verificar se os lados A, B e C formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Continuar o código
    cos_alpha = (b ** 2 + c ** 2 - a ** 2) / (2.0 * b * c)
    cos_beta = (a ** 2 + c ** 2 - b ** 2) / (2.0 * a * c)
    cos_gamma = (a ** 2 + b ** 2 - c ** 2) / (2.0 * a * b)
    # Arco cosseno
    alpha = degrees(acos(cos_alpha))
    beta = degrees(acos(cos_beta))
    gamma = degrees(acos(cos_gamma))
    # Obtendo o maior dos ângulos
    ang = max(alpha, beta, gamma)
    if ang == 90:
        print('Triângulo Retângulo')
    elif ang > 90:
        print('Triângulo Obtusângulo')
    else:
        print('Triângulo Acutângulo')
else:
    print('Não formam um triângulo')
