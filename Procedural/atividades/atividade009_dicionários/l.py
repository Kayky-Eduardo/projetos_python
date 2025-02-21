#Crie um programa para cadastrar filmes em um cinema. Para cada filme, o
#programa deve armazenar informações como título, gênero, duração e
#classificação indicativa. O programa deve permitir que o usuário cadastre
#pelo menos 5 filmes e possibilite alterações nas informações, caso
#necessário. Após o cadastro, o programa deve listar todos os filmes,
#ordenados por título, e gerar um relatório que indique quantos filmes têm
#duração superior a 2 horas e quantos têm classificação indicativa "Livre".
import os


os.system('cls')

cinema = {}

while True:
    print('-'*70)
    print('1. Registrar filme.')
    print('2. Alterar dado de um filme.')
    print('3. Lista de filmes no cinema.')
    print('4. relatório.')
    print('5. Sair.')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        os.system('cls')
        filme = input('Digite o nome do filme: ').capitalize()
        genero = input(f'Digite o gênero do filme {filme}: ').capitalize()
        duracao = (input(f'Digite a duração(horas:minutos:segundos) '
                         f'do filme {filme}: '))
        classificacao = input(f'Digite a classificação do '
                              f'filme(ex: Livre): ').capitalize()
        cinema[filme] = {'Gênero': genero,
                        'Duração': duracao,
                        'Classificação': classificacao}

        try:
            validacao = duracao.split(':')
            hora = int(validacao[0])
            min = int(validacao[1])
            sec = int(validacao[2])
            if filme == '' or genero == '' or classificacao == '':
                os.system('cls')
                del cinema[filme]
                print('Filme não cadastrado, devido a área(s) em branco.')
        except:
            print('A Duração não foi preenchida de forma correta, '
                  'tente novamente.')
            del cinema[filme]

    elif opcao == '2':
        if cinema:
            os.system('cls')
            print('Filmes cadastrados:')
            for i, j in cinema.items():
                print(f'{i}: {j}')
            print()
            escolher = input('Digite o nome do filme que deseja '
                             'alterar dados: ').capitalize()
            if escolher in cinema:
                os.system('cls')
                print(f'filme selecionado\n{escolher}: {cinema[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar == 'Duração':
                    nova_duracao = (input('Insira a nova duração'
                                          '(horas:minutos:segundos): '))
                    cinema[escolher]['Duração'] = nova_duracao
                    print('Duração alterada.')
                elif mudar in cinema[escolher]:
                    novo_valor = input('Insira um novo dado no lugar: ')
                    cinema[escolher][mudar] = novo_valor
                else:
                    print('Opção inválida.')
            else:
                print('filme não encontrado.')
        else:
            print('Nenhum filme cadastrado.')
    
    elif opcao == '3':
        os.system('cls')
        if cinema:
            for filme, dados in sorted(cinema.items()):
                print(f'Filme: {filme}\nGênero: {dados["Gênero"]}')
                print(f'Duração: {dados["Duração"]}')
                print(f'Classificação: {dados["Classificação"]}')
                if len(cinema) > 1:
                    print('-'*70)

    elif opcao == '4':
            os.system('cls')
            if cinema:
                cnt_duracao = 0
                class_livre = 0
                for filme, info in cinema.items():
                    comparar_duracao = int(info['Duração'].split(':')[0])
                    if comparar_duracao > 2:
                        cnt_duracao += 1
                    if info['Classificação'] == 'Livre':
                        class_livre += 1
                print(f'{cnt_duracao} filme(s) possui(em) mais '
                    'de 2hrs de duração.')
                print(f'{class_livre} filme(s) possui(em) "Livre" como '
                    'classificação')

    elif opcao == '5':
        print('Saindo...')
        break