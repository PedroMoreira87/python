def cadastro():
    matriz_credenciais = [["vilmar", "123456", 0], ["junior", "abcdef", 0]]

    loop = True
    while loop:
        usuario = input("Digite seu usuario: ")
        senha = input("Digite sua senha: ")

        for credencial in matriz_credenciais:
            usuario_corrente = credencial[0]
            senha_corrente = credencial[1]
            tentativas = credencial[2]

            if usuario == usuario_corrente and senha == senha_corrente:
                if tentativas < 5:
                    credencial[2] = 0
                    loop = False
                else:
                    print("Usuario esta bloqueado, contate o administrador!")
            elif usuario == usuario_corrente:
                credencial[2] = tentativas + 1
                if credencial[2] >= 5:
                    print("Usuario foi bloqueado!")

        if loop is True:
            print("Usuario ou senha invalido!")
        else:
            print("Usuario autenticado com sucesso!")


def menu():
    try:
        ordem = int(input('Olá, usuário.'
                          '\n1 - Para cadastro de uma nova conta digite.'
                          '\n2 -Para encerrar o programa digite: (Sair)'
                          '\n> '))
        if ordem == 1:
            cadastro()
        elif ordem == 2:
            pass
        else:
            return menu()
    except ValueError:
        print('====================\nValor incorreto.\n====================')
        return menu()


menu()
