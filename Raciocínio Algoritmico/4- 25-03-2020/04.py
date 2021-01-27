"""matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[2][0])
print(matriz[2][1])
print(matriz[2][2])
print(matriz[0][0] + matriz[0][1] + matriz[0][2] + matriz[1][0] + matriz[1][1] + matriz[1][2] + matriz[2][0] + matriz[2][1] + matriz[2][2])"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
for linha in range(3):
    for coluna in range(3):
        print(matriz[linha][coluna])
        soma += matriz[linha][coluna]
print(soma)
