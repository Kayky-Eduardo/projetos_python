import os

os.system('cls')

print('-' * 70)
print('------ TABELA PERIÓDICA ------')
print('-' * 70)

# Inicialização do dicionário e da lista
elementos = {}  # Dicionário
periodica = []  # Lista

while True:
    os.system('cls')

    # Cabeçalho do menu
    print('-' * 70)
    print('MENU DE OPÇÕES:')
    print('=' * 70)
    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')
    print('-' * 70)

    # Solicitação da escolha do usuário
    opcao = input('Escolha uma opção (1-5): ')

    if opcao == '1':
        # Adicionar um elemento
        simbolo = str(input('Símbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input('\nElemento adicionado. Pressione Enter para continuar...')

    elif opcao == '2':
        # Visualizar todos os elementos
        print("\nElementos na tabela periódica:")
        print('-' * 70)
        for elemento in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.capitalize()}: {valor}')
            print('-' * 70)
        input('\nPressione Enter para continuar...')

    elif opcao == '3':
        # Atualizar um elemento
        simbolo = str(input('Digite o símbolo do elemento para atualizar: '))
        # Inicializa a flag como False
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'Digite o novo símbolo para'
                f'"{simbolo}" (ou deixe em branco para manter o atual): '))
                novo_nome = str(input(f'Digite o novo nome para'
                f' "{nome}" (ou deixe em branco para manter o atual): '))

                # Atualiza o símbolo e o nome se fornecidos
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag como True quando o elemento é encontrado
                encontrado = True
                break
        if encontrado:
            input('\nElemento atualizado. Pressione Enter para continuar...')
        else:
            input('\nElemento não encontrado. Pressione Enter para continuar...')
    
    elif opcao == '4':
        # Remover um elemento
        simbolo = str(
            input('Digite o símbolo do elemento que deseja remover: '))
        encontrado = False # Inicializa a flag como False
        for elemento in periodica:
            if elemento in periodica:
                if elemento['simbolo'] == simbolo:
                    periodica.remove(elemento)
                    # Define a flag como True quando o elemento é encontrado
                    encontrado = True
                    break
        if encontrado:
            input('\nElemento Removido. Pressione Enter para continuar...')
        else:
            input('\nElemento não encontrado. Pressione Enter para continuar...')

    elif opcao == '5':
        print('Saindo do programa.')
        break

    else:
        input('Opção inválida. Enter para tentar novamente...')