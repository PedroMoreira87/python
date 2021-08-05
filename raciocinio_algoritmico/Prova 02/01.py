# A função descrita abaixo objetiva retornar o somatório de todos os valores positivos, isto é, maiores que zero,
# fornecidos como parâmetro em uma lista. Infelizmente, o programador cometeu um ou mais erros nesta função e ela
# deve ser corrigida. Desta forma, seu objetivo é reescrever esta função no espaço fornecido abaixo, corrigindo a
# função para que ela funcione de forma adequada.
#
# Código original
#
# def soma_positivos(lista):
#
#     soma = 1
#
#     for i in range(len(lista) + 1):
#
#         if lista[i] > 0:
#
#             soma = lista[i]


def soma_positivos(lista):
    soma = 0
    for i in lista:
        if i > 0:
            soma += i
    return soma


l1 = [2, 3, 4, 5]
print(soma_positivos(l1))
