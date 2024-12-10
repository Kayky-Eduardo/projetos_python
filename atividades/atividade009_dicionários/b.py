import os


os.system('cls')

dicio = {}
for i in range(1, 6):
    cores = input('Digite uma cor: ')
    valor = input('Insira um valor para está cor: ')
    dicio[cores] = valor

while True:
    print('1. Adicionar 5 cores e valores')
    print('2. Trocar valor de alguma das cores')
    print('3. Mostrar o dicionário em ordem alfabética')
    resp = input('Escolha uma opção: ')
                  
    if resp == '1':
        novas_cores = input('Digite os pares(chave:valor) dividido por virgula: ')
        lista_novas_cores = novas_cores.split(',')
        novos_dados = {}
        for cor in lista_novas_cores:
            chave, valor = cor.split(':')
            novos_dados[chave] = valor
            dicio.update(novos_dados)

    elif resp == '2':
        print(f'Dicionário atual: {dicio}')
        escolha = input('Escolha uma das cores: ')

        if escolha in dicio:
            del dicio[escolha]
            valor = input('Escolha um valor para a cor: ')
            dicio[escolha] = valor

    elif resp == '3':
        ord_alf = sorted(dicio)
        print(f'Chaves em ordem alfabética: {ord_alf}')
        # checando quantas vezes o primeiro caractere aparece
        alf = 'abcdefghijklmnopqrstuvwxyz'

        for char in alf:
            num = 0
            for palavra in ord_alf:
                if char in palavra[0]:
                    num += 1
            if num == 0:
                continue
            else:
                print(f'{num} cor(es) começam com a letra {char}')