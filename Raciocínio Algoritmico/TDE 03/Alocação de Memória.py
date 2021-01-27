import random

memoria = []
memoriatira = []

linhas = 0
colunas = 0


def cria_matriz():
    # criação da matriz
    global memoria
    global memoriatira
    global linhas
    global colunas
    linhas = int(input("Digite quantas linhas você quer na matriz:"))
    colunas = int(input("Digite quantas colunas você quer na matriz:"))
    print('=' * 120)
    for x in range(linhas):
        # cria uma matriz e uma lista clone para alocar a memória
        memoria.append([])
        for y in range(colunas):
            if random.randint(0, 1) == 1:
                memoria[x].append(1)
                memoriatira.append(1)
            else:
                memoria[x].append(0)
                memoriatira.append(0)
    matriz_grafica()


def matriz_grafica():
    # cria a matriz gráfica
    for x in range(len(memoria)):
        linha = ''
        for y in range(len(memoria[x])):
            if memoria[x][y] == 0:
                linha = linha + ' |'
            else:
                linha = linha + 'X|'
        print(linha)
    print('=' * 120)
    menu()


def const_matriz():
    # reconstroi a matriz
    global memoria
    memoria = []
    index = 0
    for x in range(linhas):
        memoria.append([])

    for x in range(len(memoriatira)):
        if x % colunas == 0 and x > 0:
            index += 1
        memoria[index].append(memoriatira[x])


def first_fit():
    # first fit
    global memoria
    global memoriatira
    raio = int(input("Digite quantas espaços você quer alocar:"))
    print('=' * 120)
    # percorre a tira e se no range de raio tiver 1 ele da break pois a memoria não pode ser alocada
    for x in range(len(memoriatira)):
        for r in range(raio):
            try:
                if memoriatira[x + r] == 1:  # x nesta posição vai ser sempre 0
                    break
            except IndexError:
                pass
        else:
            for r in range(raio):
                try:
                    memoriatira[x + r] = 1
                except IndexError:
                    pass
            const_matriz()
            matriz_grafica()
            return
    print('Não foi possível alocar com o first fit')


def best_fit():
    # best fit
    global memoria
    global memoriatira
    raio = int(input("Digite quantas espaços você quer alocar:"))
    print('=' * 120)
    resultado = []
    for x in range(len(memoriatira)):
        if memoriatira[x - 1] == 0 and x != 0:
            continue
        for r in range(raio):
            try:
                if memoriatira[x + r] == 1:  # x nesta posição vai ser sempre 0
                    break
            except IndexError:
                pass
        else:
            cont = 0
            for contador in memoriatira[x:]:
                if contador == 1:
                    resultado.append([x, cont])
                    break
                cont += 1
    try:
        menorvalor = resultado[0][1]
        coordenada = resultado[0][0]
        for x in range(len(resultado)):
            if resultado[x][1] < menorvalor:
                menorvalor = resultado[x][1]
                coordenada = resultado[x][0]
        print(f'A coordenada correta é: {coordenada}')
    except IndexError:
        print('Não foi possível alocar com o best fit')
    for r in range(coordenada, coordenada + raio):
        memoriatira[r] = 1
    const_matriz()
    matriz_grafica()


def worst_fit():
    # worst fit
    global memoria
    global memoriatira
    raio = int(input("Digite quantas espaços você quer alocar:"))
    print('=' * 120)
    resultado = []
    for x in range(len(memoriatira)):
        if memoriatira[x - 1] == 0 and x != 0:
            continue
        for r in range(raio):
            try:
                if memoriatira[x + r] == 1:  # x nesta posição vai ser sempre 0
                    break
            except IndexError:
                pass
        else:
            cont = 0
            for contador in memoriatira[x:]:
                if contador == 1:
                    resultado.append([x, cont])
                    break
                cont += 1
            for contador in memoriatira[x:-1]:
                if contador == 0:
                    resultado.append([x, cont])
                    break
                cont += 1
    try:
        maiorvalor = resultado[0][1]
        coordenada = resultado[0][0]
        for x in range(len(resultado)):
            if resultado[x][1] > maiorvalor:
                maiorvalor = resultado[x][1]
                coordenada = resultado[x][0]
        print(f'A coordenada correta é: {coordenada}')
    except IndexError:
        print('Não foi possível alocar com o best fit')
    for r in range(coordenada, coordenada + raio):
        memoriatira[r] = 1
    const_matriz()
    matriz_grafica()


def desalocacao():
    # desalocação
    global memoriatira
    global memoria
    linha_ini = int(input('Digite a linha de inicio para desalocar: '))
    coluna_ini = int(input('Digite a coluna de inicio para desalocar: '))
    linha_fim = int(input('Digite a linha de fim para desalocar: '))
    coluna_fim = int(input('Digite a coluna de fim para desalocar: '))
    if linha_ini > linha_fim:
        print('Coordenadas invalidas!')
        print('=' * 120)
        menu()
    else:
        try:
            for x in range(coluna_ini, len(memoria[linha_ini])):
                memoria[linha_ini][x] = 0
            for x in range(linha_ini + 1, linha_fim):
                for y in range(len(memoria[x])):
                    memoria[x][y] = 0
            for x in range(coluna_fim + 1):
                memoria[linha_fim][x] = 0
            # matriz_grafica()
        except IndexError:
            print('Coordenadas invalidas!')
            print('=' * 120)
            menu()
    memoriatira = []
    for x in range(len(memoria)):
        for y in range(len(memoria[x])):
            memoriatira.append(memoria[x][y])
    const_matriz()
    matriz_grafica()


# menu para o usuário
def menu():
    try:
        ordem = int(input('Olá, usuário.'
                          '\n1 - Para criar uma matriz'
                          '\n2 - Para alocação first fit'
                          '\n3 - Para alocação best fit'
                          '\n4 - Para alocação worst fit'
                          '\n5 - Para desalocar a memória'
                          '\n6 - Para modo de teste'
                          '\n7 - Para encerrar o programa'
                          '\n> '))
        if ordem == 1:
            cria_matriz()

        elif ordem == 2:
            first_fit()

        elif ordem == 3:
            best_fit()

        elif ordem == 4:
            worst_fit()

        elif ordem == 5:
            desalocacao()

        elif ordem == 6:
            pass

        elif ordem == 7:
            pass
        else:
            return menu()
    except ValueError:
        print('====================\nValor incorreto.\n====================')
        return menu()


menu()
