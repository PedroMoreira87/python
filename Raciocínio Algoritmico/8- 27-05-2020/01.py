"""Exercício 58 lista 3"""

import numpy


# Foi utilizado o numpy para criar uma matriz randomica

def matriz(m):
    ma = []
    for i in range(len(m)):
        linha = []
        for j in range(len(m[i])):
            linha.append(0)
        ma.append(linha)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if i != j:
                ma[i][j] = m[i][j]
    return ma


def rand_mat():
    qualquer = numpy.random.randint(1, 9, size=(4, 4))
    return qualquer
    # numpy.random.randint(low, high=None, size=None, dtype='l')
    # low = Lowest (signed) integer to be drawn from the distribution
    # high(optional)= If provided, one above the largest (signed) integer to be drawn from the distribution
    # size(optional) = Output shape i.e. if the given shape is, e.g., (m, n, k), then m * n * k samples are drawn
    # dtype(optional) = Desired dtype of the result.


print(rand_mat())
print(matriz(rand_mat()))

# qualquer = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print(qualquer)
