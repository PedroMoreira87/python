# Entrada de dados
saldo_cc = float(input('Informe o saldo da sua conta corrente: '))
# Saída de dados
if saldo_cc < 0:
    print('Seu saldo é negativo')
elif saldo_cc > 0:
    print('Seu saldo é positivo')
else:
    print('Sua conta esta zerada')
