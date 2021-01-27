# Entrada de dados
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
# Processamento
gotamg = 20 / 500.0
# Saída de dados
# Adulto
if idade >= 12:
    if peso >= 60:
        print(gotamg * 1000)
    else:
        print(gotamg * 875)
# Adolescente
else:
    if 5 <= peso <= 9:
        print(gotamg * 125)
    elif 9 < peso <= 16:
        print(gotamg * 250)
    elif 16 < peso <= 24:
        print(gotamg * 375)
    elif 24 < peso <= 30:
        print(gotamg * 500)
    elif peso > 30:
        print(gotamg * 750)
    else:
        print('Você não pode tomar o remédio')
