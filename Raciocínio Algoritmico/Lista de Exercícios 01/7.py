# Entrada de dados
from math import pi
n1 = float(input('Digite o raio da esfera'))
# Processamento
n2 = (4/3) * pi * (n1 ** 3)
n3 = 4 * pi * (n1 ** 2)
# Saída de dados
print(f'O volume é: {n2:.2f} \nA área da superfície é: {n3:.2f}')
