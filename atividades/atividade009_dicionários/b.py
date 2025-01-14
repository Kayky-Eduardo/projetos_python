import os


os.system('cls')

dicio = {}
for i in range(1, 6):
    cores = input('Digite uma cor: ')
    valor = input(f'Insira um valor para a cor {cores}: ')
    dicio[cores] = valor
    os.system('cls')

while True:
    print('1. Adicionar nova cor e valor')
    print('2. Trocar valor de alguma das cores')
    print('3. Mostrar o dicionário em ordem alfabética')
    resp = input('Escolha uma opção: ').strip()
                  
    if resp == '1':
        os.system('cls')
        cor = input('Digite uma nova cor: ')
        valor = input(f'Digite um valor para a cor {cor}: ')
        dicio[cor] = valor    

    elif resp == '2':
        os.system('cls')
        print(f'Dicionário atual: {dicio}')
        escolha = input('Escolha uma das cores: ')
        
        if escolha in dicio:    
            novo_valor = input(f'Escolha um novo valor para a cor "{escolha}": ').strip()
            dicio[escolha] = novo_valor
            print(f'O valor da cor "{escolha}" foi atualizado para "{novo_valor}".')
        else:
            print(f'A cor "{escolha}" não está no dicionário.')

    elif resp == '3':
        os.system('cls')
        ord_alf = sorted(dicio)
        alf = 'abcdefghijklmnopqrstuvwxyz'

        print(f'Dicionário atual: ')
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