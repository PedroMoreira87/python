# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
#
# print(((1-4) ** 2 + (4-4) ** 2 + (7-4) ** 2)/3)


def constroi_matriz(n, m):
    mat = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(0)
        mat.append(linha)
    return mat


def popula_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = float(input(f'Digite o valor para a posição ({i}, {j}): '))
    return mat


def pega_coluna(mat, c):
    col = []
    for i in range(len(mat)):
        col.append(mat[i][c])
    return col


def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma / len(lista)


def variancia(lista):
    mu = media(lista)

    var = 0
    for i in range(len(lista)):
        var += (lista[i] - mu) ** 2

    var /= len(lista)
    return var


def moda(lista):
    # contar os números
    # dicionário no formato <chave, valor>, sendo que
    # chave é um número e valor é a quantidade de ocorrências
    contagem = {}
    for i in range(len(lista)):
        if lista[i] in contagem:  # valor já existe?
            # incrementando a contagem de um valor que já foi visto antes
            contagem[lista[i]] += 1
        else:
            # é a primeira vez que vemos esse valor em específico
            contagem[lista[i]] = 1

    # verificar quais números mais se repetiram
    # 1, 2, 3, 4 -> amodal (sem moda)
    # 1, 1, 2, 3, 4 -> 1 é a moda
    # 1, 1, 2, 2, 3, 4 -> bimodal (tanto 1 quanto 2 são modas)

    modas = []
    vezes = 0
    for num, qtd in contagem.items():
        if qtd > vezes:  # a moda mudou
            modas = [num]
            vezes = qtd
        elif qtd == vezes:  # mais uma moda
            modas.append(num)

    # teste para verificar se o conjunto é amodal
    if vezes == 1:
        modas = []

    return modas


mat = constroi_matriz(3, 3)
mat = popula_matriz(mat)

col_0 = pega_coluna(mat, 0)
print(f'Media coluna 0: {media(col_0)}')
print(f'Moda coluna 0: {moda(col_0)}')
print(f'Variância coluna 0: {variancia(col_0)}')
