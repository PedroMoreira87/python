n = int(input('Qual termo deseja encontrar da sequência Fibonacci?\n'))

if n < 1:
    print('Erro! Não deve ser menor que 1')
elif n == 1:
    print(f'O termo de posição {n} é {n} \nE a série completa é: {n}')
else:
    fibonacci = [1, 1]
    i = 0
    j = 1
    for k in range(n - 2):
        fibonacci.append(fibonacci[i] + fibonacci[j])
        i += 1
        j += 1
    print(f'O termo de posição {n} é: {fibonacci[-1]} \nE a série completa é: {fibonacci}')
