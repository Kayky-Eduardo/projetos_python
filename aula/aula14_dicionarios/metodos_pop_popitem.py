import os


os.system('cls')

Meu_dicionario = {}

while True:
    print('1. Adicionar um par chave-valor')
    print('2. Remover um item usando pop()')
    print('3. Remover o último item usando popitem()')
    print('4. Mostrar dicionário atual')
    print('5. Sair')

    opcao = input('Escolha uma opção (1-5): ')

    if opcao == '1':
        # Adicionar um par chave-valor ao dicionário
        chave = input('Digite a chave: ')
        Valor = input('Digite o valor: ')
        Meu_dicionario[chave] = Valor
        print(f'Par {chave}: {Valor} adicionado.')

    elif opcao == '2':
        # Remover um item específico usando pop()
        if Meu_dicionario:
            chave = input('Digite a chave do item que deseja remover: ')
            valor_removido = Meu_dicionario.pop(chave, 'Chave não encontrada')
        else:
            print('O dicionário está vazio. Adicione itens primeiros.')

    elif opcao == '3':
        # Remover o último item usando popitem()
        if Meu_dicionario:
            chave, valor = Meu_dicionario.popitem()
            print(f'Último item removido: {chave}: {valor}')
        else:
            print('O dicionário está vazio. Adicione itens primeiros.')
    
    elif opcao == '4':
        # Mostrar o dicionario atual
        if Meu_dicionario:
            print('Dicionário atual:', Meu_dicionario)
        else:
            print('O dicionário está vazio.')
    
    elif opcao == '5':
        print('Saindo do programa.')
        break
    else:
        print('Opção inválida. Tente novamente.')