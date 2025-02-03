# o) Desenvolva um programa para gerenciar os equipamentos de uma academia. O
# programa deve permitir que o usuário cadastre equipamentos, onde cada
# equipamento terá nome, tipo (musculação, cardio, etc.), quantidade e estado
# (novo, usado, necessitando reparos). O programa deve permitir que o usuário
# cadastre pelo menos 5 equipamentos e altere informações sobre a quantidade ou
# estado de qualquer equipamento. Após o cadastro, o programa deve listar todos
# os equipamentos, ordenados por tipo, e gerar um relatório que informe quantos
# equipamentos precisam de reparos e quantos estão na categoria "Cardio".
import os


equipamentos = {}

class Equipamentos:
    def __init__(self):
        pass

    def registrar():
        nome = input('Digite o nome do equipamento: ').capitalize()
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
                print(f'Nome: {nome}, Quantidade: {dados["Quantidade"]}, '
                      f'Estado: {dados["Estado"]}')

    def alterar_dados():
        if equipamentos:
            print('Equipamentos cadastrados:')
            for i, j in sorted(equipamentos.items()):
                print(f'{i}: {j} ')
            escolher = input('Qual deseja mudar: ').capitalize()
            if escolher in equipamentos:
                os.system('cls')
                print(f'Item selecionado:\n{escolher} '
                      f'{equipamentos[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar in equipamentos[escolher]:
                    novo_valor = input('Digite o que deseja colocar '
                                       f'no lugar de {mudar}: ')
                    if mudar == 'Quantidade':
                        novo_valor = int(novo_valor)
                    equipamentos[escolher][mudar] = novo_valor
                else:
                    print('opção desconhecida')
            else:
                print('Item inexistente.')
        else:
            print('Lista de equipamentos vazia')
        
    def relatorio():
        os.system('cls')
        equipamentos_por_tipo = {}
        precisa_reparo = 0
        cardio = 0
        
        for nome, dados in equipamentos.items():
            tipo = dados['Tipo']
            if tipo not in equipamentos_por_tipo:
                equipamentos_por_tipo[tipo] = []
            equipamentos_por_tipo[tipo].append((nome, dados))
            if tipo == 'Cardio':
                cardio += 1
            if dados['Estado'] == 'Necessitando reparos':
                precisa_reparo += 1
                     
        print('Relatório:\n')
        print(f'Equipamentos necessitando de reparos: {precisa_reparo}')
        print(f'Equipamentos que estão na categoria "Cardio": {cardio}')