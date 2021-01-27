# Entrada de dados
a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
# Processamento
# A como primeiro
ordem = a, b, c
if a <= c <= b:
    ordem = a, c, b
# B como primeiro
if b <= a <= c:
    ordem = b, a, c
if b <= c <= a:
    ordem = b, c, a
# C como primeiro
if c <= a <= b:
    ordem = c, a, b
if c <= b <= a:
    ordem = c, b, a
# Saída de dados
print(f'Os números digitados em ordem crescente são: {ordem}')
