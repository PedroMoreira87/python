def fat_recursivo(n):
    if n < 0:  # caso de erro (criterio de parada)
        return -1
    elif n == 0 or n == 1:  # criterio de parada
        # (0!) = 1, assim como (1!) = 1
        return 1
    return n * fat_recursivo(n - 1)


print(fat_recursivo(3))

# Se você usar o debug vai conseguir ver as pilhas de chamada sendo feitas
# Quando for para o print as pilhas de chamada vão desaparecendo
# Se não tiver um critério de parada vai dar STACK OVERFLOW
