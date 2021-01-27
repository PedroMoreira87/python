# Entrada de dados
anos = int(input('Qual a sua idade em anos? '))
meses = int(input('Qual a sua idade em meses? '))
dias = int(input('Qual a sua idade em dias? '))
# Processamento
n = 365 * anos + meses * 12 + dias
# Saída de dados
print(f'Sua idade em dias é: {n}')
