# Um programador foi incumbido de desenvolver uma função que recebe como parâmetro uma lista de valores inteiros (
# tipo int) e que retornasse outra lista com o dobro dos valores pares e o triplo dos valores ímpares existentes na
# lista original. Infelizmente, o programador não terminou a função e você deve completá-la abaixo:
#
# Código a ser completado
#
# def dobro_triplo(lista):
#
#     l_ret = []
#
#     for i in range(___________):
#
#         if l[i] % 2 == 0:
#
#             l_ret.append(2 * lista[i])
#
#             ___________________:
#
#             l_ret.append(3 * lista[i])
#
#     return l_ret


def dobro_triplo(lista):
    l_ret = []
    for i in range(len(lista)):
        if i % 2 == 0:
            l_ret.append(2 * lista[i])
        else:
            l_ret.append(2 * lista[i])
    return l_ret


l1 = [2, 3, 4, 5, 6]

print(dobro_triplo(l1))
