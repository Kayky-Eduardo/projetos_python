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


os.system('cls')

dicio = {}


def listagem():
    if dicio:
        for nome, info in dicio.items():
            # breve explicação para caso eu me esqueça
            # nome vai virar o dicionario q está dentro do dicionario e eu vou buscar os dados dele por info
            # poderia fazer de um jeito mais curto igual no 2 mas assim fica mais bonito
            print('-'*70)
            print(f'{nome}:\nTipo: {info["Tipo"]}\n'
                f'Teor alcoólico: {info["Teor alcoólico"]}%\n'
                f'Safra: {info["Safra"]}')
    else:
        print('Lista vazia.')    
        
def mudar_dados():
    if dicio:
        listagem()

        nome_vinho = input('\nQual vinho deseja modificar: ').capitalize()
        os.system('cls')
        if nome_vinho in dicio:
            mudar = input('Digite oque deseja modificar: ').capitalize()
            if mudar in dicio[nome_vinho]:
                novo = input('Digite o que deseja colocar no lugar: ')
                dicio[nome_vinho][mudar] = novo
                print('Mudança feita.')
            else:
                print('Classificação não encontrada.')
        else:
            print('Vinho não encontrado.')
    else:
        print('Nada cadastrado atualmente.')

def relatorio():
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
        mudar_dados()

    elif opcao == '3':
        os.system('cls')
        listagem()

    elif opcao == '4':
        relatorio()

    elif opcao == '5':
        print('Saindo...')
        break