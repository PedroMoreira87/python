"""v = [1, 2, 3, 4]
media = (v[0] + v[1] + v[2] + v[3]) / 4
print(media)"""

v = [1, 2, 3, 4]
vm = 0
for i in v:
    vm += i / 4  # += Adiciona outro valor ao valor da variável e atribui o novo valor à variável.
print(vm)
