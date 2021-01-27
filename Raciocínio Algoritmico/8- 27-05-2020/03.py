# Arrumar a matriz
# def aloca_linha(m):
#     return m + 1 * [0]
#
#
# def aloca_matriz(n, m):
#     mat = []
#     for i in range(n):
#         mat.append(aloca_linha(m))
#     return mat
#
#
# m = aloca_matriz(5, 2)
# print(m)

import functools


def aloca_linha(n, m):
    line = ['0' for j in range(m)]
    line[n] = '1'
    return line


def aloca_matriz(n, m):
    mat = []
    if n != m:
        return None
    if n <= 0 or m <= 0:
        return None
    for i in range(n):
        mat.append(aloca_linha(i, m))
    return mat


def printMat(mat):
    for line in mat:
        print(' | ' + functools.reduce(lambda a, b: a + ' | ' + b, line) + ' | ')
# Serve para formatação de matriz


printMat(aloca_matriz(5, 5))


# Outra forma de fazer o exercício
# import numpy
#
#
# def aloca_matriz(m):
#     ma = []
#     for i in range(len(m)):
#         linha = []
#         for j in range(len(m)):
#             linha.append(0)
#         ma.append(linha)
#
#     for i in range(len(m)):
#         for j in range(len(m)):
#             if i == j:
#                 ma[i][j] = 1
#     return ma
#
#
# qualquer = numpy.random.randint(1, 9, size=(5, 5))
#
# print(qualquer)
# print(aloca_matriz(qualquer))
