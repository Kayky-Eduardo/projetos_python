#k) Desenvolva um programa para controlar tarefas de um projeto, onde cada
# tarefa terá um nome, data de vencimento e prioridade (alta, média, baixa).
# O programa deve permitir que o usuário cadastre ao menos 5 tarefas e altere
# a prioridade ou data de vencimento de qualquer tarefa. Após o cadastro, o
# programa deve listar todas as tarefas ordenadas pela data de vencimento e
# gerar um relatório que informe quantas tarefas possuem prioridade alta e
# quantas têm vencimento no próximo mês.



# PROGRAMA INCOMPLETO
import os
import datetime


os.system('cls')


tarefas = {}

while True:
    print('-'*70)
    print('1. Registrar tarefa.')
    print('2. Alterar dado de uma tarefa.')
    print('3. Lista de tarefas.')
    print('4. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        nome = input('Digite o nome da tarefa: ').capitalize()
        data_vencimento = input('Digite a data de vencimento da tarefa'
                                '(dd/mm/aaaa): ')
        prioridade = input('Digite a prioridade da tarefa(alta, '
                           'média, baixa): ').capitalize()
        tarefas[nome] = {'Data de vencimento': data_vencimento,
                           'Prioridade': prioridade}
    
    elif opcao == '2':
        if tarefas:
            os.system('cls')
            print('Tarefas cadastradas:')
            for i, j in tarefas.items():
                print(f'{i}: {j}')
            print()
            escolher = input('Digite o nome da tarefa q deseja '
                             'alterar dados:').capitalize()
            if escolher in tarefas:
                print(f'tarefa selecionada {escolher}: {tarefas[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar == 'Data de vencimento':
                    nova_data = (input('Digite a Data de vencimento da tarefa'
                                       '(dd/mm/aaaa): '))
                    tarefas[escolher]['Data de vencimento'] = nova_data
                    print('Data de vencimento alterada.')
                elif mudar == 'Prioridade':
                    nova_prioridade = input('Digite a prioridade da tarefa'
                    '(alta, média, baixa)').capitalize()
                    tarefas[escolher]['Prioridade'] = nova_prioridade
                    print('Prioridade alterada.')
                else:
                    print('Classificação não encontrada.')
            else:
                print('Tarefa não encontrada.')
        else:
            print('Nenhuma tarefa cadastrada.')
    
    elif opcao == '3':
        for evento, info_data in tarefas.items():
            data_tarefa = datetime.datetime.strptime(
            info_data['Data de vencimento'], r'%d/%m/%Y')
            if data_tarefa > datetime(2025, 1, 13):
                print(f'Data de vencimento {data_tarefa} Prioridade: '
                      f'{info_data['Prioridade']}')