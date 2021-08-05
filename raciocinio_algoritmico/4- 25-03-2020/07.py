def restaurante():
    total = []
    maior_800 = 0
    while True:
        prato = float(input('Insira o peso do prato em gramas: '))
        if prato <= 0:
            break
        elif prato > 800:
            print('Alerta, prato maior que 800g')
            maior_800 += 1
        total.append(prato)
    media = 0
    for x in total:
        media += x / len(total)
    print(media)
    print(f'{maior_800} prato(s) maior(es) que 800g')


restaurante()
