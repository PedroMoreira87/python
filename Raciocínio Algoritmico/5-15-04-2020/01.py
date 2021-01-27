def delta(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def bhaskara(a, b, c):
    d = delta(a, b, c)
    r1 = -b + (d ** 0.5) / (2 * a)
    r2 = -b - (d ** 0.5) / (2 * a)
    return r1, r2  # Tupla


# Criar variáveis
a = 2
b = 1
c = -10

raiz1, raiz2 = bhaskara(a, b, c)

print(raiz1)
print(raiz2)
