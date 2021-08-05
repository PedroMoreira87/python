# Entrada de dados
from math import sqrt
n1 = float(input('Qual o tamanho do lado a?'))
n2 = float(input('Qual o tamanhdo do lado b?'))
n3 = float(input('Qual o tamanhdo do lado c?'))
# Processamento
n4 = (n1 + n2 + n3) / 2
n5 = n4 * (n4 - n1) * (n4 - n2) * (n4 - n3)
n6 = sqrt(n5)
# Saída de dados
print(f'A área do triângulo é: {n6:.2f}')
