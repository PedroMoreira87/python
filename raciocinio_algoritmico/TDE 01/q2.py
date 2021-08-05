# Entrada de dados
from math import sqrt
a = float(input('Qual o tamanho do lado A?'))
b = float(input('Qual o tamanho do lado B?'))
c = float(input('Qual o tamanho do lado C?'))
# Processamento
p = (a + b + c) / 2
delta = p * (p - a) * (p - b) * (p - c)
# Saída de dados
if a < b + c and b < a + c and c < a + b:
    area = sqrt(delta)
    print(f'A área do triângulo é: {area:.2f}')
elif a <= 0 or b <= 0 or c <= 0:
    print("Lados nulos ou negativos não são aceitos.")
else:
    print("Triângulo inexistente.")
