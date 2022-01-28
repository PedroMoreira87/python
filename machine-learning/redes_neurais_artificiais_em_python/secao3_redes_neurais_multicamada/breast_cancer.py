# tipos de funções de ativação: https://en.wikipedia.org/wiki/Activation_function
# numpy exp: http://pyscience-brasil.wikidot.com/docitem:numpy-exp
# função de ativação utilizada: sigmoid
# dataset https://archive.ics.uci.edu/ml/index.php

import numpy as np
from sklearn import datasets


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


def sigmoid_derivada(sig):
    return sig * (1 - sig)


base = datasets.load_breast_cancer()
entradas = base.data
valoresSaida = base.target
saidas = np.empty([569, 1], dtype=int)
for i in range(569):
    saidas[i] = valoresSaida[i]

# pesos inicializados com valores aleatórios // -1 para deixar negativo e 2 para randomizar o negativo
pesos0 = 2 * np.random.random((30, 5)) - 1
pesos1 = 2 * np.random.random((5, 1)) - 1

epocas = 10000  # pois as vezes os pesos podem nunca chegar no valor correto
taxa_aprendizagem = 0.3
momento = 1

for j in range(epocas):
    # soma e função de ativação na camada oculta // feedforward
    camada_entrada = entradas
    soma_sinapse0 = np.dot(camada_entrada, pesos0)
    camada_oculta = sigmoid(soma_sinapse0)

    # soma e função de ativação na camada de saída
    soma_sinapse1 = np.dot(camada_oculta, pesos1)
    camada_saida = sigmoid(soma_sinapse1)

    # cálculo do erro
    erro_camada_saida = saidas - camada_saida
    media_absoluta = np.mean(
        abs(erro_camada_saida))  # cost function // abs é usado para fazer a média com números absolutos, ignorando negativos
    print("Erro: " + str(media_absoluta))

    # cálculo do delta da saída
    derivada_saida = sigmoid_derivada(camada_saida)
    delta_saida = erro_camada_saida * derivada_saida

    # cálculo do delta da camada oculta
    pesos1_transposta = pesos1.T  # transposição de matriz
    delta_saida_x_peso = delta_saida.dot(pesos1_transposta)
    delta_camada_oculta = delta_saida_x_peso * sigmoid_derivada(camada_oculta)

    # ajuste dos pesos da camada oculta para a camada de saída // backpropagation
    camada_oculta_transposta = camada_oculta.T  # transposição de matriz
    pesos_novo1 = camada_oculta_transposta.dot(delta_saida)
    pesos1 = (pesos1 * momento) + (pesos_novo1 * taxa_aprendizagem)

    # ajuste dos pesos da camada de entrada para a camada oculta
    camada_entrada_transposta = camada_entrada.T
    pesos_novo0 = camada_entrada_transposta.dot(delta_camada_oculta)
    pesos0 = (pesos0 * momento) + (pesos_novo0 * taxa_aprendizagem)
