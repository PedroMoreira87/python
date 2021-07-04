# Entregar arquivo com o código da função teste_cartela
#
# Verificador de cartela de bingo
#
# CRIAR UMA FUNÇÃO DO TIPO:
#
# def teste_cartela(numeros_bilhete,numeros_sorteados): #numeros_bilhete e numeros_sorteados tipo lista com valores inteiros
#
# ...
#
# return([bingo,n_acertos,p_acertos,[numeros_acertados],[numeros_faltantes]]) #retorno tipo lista
#
# ps: a função deve suportar qualquer tamanho das listas
#
# exemplo1:
#
# bilhete=[1,2,3,4,6]
#
# sorteados=[1,2,3,4,5,6,7,8,9,10]
#
# x=teste_cartela(bilhete,sorteados)
#
# print(x)
#
# [true,5,100.0,[1,2,3,4,6],[]]
#
# print(x[1])
#
# 5
#
# exemplo2:
# bilhete=[1,4,7,13,20,22]
#
# sorteados=[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#
# x=teste_cartela(bilhete,sorteados)
#
# print(x)
#
# [False,3,50.0,[13,20,22],[1,4,7]]
#
# print(x[3])
#
# [13,20,22]

bilhete1 = [1, 2, 3, 4, 6]
sorteados1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bilhete2 = [1, 4, 7, 13, 20, 22]
sorteados2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


def teste_cartela(numeros_bilhete, numeros_sorteados):
    bingo = False
    n_acertos = 0
    numeros_acertados = []

    for element in numeros_sorteados:  # outro modo de fazer list(set(sorteados).intersection(bilhete))
        if element in numeros_bilhete:
            numeros_acertados.append(element)
            n_acertos += 1

    numeros_faltantes = list(set(numeros_bilhete) - set(numeros_sorteados))

    if numeros_bilhete == numeros_acertados:
        bingo = True

    p_acertos = len(numeros_acertados) * 100 / len(numeros_bilhete)

    return [bingo, n_acertos, p_acertos, numeros_acertados, numeros_faltantes]


print(teste_cartela(bilhete1, sorteados1))
