# Entrada de dados
numeros = int(input('Qual os números da placa? '))
mes_atual = (int(input('Mês atual: ')))
# Processamento
digito = numeros % 10
# Saída de dados
if digito == mes_atual:
    print('IPVA vence este mês!')
else:
    print('IPVA vence outro mês!')
    if digito == 1:
        print('IPVA vence em janeiro!')
    elif digito == 2:
        print('IPVA vence em fevereiro!')
    elif digito == 3:
        print('IPVA vence em março!')
    elif digito == 4:
        print('IPVA vence em abril!')
    elif digito == 5:
        print('IPVA vence em maio!')
    elif digito == 6:
        print('IPVA vence em junho!')
    elif digito == 7:
        print('IPVA vence em julho!')
    elif digito == 8:
        print('IPVA vence em agosto!')
    elif digito == 9:
        print('IPVA vence em setembro!')
    else:
        print('IPVA vence em outubro!')
