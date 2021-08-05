# Entrada de dados
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))
# Processamento
imc = peso / (altura ** 2)
# Saída de dados
print(f'Seu IMC é: {imc:.2f}')
if imc < 17:
    print('Muito abaixo do peso')
elif imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Acima do peso')
elif imc < 35:
    print('Obesidade I')
elif imc < 40:
    print('Obesidade II (severa)')
else:
    print('Obesidade III (mórbida)')
