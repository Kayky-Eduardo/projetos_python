#d) Desenvolva um programa que permita ao usuário cadastrar informações sobre
#5 tipos de vinho. Para cada vinho, o programa deve coletar as seguintes infor
#mações: nome do vinho, tipo(como tinto, branco, rosé, etc.), teor alcoólico
#e safra. Após o cadastro das informações, o programa deve exibir uma lista 
#detalhada com todos os vinhos cadastrados, incluindo as informações de nome,
#tipo, teor alcoólico e safra. Além disso, o programa deve permitir ao usuário
#modificar os dados de qualquer vinho previamente cadastrado. Por fim, o 
#programa deve gerar um relatório que informe quantos vinhos possuem teor
#alcoólico superior a 12% e quantos pertencem a safra superior ao ano de 2015
#além de ordenar os vinhos por nome de forma crescente e exibi-los
import os
from funcoes_utilizadas_dicionarios import modulo_atv_D


os.system('cls')

dicio = {}

while True:
    print('-'*70)
    print('1. Adicionar 5 tipos de vinho.')
    print('2. Modificar um vinho cadastrado')
    print('3. Exibir lista dos vinhos cadastrados.')
    print('4. Relatório.')
    print('5. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        for i in range(5):
            nome = input(f'Digite o nome do {i+1}º vinho: ').capitalize()
            tipo = input(f'Digite o tipo de vinho: ')
            t_alcool = float(input(f'Digite o teor alcoólico do vinho {nome}: '))
            safra = int(input(f'Digite quando foi a safra do vinho {nome}: '))
            dicio[nome] = {'Tipo': tipo,'Teor alcoólico': t_alcool, 'Safra': safra}
            print('Vinho cadastrado.')
            input('Enter para continuar')
            os.system('cls')

    if opcao == '2':
        os.system('cls')
        modulo_atv_D.mudar_dados(dicio)

    elif opcao == '3':
        os.system('cls')
        modulo_atv_D.listagem(dicio)

    elif opcao == '4':
        os.system('cls')
        modulo_atv_D.relatorio(dicio)

    elif opcao == '5':
        print('Saindo...')
        break