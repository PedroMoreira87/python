# A série de Fibonacci é formada pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc. Nesta sequência,
# cada termo é definido pela soma dos dois anteriores. Um programador tentou escrever uma função que retornasse até a
# n-ésima posição desta sequência, contudo, o código não funciona de forma apropriada. Seu objetivo é corrigir esta
# função no espaço fornecido abaixo.
#
# Dicas: (i) Lembre-se de verificar valores pequenos de n. (ii) Verifique laços de repetição infinitos. (iii) Use
# teste de mesa para verificar a função abaixo passo a passo.
#
# Código
# original
#
#
# def fibonacci(n):
#     a = 0
#
#     b = 1
#
#     fib_vals = [a, b]
#
#     while fib_vals != n:
#         soma = a + b
#
#         fib_vals.append(soma)
#
#         b = soma
#
#         a = b
#
#     return fib_vals


def fibonacci(n):
    a = 0
    b = 1
    fib_vals = [a, b]
    while b < n:  # Não estou conseguindo pegar pelo indice, somente pelo valor.
        a, b = b, a + b
        fib_vals.append(b)
    return fib_vals


termos = 20
print(fibonacci(termos))
