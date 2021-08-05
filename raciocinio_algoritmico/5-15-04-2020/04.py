def x():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    soma = 0
    for lista in range(len(matrix)):
        for elemento in range(lista + 1, len(matrix)):
            soma = soma + matrix[lista][elemento]
    print(soma)


x()
