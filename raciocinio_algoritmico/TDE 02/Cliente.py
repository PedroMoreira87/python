import pickle

pickle_in = open('gerente.pickle', 'rb')
# nomes = pickle.load(pickle_in)
# dados = pickle.load(pickle_in)  # porque ele está importando o nomes no lugar do contas??
contas = pickle.load(pickle_in)

# print(nomes)
# print('============')
# print(dados)
# print('============')
print(contas)
print('============')

while True:
    seu_nome = input('Digite o seu nome cadastrado: ')
    if seu_nome not in contas:
        print('Nome não cadastrado')
    else:
        ordem = input(f'Olá, {seu_nome}.'
                      '\nPara saque digite: (Saque)'
                      '\nPara depósito digite: (Depósito)'
                      '\nPara visualização de saldo digite: (Saldo)'
                      '\nPara simulação de investimento digite: (Simulação)'
                      '\nPara encerrar o programa digite: (Sair)'
                      '\n> ').lower()

        if ordem.startswith('saque'):  # incompleto
            while True:
                numero_conta = input('Digite o número da conta corrente: ')
                senha = input('Digite senha da conta corrente: ')
                if numero_conta not in contas[seu_nome].get('Conta corrente'):
                    print('Erro! Conta corrente incorreta')
                elif senha not in contas[seu_nome].get('Senha'):
                    print('Erro! Senha incorreta')
                else:
                    print('Acesso concedido!')
                    print('Seu saldo atual é de: R$', contas[seu_nome].get('Saldo'))
                    saque = input('Digite o valor a ser sacado: R$')
                    break

        if ordem.startswith('depósito'):  # incompleto
            while True:
                numero_conta = input('Digite o número da conta corrente: ')
                senha = input('Digite senha da conta corrente: ')
                if numero_conta not in contas[seu_nome].get('Conta corrente'):
                    print('Erro! Conta corrente incorreta')
                elif senha not in contas[seu_nome].get('Senha'):
                    print('Erro! Senha incorreta')
                else:
                    print('Acesso concedido!')
                    break

        if ordem.startswith('saldo'):
            while True:
                numero_conta = input('Digite o número da conta corrente: ')
                senha = input('Digite senha da conta corrente: ')
                if numero_conta not in contas[seu_nome].get('Conta corrente'):
                    print('Erro! Conta corrente incorreta')
                elif senha not in contas[seu_nome].get('Senha'):
                    print('Erro! Senha incorreta')
                else:
                    print('Acesso concedido!')
                    print('Nome completo:', seu_nome)
                    print('Conta corrente:', contas[seu_nome].get('Conta corrente'))
                    print('Saldo atual: R$', contas[seu_nome].get('Saldo'))
                    break

        if ordem.startswith('simulação'):  # incompleto
            while True:
                numero_conta = input('Digite o número da conta corrente: ')
                senha = input('Digite senha da conta corrente: ')
                if numero_conta not in contas[seu_nome].get('Conta corrente'):
                    print('Erro! Conta corrente incorreta')
                elif senha not in contas[seu_nome].get('Senha'):
                    print('Erro! Senha incorreta')
                else:
                    print('Acesso concedido!')
                    meses_investimento = float(input('Por quantos meses gostaria de investir? '))
                    aporte_inicial = float(input('Qual o valor do aporte inicial? R$'))
                    i = 1.15
                    montante_bruto = aporte_inicial * ((1 + i / 100) ** meses_investimento)
                    taxa = ''
                    if meses_investimento <= 12:
                        taxa = 1 / 100
                    elif meses_investimento > 60:
                        taxa = 0.5 / 100
                    montante_liquido = montante_bruto - (montante_bruto * taxa)
                    print(f'Seu dinheiro renderá: R${montante_liquido:.2f}')
                    break

        if ordem.startswith('sair'):
            break




# while True:
#     numero_conta = input('Digite o número da conta corrente: ')
#     senha = input('Digite senha da conta corrente: ')
#     for id, info in nomes.items():
#         for key in info:
#             if numero_conta == info[key]:
#                 print('Número da conta corrente correto')
#                 break
#     for id, info in nomes.items():
#         for key in info:
#             if senha == info[key]:
#                 print('Número da senha correto')
#                 valor_sacado = input('Qual o valor que deseja sacar? R$')
#                 for id, info in nomes.items():
#                     for key in info:
#                         nomes.pop
#     break
