import pickle
import random
import string

pickle_out = open('gerente.pickle', 'wb')

contas = {}

nomes = []


while True:
    ordem = input('Olá, usuário.'
                  '\nPara cadastro de uma nova conta digite: (Cadastro)'
                  '\nPara busca de uma conta corrente digite: (Busca)'
                  '\nPara definição de nova senha digite: (Nova senha)'
                  '\nPara encerrar o programa digite: (Sair)'
                  '\n> ').lower()

    if ordem.startswith('cadastro'):
        dados = {}

        while True:
            nome = input('Digite o nome do cliente: ')
            if all(nome.isalpha() or nome.isspace() for nome in nome):
                nome = nome.title()
                nomes.append(nome)
                break
            else:
                print('Digite apenas letras!')

        profissao = input('Profissão: ')
        if profissao[0].islower():
            profissao = profissao.title()
        dados['Profissão'] = profissao

        renda_mensal = input('Renda mensal: R$')
        dados['Renda mensal'] = renda_mensal

        endereco = input('Endereço: ')
        if endereco[0].islower():
            endereco = endereco.title()
        dados['Endereço'] = endereco

        telefone = input('Telefone: ')
        dados['Telefone'] = telefone

        while True:
            numero_conta = input('O número da conta corrente deverá conter 5 dígitos!'
                                 '\nO número da conta corrente deverá ser do tipo inteiro!'
                                 '\nNúmero da conta corrente: ')
            dados['Conta corrente'] = numero_conta
            if not numero_conta.isdigit():  # porque ele faz o trajeto corretamente com o not e não com o normal
                print('Erro!')  # com o normal ele conta 5 mesmo usando a letra e aceita ex: "ds233"
            elif not len(numero_conta) == 5:
                print('Erro!')
            else:
                break

        senha = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        dados['Senha'] = senha
        print(f'A senha provisória do cliente será: {senha}')

        saldo = random.randint(100, 10000)
        dados['Saldo'] = saldo
        print(f'O saldo do cliente é: R${saldo},00')

        print('======================================================================')
        print('NOVA CONTA CRIADA COM SUCESSO!')
        print('======================================================================')

        contas[nome] = dados

    elif ordem.startswith('busca'):
        while True:
            nome = input('Digite o nome do cliente: ')
            nome = nome.title()
            if nome in nomes:
                print(f'Conta corrente', contas[nome].get('Conta corrente'))
                print('======================================================================')
                break
            else:
                print('Erro! Conta invalida')

    elif ordem.startswith('nova senha'):
        while True:
            numero_conta = input('Digite o número da conta corrente: ')
            if numero_conta == dados['Conta corrente']:
                break
        while True:
            senha_especial = '!@#$%&_=´`^~*éúóáçà'
            if numero_conta == dados['Conta corrente']:
                nova_senha = input('A nova senha deve conter entre 4 a 8 caracteres alfanuméricos!'
                                   '\nA nova senha não pode conter acentos e/ou caracteres especiais!'
                                   '\nNova senha: ')
                if not 4 <= len(nova_senha) <= 8:
                    # porque se eu cololocar um 'and' e juntar com o '<=' ele não funciona?
                    print('Erro!')
                elif not any(char.isdigit() for char in nova_senha):
                    print('Erro!')
                elif not any(char.isalpha() for char in nova_senha):
                    print('Erro!')
                elif any(char in senha_especial for char in nova_senha):
                    print('Erro!')
                else:
                    dados['Senha'] = nova_senha
                    print('======================================================================')
                    print('NOVA SENHA CRIADA COM SUCESSO!')
                    print('======================================================================')
                    break

    elif ordem.startswith('sair'):
        break

nomes.sort()
for nome in nomes:
    print('Nome: ', nome)
    print('Profissão: ', contas[nome].get('Profissão'))
    print('Renda mensal: R$', contas[nome].get('Renda mensal'))
    print('Endereço: ', contas[nome].get('Endereço'))
    print('Telefone: ', contas[nome].get('Telefone'))
    print('Conta corrente: ', contas[nome].get('Conta corrente'))
    print('Senha: ', contas[nome].get('Senha'))
    print('Saldo: ', contas[nome].get('Saldo'))
    print('======================================================================')

# pickle.dump(nomes, pickle_out)
# pickle.dump(dados, pickle_out)
pickle.dump(contas, pickle_out)

pickle_out.close()
