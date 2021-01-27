# Entrada de dados
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
# Processamento
delta = b ** 2 - 4 * a * c
# Saida de dados
if delta < 0:
    print('Nao existem raizes reais')
elif delta == 0:
    r1 = (-b + delta ** (1 / 2.0)) / (2 * a)
    print('Existe apenas uma raiz')
    print(r1)
else:
    r1 = (-b + delta ** (1 / 2.0)) / (2 * a)
    r2 = (-b - delta ** (1 / 2.0)) / (2 * a)
    print(r1)
    print(r2)
