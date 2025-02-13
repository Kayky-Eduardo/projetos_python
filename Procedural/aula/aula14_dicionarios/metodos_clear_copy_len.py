import os

os.system('cls')  # Limpa a tela (funciona em sistemas Windows)

# Criação do dicionário vazio
meu_dicionario = {}

while True:
    print('-' * 70)
    print("Menu de opções:")
    print("1. Adicionar um par chave-valor ao dicionário")
    print("2. Mostrar o dicionário")
    print("3. Mostrar o tamanho do dicionário")
    print("4. Fazer uma cópia do dicionário")
    print("5. Limpar o dicionário")
    print("6. Sair")
    print('-' * 70)

    # Solicitação da escolha do usuário
    opcao = input("Escolha uma opção (1-6): ")

    if opcao == '1':
        # Adiciona um novo par chave-valor ao dicionário
        chave = input("Digite a chave: ")
        # Validação para garantir que a chave não seja vazia
        while not chave:
            print("A chave não pode ser vazia. Tente novamente.")
            chave = input("Digite a chave: ")

        valor = input("Digite o valor: ")
        # Validação para garantir que o valor não seja vazio
        while not valor:
            print("O valor não pode ser vazio. Tente novamente.")
            valor = input("Digite o valor: ")

        meu_dicionario[chave] = valor
        print(f"Par {chave}: {valor} adicionado.")
       
    elif opcao == '2':
    # Exibe o dicionário atual
        print("Dicionário atual:", meu_dicionario)

    elif opcao == '3':
        # Mostra o tamanho do dicionário usando len()
        tamanho = len(meu_dicionario)
        print(f"O dicionário tem {tamanho} elementos.")

    elif opcao == '4':
        # Cria uma cópia do dicionário usando copy() e exibe a cópia
        copia_dicionario = meu_dicionario.copy()
        print("Cópia do dicionário:", copia_dicionario)

    elif opcao == '5':
        # Limpa o dicionário usando clear()
        meu_dicionario.clear()
        print("Dicionário limpo.")

    elif opcao == '6':
        # Sai do programa
        print("Saindo do programa.")
        break
    else:
        # Mensagem para opção inválida
        print("Opção inválida. Tente novamente.")