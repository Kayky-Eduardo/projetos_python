# o) Desenvolva um programa para gerenciar os equipamentos de uma academia. O
# programa deve permitir que o usuário cadastre equipamentos, onde cada
# equipamento terá nome, tipo (musculação, cardio, etc.), quantidade e estado
# (novo, usado, necessitando reparos). O programa deve permitir que o usuário
# cadastre pelo menos 5 equipamentos e altere informações sobre a quantidade ou
# estado de qualquer equipamento. Após o cadastro, o programa deve listar todos
# os equipamentos, ordenados por tipo, e gerar um relatório que informe quantos
# equipamentos precisam de reparos e quantos estão na categoria "Cardio".
import os


os.system('cls')

equipamentos = {}

while True:
    print('-'*70)
    print('1. Registrar equipamento.')
    print('2. Alterar dado de um equipamento')
    print('3. Relatório.')
    print('4. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        nome = input('Digite o nome do equipamento: ')
        tipo = input('Insira o tipo do equipamento'
                     '(musculação, cardio, etc): ').capitalize()
        quantidade = int(input('Quantidade de equipamentos: '))
        estado = input('Qual o estado do esquipamento'
                       '(novo, usado, necessitando reparos): ').capitalize()
        equipamentos[nome] = {'Tipo': tipo,'Quantidade': quantidade,
                              'Estado': estado}
        
        equipamentos_por_tipo = {}
        for nome, dados in equipamentos.items():
            tipo = dados['Tipo']
            if tipo not in equipamentos_por_tipo:
                equipamentos_por_tipo[tipo] = []
            equipamentos_por_tipo[tipo].append((nome, dados))
        for tipo in sorted(equipamentos_por_tipo.keys()):
            print(f'\nTipo: {tipo}')
            for nome, dados in equipamentos_por_tipo[tipo]:
                print(f'Nome: {nome}, Quantidade: {dados["Quantidade"]}, Estado: {dados["Estado"]}')

    elif opcao == '2':
        continue