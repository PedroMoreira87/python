"""l = [1, 2, 3, 4, 5]
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[0] + l[1] + l[2] + l[3] + l[4])"""

l = [1, 2, 3, 4, 5]
soma = 0
for i in range(len(l)):
    print(l[i])
    soma += l[i]
print(soma)
