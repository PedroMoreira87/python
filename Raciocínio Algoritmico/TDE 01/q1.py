# Entrada de dados
r = int(input('Qual a razão da progressão aritmética?'))
a1 = int(input('Qual o primeiro termo da progressão aritmética?'))
n = int(input('Quantos termos a progressão aritmética possui?'))
# Processamento
n3 = a1 + r * (n - 1)
# Saída de dados
print(f'O termo desejado da PA é: {n3}')
