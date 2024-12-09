import os

meu_dicionario = {}
os.system('cls')

# Loop principal do programa
while True:
    print('-'*70)
    print("\nMenu de opções:")
    print("1. Criar dicionário com fromkeys()")
    print("2. Buscar valor de uma chave com get()")
    print("3. Sair")
    print('-'*70)

    opcao = input("Escolha uma opção (1-3): ")

    if opcao == '1':
        # Criação de um dicionário usando fromkeys()
        chaves = input("Digite as chaves separadas por vírgula: ").split(',')
        valor_padrao = input("Digite o valor padrão para as chaves: ")

        if not chaves or not valor_padrao:
            print("Erro: Chaves ou valor padrão não podem ser vazios.")
        else:
            meu_dicionario = dict.fromkeys(chaves, valor_padrao)
            print("Dicionário criado:", meu_dicionario)
    elif opcao == '2':
        # Verifica se o dicionário foi criado antes de tentar acessá-lo
        if meu_dicionario:
            print("Chaves disponíveis: ", ", ".join(meu_dicionario.keys()))
            chave = input("Digite a chave que deseja buscar: ")
            valor = meu_dicionario.get(chave, "Chave não encontrada")
            print('-'*70)
            print(f"Valor para a chave '{chave}': {valor}")
        else:
            print('-'*70)
            print("Erro! Crie um dicionário primeiro.")

    elif opcao == '3':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente!")