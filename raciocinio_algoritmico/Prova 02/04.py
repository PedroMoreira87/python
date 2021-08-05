# Um programador foi incumbido de escrever uma função chamada aloca_matriz que, a partir de dois parâmetros n e m,
# aloque uma matriz usando listas em Python com n linhas e m colunas e que instanciasse seus valores como uma matriz
# identidade. Lembre-se: uma matriz identidade é aquela cuja diagonal principal possui valores 1.0 (um) e os demais
# valores são 0.0 (zero). O código criado pelo programador está abaixo, contudo, ele está incorreto. Seu objetivo é
# então corrigir este código para garantir que seu funcionamento seja correto e que nenhuma matriz seja retornada
# caso os valores de n e m sejam inválidos (retorne Null neste caso).
# Código
# original
#
#
# def aloca_linha(m):
#     return m + 1 * [0]
#
#
# def aloca_matriz(n, m):
#     mat = []
#
#     for i in range(n):
#         mat.append(aloca_linha(m))
#
#     return mat
#
#
# m = aloca_matriz(5, 2)
#
# print(m)


def aloca_linha(n, m):
    linha = [0 for _ in range(m)]
    linha[n] = 1
    return linha


def aloca_matriz(n, m):
    mat = []
    if n != m:
        return None
    if n <= 0 or m <= 0:
        return None
    for i in range(n):
        mat.append(aloca_linha(i, m))
    return mat


print((aloca_matriz(4, 4)))
