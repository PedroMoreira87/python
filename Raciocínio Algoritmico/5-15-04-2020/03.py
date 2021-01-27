x = 1


def num(x):
    n = int(input('Escolha um número: '))
    while x <= n:
        if x % 3 == 0 and x % 5 == 0:
            print(x)
        x = x + 1


print(num(x))
