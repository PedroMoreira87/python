# Entrada de dados
from math import floor
n1 = float(input('Digite o número de aulas:'))
# Processamento
n2 = n1 * 0.25
n3 = floor(n2)
# Saída de dados
print(f'Como RA tem {n1} aulas, você pode faltar {n3} vezes')
