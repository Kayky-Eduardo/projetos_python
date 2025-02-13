import os
from agenda import listar_compromissos

def exibir_agenda(agenda):
    os.system('cls')
    """
    Exibe todos os compromissos agendados ou apenas os compromissos
    de uma data específica
    
    :parâmetro agenda: Dicionário que armazena os compromissos
    """
    print('\nExibindo compromissos agendados')
    opcao = input('Todos os compromissos ou por data (t/d): ').lower()
    
    if opcao == 't':
        # Listar todos os compromissos
        listar_compromissos(agenda)
    elif opcao == 'd':
        # Lista compromissos de uma data específica
        data = input(
            'Digite a data dos compromissos (formato dd/mm/aaaa: '
        )
        listar_compromissos(agenda, data)
    else:
        print('\nOpção inválida! "t" para todos ou "d" para data.')