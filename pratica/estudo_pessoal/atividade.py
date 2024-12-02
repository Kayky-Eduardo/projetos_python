import os


os.system('cls')

compras = []

while True:
    print('1. Adicionar')
    print('2. Remover')
    print('3. Mostrar a lista')
    resp = input('Qual opção deseja escolher: ')
    
    if resp == '1':
        qntd_ad = int(input('Quantos itens deseja adicionar: '))
        for i in range(qntd_ad):
            adicionar = input('escreva oque deseja adicionar: ').capitalize()
            compras.append(adicionar)
    elif resp == '2':
        qntd_r = int(input('Quantos itens deseja remover: '))
        for i in range(qntd_r):
            remover = input('Oque deseja remover: ').capitalize()
            if remover in compras:
                compras.remove(remover)
                print(f'Item removido')
            else:
                print(f'Item não encontrado')
    elif resp == '3':
        print(f'Lista: {compras}')