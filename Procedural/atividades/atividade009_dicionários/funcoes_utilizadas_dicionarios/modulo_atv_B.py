def  ordem_afabetica(dicio):
    ord_alf = sorted(dicio)
    alf = 'abcdefghijklmnopqrstuvwxyz'

    print(f'Dicionário atual:\n')
    for i, j in sorted(dicio.items()):
        print(f'{i}: {j}', end= ' | ')
    print()
    # checando quantas vezes o primeiro caractere aparece

    for char in alf:
        num = 0
        for palavra in ord_alf:
            if char in palavra[0]:
                num += 1
        if num == 0:
            continue
        else:
            print(f'{num} cor(es) começam com a letra {char}')
            print('-'*70)