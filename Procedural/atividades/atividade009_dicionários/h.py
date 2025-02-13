# Programa de Cadastro de Livros: Crie um programa para cadastrar livros em
# uma biblioteca. Para cada livro, o programa deve armazenar informações como
# título, autor, ano de publicação e número de páginas. O programa deve
# permitir que o usuário cadastre pelo menos 5 livros e forneça a opção de
# alterar qualquer dado cadastrado. Após o cadastro, o programa deve exibir
# todos os livros cadastrados ordenados por título. Além disso, deve gerar um
# relatório que indique quantos livros possuem mais de 300 páginas e quantos
# são do autor "J.K. Rowling".
import os


os.system('cls')

livros_cadastrados = {}


while True:
    print('='*70)
    print('1. Cadastrar livros.')
    print('2. Alteração de dados.')
    print('3. Relatório.')
    print('4. Sair')
    print('-'*70)

    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        titulo = input('Digite o título do livro que deseja cadastrar: ')
        autor = input('Digite o nome do autor do livro: ').upper()
        num_pag = int(input('Digite o numero de páginas do livro: '))
        livros_cadastrados[titulo] = {'Autor': autor,
                                      'Número de páginas': num_pag}
        os.system('cls')
        
    elif opcao == '2':        
        print('Livros cadastrados:')
        for i, j in sorted(livros_cadastrados.items()):
            print(f'{i}: {j}')
        if livros_cadastrados:
            mudar = input('Digite o título do livro deseja modificar: ')
            if mudar in livros_cadastrados:
                os.system('cls')
                print(f'Livro selecionado: {livros_cadastrados[mudar]}')
                escolha = input('O que deseja trocar: ').capitalize()
                if escolha in livros_cadastrados[mudar]:
                    novo = input('Digite o que deseja colocar no lugar: ')
                    livros_cadastrados[mudar][escolha] = novo
                    print('Mudança feita.')
                    print('-'*70)
                    print('Livros cadastrados:\n')    
                    for livro, dados in livros_cadastrados.items():
                        print(f'Título: {livro}\nAutor: {dados["Autor"]}\n'
                        f'Número de páginas: {dados["Número de páginas"]}')
                        print('.'*70)
                else:
                    print('Classificação não encontrada.')
            else:
                print('Este livro não esta cadastrado')
        else:
            print('Não possuímos nada cadastrado.')
    
    elif opcao == '3':
        os.system('cls')
        cont_pg = 0
        cont_autor = 0
        for i, j in sorted(livros_cadastrados.items()):
            print(f'{i}: {j}')
        for dados in livros_cadastrados.values():
            if int(dados['Número de páginas']) > 300:
                cont_pg += 1
            if dados['Autor'] == 'J.K. ROWLING':
                cont_autor += 1
        print(f'{cont_pg} Livros possuem mais de 300 páginas.')
        print(f'{cont_autor} Livros tem como autor J.K. Rowling.')