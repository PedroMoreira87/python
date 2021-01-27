def fib(n):
    # criterios de parada
    if n < 0:
        return -1  # criterio de erro
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


posicao = 20
print(fib(posicao))
