"""Exercício 61 lista 3"""


def calcH(n):
    return sum([1 / i for i in range(1, n + 1)])


n1 = int(input('Digite o valor de N:'))
print(f'{calcH(n1):.2f}')
