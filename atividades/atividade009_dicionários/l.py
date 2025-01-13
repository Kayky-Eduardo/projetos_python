# Crie um programa para cadastrar filmes em um cinema. Para cada filme, o
# programa deve armazenar informações como título, gênero, duração e
# classificação indicativa. O programa deve permitir que o usuário cadastre
# pelo menos 5 filmes e possibilite alterações nas informações, caso
# necessário. Após o cadastro, o programa deve listar todos os filmes,
# ordenados por título, e gerar um relatório que indique quantos filmes têm
# duração superior a 2 horas e quantos têm classificação indicativa "Livre".
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
        filme = input('Digite o titulo do filme: ').capitalize()
        genero = input(f'Digite o genero do filme {filme}: ').capitalize()
        duracao = (input(f'Digite a duração(horas:minutos:segundos) '
                         f'do filme {filme}: '))
        classificacao = input(f'Digite a classificação do '
                              f'filme {filme}: ').capitalize()
        cinema[filme] = {'Gênero': genero,
                        'Duração': duracao,
                        'Classificação': classificacao}
    
    elif opcao == '2':
        if cinema:
            os.system('cls')
            print('Filmes cadastrados:')
            for i, j in cinema.items():
                print(f'{i}: {j}')
            print()
            escolher = input('Digite o nome do filme que deseja '
                             'alterar dados:').capitalize()
            if escolher in cinema:
                print(f'filme selecionado {escolher}: {cinema[escolher]}')
                mudar = input('O que deseja mudar: ').capitalize()
                if mudar == 'Duração':
                    nova_duracao = (input('Insira a nova duração'
                                          '(horas:minutos:segundos): '))
                    cinema[escolher]['Duração'] = nova_duracao
                    print('Duração alterada.')
                elif mudar == 'Gênero':
                    novo_genero = input('Digite o gênero: ').capitalize()
                    cinema[escolher]['Gênero'] = novo_genero
                    print('Gênero alterado.')
                elif mudar == 'Classificação':
                    nova_class = input('Digite a nova classificação: '
                                       '').capitalize()
                    cinema[escolher]['Classificação'] = nova_class
                    print('Classificação alterada.')
                else:
                    print('Opção inválida.')
            else:
                print('filme não encontrado.')
        else:
            print('Nenhum filme cadastrado.')
    
    elif opcao == '3':
        if cinema:
            os.system('cls')
            for filme, dados in sorted(cinema.items()):
                print('='*70)
                print(f'Filme: {filme}')
                print(f'Gênero: {dados["Gênero"]}')
                print(f'Duração: {dados["Duração"]}')
                print(f'Classificação: {dados["Classificação"]}')
        else:
            print('Nenhum filme registrado.')

    elif opcao == '4':
        if cinema:
            cnt_duracao = 0
            class_livre = 0
            for filme, info in cinema.items():
                comparar_duracao = int(info['Duração'].split(':')[0])
                if comparar_duracao > 2:
                    cnt_duracao += 1
                if info['Classificação'] == 'Livre':
                    class_livre += 1
            os.system('cls')
            print(f'{cnt_duracao} filme(s) possui(em) mais '
                  'de 2hrs de duração.')
            print(f'{class_livre} filme(s) possui(em) "Livre" como '
                  'classificação como classificação')
            
    elif opcao == '5':
        print('Saindo...')
        break