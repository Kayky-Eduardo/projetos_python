# m) Desenvolva um programa que registre viagens feitas por uma empresa de
# turismo. Para cada viagem, o programa deve armazenar informações como
# destino, data de partida, duração e número de vagas disponíveis. O programa
# deve permitir que o usuário cadastre pelo menos 5 viagens e altere
# informações sobre a viagem, como a data de partida ou o número de vagas.
# Após o cadastro, o programa deve listar as viagens ordenadas por destino e
# gerar um relatório que indique quantas viagens têm menos de 10 vagas
# disponíveis e quantas ocorrem após o dia 01/06/2025.
import os


os.system('cls')

viagens = {}


while True:
    print('-'*70)
    print('1. Registrar viagem.')
    print('2. Alterar dado de uma viagem.')
    print('3. relatório.')
    print('4. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        destino = input('Digite o destino do viagem: ').capitalize()
        data_de_partida = input(f'Digite a data de partida(dd/mm/aaaa) '
                                f'da viagem {destino}: ').capitalize()
        duracao = input(f'Digite a duração(horas:minutos:segundos) '
                         f'da viagem {destino}: ')
        vagas = int(input(f'Número de vagas disponíveis: '))
        viagens[destino] = {'Data de partida': data_de_partida,
                            'Duração da viagem': duracao,
                            'Vagas disponíveis': vagas}
        if len(viagens) > 1:
            os.system('cls')
            print('Viagens cadastradas:')
            for viagem, dados in sorted(viagens.items()):
                print('='*70)
                print(f'Destino: {viagem}')
                print(f'Data de partida: {dados["Data de partida"]}')
                print(f'Duração da viagem: {dados["Duração da viagem"]}')
                print(f'Vagas disponíveis: {dados["Vagas disponíveis"]}')
        else:
            continue

    elif opcao == '2':
        if viagens:
            os.system('cls')
            print('viagens cadastradas:')
            for i, j in viagens.items():
                print(f'{i}: {j}')
            print()
            escolher = input('Digite o nome da viagem q deseja '
                             'alterar dados: ').capitalize()
            if escolher in viagens:
                os.system('cls')
                print(f'viagem selecionada {escolher}: {viagens[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar == 'Data de partida':
                    nova_data = input('Insira a nova data(dd/mm/aaaa): ')
                    viagens[escolher]['Data de partida'] = nova_data
                    print('Data de partida alterada.')
                elif mudar == 'Vagas disponíveis':
                    nova_vaga = int(input('Nova quantidade de vagas: '))
                    viagens[escolher]['Vagas disponíveis'] = nova_vaga
                    print('Número de vagas alterado.')
                else:
                    print('Classificação não encontrada.')
            else:
                print('Tarefa não encontrada.')
        else:
            print('Nenhuma tarefa cadastrada.')
        
    elif opcao == '3':
        os.system('cls')
        conta_vagas = 0
        apos_data = 0
        for info in viagens.values():
            dia, mes, ano = map(int, info['Data de partida'].split('/'))
            if ano > 2025:
                apos_data += 1
            elif ano == 2025:
                if mes >= 6:
                    if dia >= 1:
                        apos_data += 1
                else:
                    apos_data += 1
            if int(info['Vagas disponíveis']) < 10:
                conta_vagas += 1
        print(f'{conta_vagas} viagens tem menos de 10 vagas')
        print(f'{apos_data} viagens ocorrem após a data "01/06/2025"')
        
    elif opcao == '4':
        print('Saindo...')
        break