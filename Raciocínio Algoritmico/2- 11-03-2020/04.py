# Entrada de dados
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
n3 = float(input('Insira sua terceira nota: '))
n4 = float(input('Insira sua quarta nota: '))
# Processamento
media = (n1 + n2 + n3 + n4) / 4
# Saída de dados
print(media)
if media >= 7:
    print('Aprovado')
elif 6 <= media >= 4:
    print('Recuperação')
else:
    print('Reprovado')
