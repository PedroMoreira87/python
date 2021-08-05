# Entrada de dados
razão = int(input('Qual a razão? '))
primeiro = int(input('Qual o primeiro termo? '))
# Processamento
décimo = primeiro + (10 - 1) * razão
# Saída de dados
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' > ')
print('ACABOU')
