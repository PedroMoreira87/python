hexa_legal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ "
print("")
print("*O CAPSLOCK DEVE ESTAR ATIVADO PARA O PROGRAMA FUNCIONAR CORRETAMENTE*")


# NUMEROS DECIMAIS para NUMEROS X:
def decParaX(dec, baseX):
    listaDosRestos = []
    resultados = int(dec)

    while resultados + 1 > baseX:  # PUPULA A LISTA DOS RESTOS
        listaDosRestos.append(resultados % baseX)
        resultados = resultados // baseX
    listaDosRestos.append(resultados % baseX)

    for i in range(len(listaDosRestos)):  # AJUSTA OS NUMEROS DE ACORDO COM A BASE DE X
        listaDosRestos[i] = hexa_legal[listaDosRestos[i]]

    finalResult10Para = ""  # CONCATENA OS RESTOS NO RESULTADO FINAL
    for i in range(len(listaDosRestos) - 1, -1, -1):
        finalResult10Para += str(listaDosRestos[i])

    print(f"Numero retornado: {finalResult10Para} (base: {baseX})")
    print("")


# NUMEROS X para NUMEROS DECIMAIS:
def xParaDec(x, baseX):
    listaX = []
    listaConversao = []

    for i in range(len(str(x)) - 1, -1, -1):  # INVERTE A ORDEM DO NUMERO INSERIDO
        listaX.append(str(x)[i])

    for i in range(len(listaX)):  # CONVERTE POSSIVEIS "LETRAS" EM NUMEROS DECIMAIS
        for j in range(len(hexa_legal)):
            if listaX[i] == hexa_legal[j]:
                listaX[i] = j

    for i in range(len(listaX)):  # REALIZA A CONVERSAO
        y = int(listaX[i]) * (baseX ** i)
        listaConversao.append(y)

    finalResultPara10 = 0
    for i in listaConversao:  # SOMA OS NUMEROS CONVERTIDOS NO RESULTADO FINAL
        finalResultPara10 += int(i)

    if mudancaDupla:
        return finalResultPara10
    else:
        print(f"Decimal retornado: {finalResultPara10}")
        print("")
        return finalResultPara10


runAgain = True

while runAgain:

    print("")
    numInput = input("Digite um numero para ser convertido: ")
    baseInput = int(input("Digite a base numerica desse numero: "))
    baseOutput = int(input("Digite a casa numerica para transformar esse numero: "))
    print("")

    if baseInput == 10:
        mudancaDupla = False
        decParaX(numInput, baseOutput)

    elif baseOutput == 10:
        mudancaDupla = False
        xParaDec(numInput, baseInput)

    else:
        mudancaDupla = True
        decParaX(xParaDec(numInput, baseInput), baseOutput)

    rodarDnv = input("Deseja fechar o programa? (Y/N) ")
    print("")

    if rodarDnv == "Y":
        runAgain = False
