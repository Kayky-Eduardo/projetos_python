#d) Desenvolva um programa que permita ao usuário cadastrar informações sobre
#5 tipos de vinho. Para cada vinho, o programa deve coletar as seguintes infor
# mações: nome do vinho, tipo (como tinto, branco, rosé, etc.), teor alcoólico
# e safra. Após o cadastro das informações, o programa deve exibir uma lista 
# detalhada com todos os vinhos cadastrados, incluindo as informações de nome,
# tipo, teor alcoólico e safra. Além disso, o programa deve permitir ao usuário
# modificar os dados de qualquer vinho previamente cadastrado. Por fim, o 
# programa deve gerar um relatório que informe quantos vinhos possuem 
# alcoólico superior a 12% e quantos pertencem a safra superior ao ano de 2015,
# além de ordenar os vinhos por nome de forma crescente e exibi-los
import os


os.system('cls')

dicio = {}

while True:
    print('-'*70)
    print('1. Adicionar 5 tipos de vinho.')
    print('2. Modificar um vinho cadastrado')
    print('3. Exibir lista dos vinhos cadastrados.')
    print('4. Mostrar o teor alcoólico.')
    print('5. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        for i in range(5):
            nome = input(f'Digite o nome do {i+1}º vinho: ').capitalize()
            tipo = input(f'Digite o tipo de vinho: ')
            t_alcool = float(input(f'Digite o ter alcoólico do vinho {nome}: '))
            safra = int(input(f'Digite quando foi a safra do vinho {nome}: '))
            dicio[nome] = {'Tipo': tipo,'Teor alcoólico': t_alcool, 'Safra': safra}
            print('Vinho cadastrado.')
            input('Enter para continuar')
            os.system('cls')

    if opcao == '2':
        if dicio:
            print(dicio)
            nome_vinho = input('Qual vinho deseja modificar: ').capitalize()
            if nome_vinho in dicio:
                mudar = input('Digite oque deseja modificar: ').lower()
                if mudar == 'tipo':
                    novo_tipo = input('Insira o novo tipo: ')
                    dicio[nome_vinho]['Tipo'] = novo_tipo
                elif mudar == 'teor alcoólico':
                    novo_teor = float(input('Insira o novo Teor alcoólico: '))
                    dicio[nome_vinho]['Teor alcoólico'] = novo_teor
                elif mudar == 'safra':
                    nova_safra = int(input('Insira uma nova safra: '))
                    dicio[nome_vinho]['Safra'] = nova_safra
                print('Mudança feita.')
            else:
                print('Vinho não encontrado.')
        else:
            print('Nada cadastrado atualmente.')
            
    elif opcao == '3':
        for nome, info in dicio.items():
            print('-'*70)
            print(f'{nome}:\nTipo: {info["Tipo"]}\n'
                  f'Teor alcoólico: {info["Teor alcoólico"]}\n'
                  f'Safra: {info["Safra"]}')
            
    elif opcao == '4':
        if dicio:
            cont_teor = 0
            cont_safra = 0
            for dados in dicio.values():
                if dados['Teor alcoólico'] > 12:
                    cont_teor += 1
                if dados['Safra'] > 2015:
                    cont_safra += 1
            print(f'Temos {cont_teor} vinhos com mais de 12% de '
                 'teor Alcoólico.')
            print(f'Temos {cont_safra} vinhos com Safra superior a de 2015. ')
            
    elif opcao == '5':
        print('Saindo...')
        break