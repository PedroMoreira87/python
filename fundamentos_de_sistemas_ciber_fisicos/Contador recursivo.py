base = int(input('Digite a base desejada: '))
digitos = int(input('Digite o número de dígitos: '))

hexa_legal = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def cont_recursivo(base, head, nivel):
    if nivel == 0:
        print(head)
    else:
        for i in range(base):
            cont_recursivo(base, head + hexa_legal[i], nivel - 1)


cont_recursivo(base, '', digitos)
