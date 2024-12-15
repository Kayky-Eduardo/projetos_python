#j) Crie um programa que gerencie eventos e Participante. O programa deve
# permitir que o usuário registre eventos, incluindo nome, data e localização,
# e associe Participante a esses eventos. Cada participante deve ter nome e
# e-mail. O programa deve permitir que o usuário insira pelo menos 3 eventos e
# associe Participante a cada evento. Após o cadastro, o programa deve exibir
# a lista de eventos com seus Participante e gerar um relatório indicando
# quantos Participante estão associados a cada evento e quantos eventos
# ocorrerão após o dia 01/01/2025.
import os
from datetime import datetime


os.system('cls')


lista_de_eventos = {}

while True:
    print('-'*70)
    print('1. Registrar evento.')
    print('2. Associar Participante a um evento.')
    print('3. Lista de eventos.')
    print('4. Relatório.')
    print('5. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        evento = input('Digite o nome do evento: ')
        data = input('Insira a data do evento(dd/mm/aaaa): ')
        local = input('Insira a localização do evento: ')
        lista_de_eventos[evento] = {'Data': data, 'Localização': local,
                                    'Participante': []}
    
    elif opcao == '2':
        qntd = int(input('Quantos Participante: '))
        novos_dados = {}
        for i in range(qntd):
            os.system('cls')
            participante = input(f'Digite o nome do {i+1}º participante: ')
            email = input('Insira o email do participante: ')
            novos_dados = {'Participante': participante,
                           'Email': email}
            associar = input('Qual evento devo associar o participante: ')
            if associar in lista_de_eventos:
                lista_de_eventos[associar]['Participante'].append(novos_dados)
            else:
                print('Evento não encontrado')
    
    elif opcao == '3':
            if lista_de_eventos:
                for evento, dados in lista_de_eventos.items():
                    print('-'*70)
                    print(f'Evento: {evento}')
                    print(f'Data: {dados["Data"]}')
                    print(f'Localização: {dados["Localização"]}')
                    print(f'Participantes:')
                    if dados['Participante']:
                        cont = 0
                        for i in dados['Participante']:
                            cont += 1
                            print(f'Nome: {i["Participante"]}, Email: {i["Email"]}')
                        print(f'{cont} participantes estão associados a este evento.')
                    else:
                        print('Nenhum participante registrado.')
            else:
                print('Nenhum evento registrado.')
    
    elif opcao == '4':
        cnt_total = 0
        cnt_apos = 0
        for evento, info_data in lista_de_eventos.items():
            data_evento = datetime.strptime(info_data['Data'], '%d/%m/%Y')
            if data_evento > datetime(2025, 1, 1):
                cnt_apos += 1
            if info_data['Participante']:
                cnt_total += len(info_data['Participante'])
        print(f'{cnt_apos} Eventos ocorrem após a data de 01/01/2025')
        print(f'{cnt_total} Participantes no total')