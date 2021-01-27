# nome = 'Geek University'
# lista = [1, 3, 5, 7, 9]
# numeros = range(1, 10)
#
# for letra in nome:
#     print(letra)
#
# for numero in lista:
#     print(numero)
#
# for numero in range(1, 10):
#     print(numero)


# emoji = '\U0001F605'
# for _ in range(3):
#     for numero in range(1, 11):
#         print(f'{emoji}' * numero)


# for num in range(5, 51, 5):
#     print(num)
#
# for num in range(10, 0, -1):
#     print(num)


# num = 1
# while num < 10:
#     print(num)
#     num = num + 1
#
# resposta = ''
# while resposta != 'sim':
#     resposta = input('Já acagou Jessica? ')


# a = 0
# while a <= 100:
#     if a % 2 != 0:
#         print(a)
#     a = a + 1


# lista1 = [10, 20, 30, 1, 2, 4, 45, 3]
# lista1.append(lista1[2] + lista1[3])
# print(lista1)
#
# if 10 or 20 or 2332 in lista1:
#     print('ok')


# cores = ['verde', 'amarelo', 'azul', 'branco']


# num1, num2, num3, num4 = cores
# print(num1)
# print(num2)
# cores.pop(2)
# print(cores)

# localidades = {
#     'Curitiba': (96.56, 98.62),
#     'Manaus': (65.96, 45.23)
# }
#
# print(localidades)
# print(type(localidades))

# dict = {'cores': 'verde', 'preço': 150.00, 'qualidade': 'boa'}
#
# print(dict.get('cores'), dict.get('preço'))

# carrinho =
#
# produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
# produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}
#
# carrinho['nome'] = 'Playstation 433232'
#
#
# print(carrinho)

# y, x = input('').split(',')
#
# print(y)

# ============================================================================================================
# """
# Escreva um programa que receba quantas entradas o usuário desejar e depois
# crie um novo contato para cada entrada (Nome, Telefone, Endereço, Email), e
# por fim imprima, em ordem alfabética, a agenda de contatos
# """
#
# nomes = []
# agenda = {}
#
# while True:
#     ordem = input('Deseja adicionar um novo contato(add) ou parar a execução(stop)').lower()
#
#     if not ordem.isalpha():
#         print("Digite apenas letras!")
#
#     elif ordem.startswith('a'):
#         contato = {}
#
#         nome = input('Digite o nome do contato: ')
#         if not nome[0].isupper():
#             nome = nome[0].upper() + nome[1:]
#
#         nomes.append(nome)
#
#         tel = input('Digite o telefone do contato: ')
#         contato['Telefone'] = tel
#
#         end = input('Digite o endereço do contato: ')
#         contato['Endereço'] = end
#
#         email = input('Digite o Email do contato: ')
#         contato['Email'] = email
#
#         agenda[nome] = contato
#
#     elif ordem.startswith('s'):
#         break
#
# print('A G E N D A\n')
# nomes.sort()
# for nome in nomes:
#     print('Nome: ', nome)
#     print('Telefone: ', agenda[nome]['Telefone'])
#     print('Endereço: ', agenda[nome]['Endereço'])
#     print('Email: ', agenda[nome]['Email'])
#     print()
#
# saldo = ''.join(random.choice(string.digits) for _ in range(4))
# contato['Saldo'] = saldo
# print(f'O saldo do cliente é: R${saldo},00')
# ============================================================================================================
# import pickle
#
# example_dict = {1:'6', 2:'2', 3:'f'}
#
# pickle_out = open('dict.pickle', 'wb')
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()
#
# pickle_in = open('dict.pickle', 'rb')
# example_dict = pickle.load(pickle_in)
#
#
# print(example_dict)
# print(example_dict[1])
# ============================================================================================================
# ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
# person = input('Get age for: ')
# age = ages.get(person)
#
# if age:
#     print(f'{person} is {age} years old.')
# else:
#     print(f"{person}'s age is unknown.")
# ============================================================================================================
# d = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
#      'emp2': {'name': 'Kim', 'job': 'Dev'},
#      'emp3': {'name': 'Sam', 'job': 'Dev'}}
#
# print(d['emp1'].get('name'))
#
# job = input('Diga o seu trabalho: ')
# test = input('Diga o seu cargo: ')
# if job in d[test].get('job'):
#     print('Deu boa')
# else:
#     print('Deu ruim')
#
# ============================================================================================================
# test = {'foo': 'bar', 'hello': 'world'}
#
# print(list(test))
# print(list(test)[0])
# ============================================================================================================
# # My dictionary
# dict = {}
# dict['Capital'] = "London"
# dict['Food'] = "Fish&Chips"
# dict['2012'] = "Olympics"
#
# # lists
# temp = []
# dictlist = []
#
# # My attempt:
# for key, value in dict.items():
#     temp = [key, value]
#     dictlist.append(temp)
#
# print(dict)
# print(temp)
# print(dictlist)
# ============================================================================================================
# def nome_completo(nome, sobrenome):
#     return f'{nome} {sobrenome}'
#
#
# print(nome_completo('Pedro', 'Moreira'))
# ============================================================================================================
# instrutor = 'Geek'  # Variável global
#
#
# def diz_oi():
#     instrutor = 'Python'  # Variável local
#     return f'Oi {instrutor}'
#
#
# print(instrutor)
# print(diz_oi())
#
# from Estudo import diz_oi  # como importar uma def de outro arquivo
#
# print(diz_oi)
# ============================================================================================================
# import numpy as np
#
#
# def matriz():
#     m = np.arange(10)
#     return m
#
#
# def troca(m):
#     m[m > 5] = -1
#     return m
#
#
# print(matriz())
# print(troca(matriz()))
# ============================================================================================================
# import functools
#
# print(functools.reduce(lambda a, b: a + b, [3, 5, 2, 1], 20))
# ============================================================================================================
# import random
# import numpy as np
#
# while True:
#     linhas = int(input('Digite o número de linhas:'))
#     colunas = int(input('Digite o número de colunas:'))
#     if linhas <= 0 or colunas <= 0:
#         print('Digite apenas valores maiores que zero!')
#     else:
#         m = [[random.randint(0, 1) for j in range(colunas)] for i in range(linhas)]
#         print('================')
#         print(m)
#         break
#
# raio = int(input("Digite quantas espaços você quer alocar:"))
# cont = 0
# for linhas in range(len(m)):
#     for colunas in range(len(m[linhas])):
#         for r in range(raio):
#             if m[linhas][colunas + r] == 1:
#                 break
#         else:
#             for r in range(raio):
#                 m[linhas][colunas + r] = 1
#
# print('================')
#
# print(np.array(m))
# ============================================================================================================
# matriz = [[0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#
# lista = []
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         lista.append(matriz[i][j])
#
# print(lista)
# ============================================================================================================
# paises = ['Brasil', '', 'Chile', 'Argentina', '', '', 'Canadá', 'Venezuela']
#
# lista = filter(lambda pais: len(pais) > 0, paises)
# print(list(lista))
#
# print(list(filter(None, paises)))
#
# lista1 = []
# for x in paises:
#     if x != '':
#         lista1.append(x)
# print(lista1)
# ============================================================================================================
# lista = 'Pedroca'
#
# print(list(reversed(lista)))
# ============================================================================================================
# def dividir(a, b):
#     try:
#         return int(a) / int(b)
#     except (ValueError, ZeroDivisionError) as err:
#         return f'Um erro foi encontrado: {err}'
#
#
# num1 = input('Digite um número:')
# num2 = input('Digite um número:')
#
# print(dividir(num1, num2))
# ============================================================================================================

counter = 1
a = 0

if a == 0:
    print("Semáfaro verde")
elif a == 1:
    print("Semáfaro amarelo")
elif a == 2:
    print("Semáfaro vermelho")

while counter <= 10:
    counter += 1
    if a == 0:
        print("Semáfaro amarelo")
        print("Semáfaro vermelho")
        print("Semáfaro verde")
    elif a == 1:
        print("Semáfaro vermelho")
        print("Semáfaro verde")
        print("Semáfaro amarelo")
    elif a == 2:
        print("Semáfaro verde")
        print("Semáfaro amarelo")
        print("Semáfaro vermelho")
    else:
        print("Erro")
a = 1
print("Semáfaro amarelo")
