def adicionar_compromisso(agenda, data, descricao):
    """
    Adiciona um compromisso ao dicionário de compromissos.
    Se a data já existe, adiciona o compromisso á
    lista de compromissos dessa data .
    
    :parâmetro agenda: Dicionário que armazena os compromissos.
    :parâmetro data: Data do compromisso
    :parâmetro descricao: Descrição do compromisso
    """
    if data not in agenda:
        # Se não houver compromissos na data,
        # cria uma lista para armazená-los.
        agenda[data] = []
    
    # Adiciona o compromisso na data específica
    agenda[data].append(descricao)

def listar_compromissos(agenda, data=None):
    """
    Exibe todos os compromissos de uma data específica ou
    de todas as datas
    
    :parâmetro agenda: Dicionário que armazena os compromissos.
    :parâmetro data: Data dos compromissos a serem listados
    (se for None, lista todos).
    """
    
    if data:
        if data in agenda:
            print(f'\nCompromissos para {data}: ')
            for compromisso in agenda[data]:
                print(f'- {compromisso}')
        else:
            print(f'\nNenhum compromisso encontado para a data {data}.')
    else:
        if not agenda:
            print('\nNenhum compromisso agendado.')
        else:
            for data, compromissos in agenda.items():
                print(f'\nCompromissos para {data}: ')   
                for compromisso in compromissos:
                    print(f'- {compromisso}')