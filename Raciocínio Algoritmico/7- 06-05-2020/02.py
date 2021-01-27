vetor = [4, 5, 2, 1]


def max_rec(vet):
    if len(vet) == 1:
        return vet[0]
    m = max_rec(vet[1:])
    if vet[0] > m:
        return vet[0]
    else:
        return m


print(max_rec(vetor))
