#k) Desenvolva um programa para controlar tarefas de um projeto, onde cada
# tarefa terá um nome, data de vencimento e prioridade (alta, média, baixa).
# O programa deve permitir que o usuário cadastre ao menos 5 tarefas e altere
# a prioridade ou data de vencimento de qualquer tarefa. Após o cadastro, o
# programa deve listar todas as tarefas ordenadas pela data de vencimento e
# gerar um relatório que informe quantas tarefas possuem prioridade alta e
# quantas têm vencimento no próximo mês.
import os


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
        os.system('cls')
        tarefas_ordenadas = sorted(tarefas.items(), key=lambda x: 
            x[1]['Data de vencimento'])
        print('Lista de tarefas ordenadas por data de vencimento:')
        for nome, dados in tarefas_ordenadas:
            print(f'Tarefa: {nome}, Vencimento: {dados["Data de vencimento"]}, '
                  f'Prioridade: {dados["Prioridade"]}')
        for info_data in tarefas.values():
            dia, mes, ano = map(int, info_data['Data de vencimento'].split('/'))
            if mes < 12:
                proximo_m = mes + 1
            else:
                proximo_m = 1
            if mes < 12:
                proximo_a = ano
            else:
                proximo_a = ano + 1
                 
        prioridade_alta = sum(1 for t in tarefas.values()
                              if t['Prioridade'] == 'Alta')
        vencimento = sum(1 for i in tarefas.values()
            if int(i['Data de vencimento'].split('/')[1]) == proximo_m)

        print(f'{prioridade_alta} tarefas possuem prioridade alta')
        print(f'{vencimento} tarefas possuem vencimento no próximo mês')