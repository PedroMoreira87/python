# o perceptron de uma camada só consegue tratar problemas linearmente separáveis (faço uma reta e consigo separar o 1 do 0)
# função de ativação utilizada: step function

import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 0, 0, 1])  # tabela do AND -- linearmente separável
# entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# saidas = np.array([0, 1, 1, 1])  # tabela do OR -- linearmente separável
# entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# saidas = np.array([0, 1, 1, 0])  # tabela do XOR -- não é linearmente separável
pesos = np.array([0.0, 0.0])
taxa_aprendizagem = 0.1


def step_function(soma):
    if soma >= 1:
        return 1
    return 0


def calcula_saida(registro):  # multiplica as entradas pelos pesos
    # s = 0
    # for i in range(len(entradas)):
    #     s += entradas[i] * pesos[i]
    # return s
    s = registro.dot(pesos)  # dot product / produto escalar
    return step_function(s)


def treinar():
    erro_total = 1
    while erro_total != 0:
        erro_total = 0
        for i in range(len(saidas)):
            saida_calculada = calcula_saida(np.asarray(entradas[i]))
            erro = saidas[i] - saida_calculada
            erro_total += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)  # os pesos são atualizados até os erros serem pequenos
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erro_total))


treinar()
print('Rede neural treinada')
print(calcula_saida(entradas[0]))
print(calcula_saida(entradas[1]))
print(calcula_saida(entradas[2]))
print(calcula_saida(entradas[3]))
