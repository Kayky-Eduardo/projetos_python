import os
from agenda import adicionar_compromisso

def cadastrar_compromisso(agenda):
    os.system('cls')
    """
    Permite ao usuário cadastrar um compromisso na agenda
    :parâmetro agenda: Dicionário que armazena os compromissos.
    """
    print('\nCadastro de Compromisso')
    data = input("Digite a data do compromisso (formato/dd/mm/aaa): ")
    descricao = input('Digite a descrição do compromisso: ')
    
    # Adiciona o compromisso á agenda
    adicionar_compromisso(agenda, data, descricao)
    
    print(f'\nCompromisso agendado para {data}: {descricao}')