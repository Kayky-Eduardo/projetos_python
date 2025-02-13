import os
from cadastro import cadastrar_compromisso
from exibir import exibir_agenda

def main():
    os.system('cls')
    # Agenda será u dicionário onde a chave é a data e o
    # valor é uma lista de compromissos
    agenda = {} # inicializa a agenda vazia
    
    while True:
        print('\nAgenda de Compromissos')
        print("-"*70)
        print('1. Cadastrar compromisso')
        print('2. Exibir compromisso')
        print('3. Sair')
        
        opcao = input('Escolha uma opção (1/2/3): ')
        
        if opcao == '1':
            # Cadastrar compromisso
            cadastrar_compromisso(agenda)
        elif opcao == '2':
            # Exibir compromissos
            exibir_agenda(agenda)
        elif opcao == '3':
            # Sair do programa
            print('\nSaindo do programa...')
            break
        else:
            print('\nOpção inválida!')

# Garante que a função main() só será executada se o arqivo
# for executado diretamente
if __name__ == '__main__':
    main()