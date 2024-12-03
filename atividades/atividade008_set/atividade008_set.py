# Trabalho sobre a estrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Kayky Eduardo
# Turma: 0392
# Ano: 2024

# o programa simula um sistema simples de gerenciamento de filmes com favoritos,
# permitindo ao usuário adicionar, remover e visualizar filmes, além de 
# visualizar os filmes que um amigo (previamente definido) assistiu.

import os

os.system('cls')

favoritos = set()

temas = ['terror', 'ação', 'suspense', 'romance', 'aventura']
terror = {'O Exorcista', 'Hereditário', 'A Bruxa', 'Corra!', 'O Iluminado'}
acao = {'Mad Max: Estrada da Fúria', 'John Wick', 'Duro de Matar',
        'O Ultimato Bourne', 'Gladiador'}
suspense = {'Os Sete Crimes Capitais', 'A Ilha do Medo',
            'O Silêncio dos Inocentes', 'Garota Exemplar', 'Prisioneiros'}
romance = {'Titanic', 'Diário de uma Paixão', 'Antes do Amanhecer',
           'La La Land', 'P.S. Eu Te Amo'}
aventura = {'O Senhor dos Anéis: A Sociedade do Anel',
            'Indiana Jones e os Caçadores da Arca Perdida', 'Jurassic Park',
            'Piratas do Caribe: A Maldição do Pérola Negra',
            'A Jornada de um Jovem Titã'}

listas_temas = [terror, acao, suspense, romance, aventura]
usuario = {'Hereditário', 'John Wick', 'Garota Exemplar', 'Titanic', 'Jurassic Park'}


print(f'Temas disponíveis: {temas}')
questao = input('Digite o seu tema favorito: ').lower()

if questao in temas:
    indice = temas.index(questao)
    filmes = listas_temas[indice]
    print(f'No tema {questao} temos {len(filmes)} filmes:')
    for filme in filmes:
        print(f'{filme}')
else:
    print('Tema não encontrado.')
    exit()

while True:
    print('='*70)
    print('1. Adicionar filmes à lista de favoritos.')
    print('2. Remover filmes da lista de favoritos.')
    print('3. Mostrar a lista de favoritos. ')
    print('4. Assistir filmes que um amigo seu(na mesma conta)'
          ' já assistiu')
    print('5. Sair.')
    print('='*70)
    
    resposta = input('Escolha uma opção: ').lower()
    if resposta == '1':
        ad = input('Digite o filme que deseja adicionar: ').strip()
        if ad in filmes:
            favoritos.add(ad)
            print(f'O filme "{ad}" foi adicionado aos seus favoritos.')
        else:
            print(f'O filme "{ad}" não foi encontrado no tema "{questao}".')

    elif resposta == '2':
        remover = input('Qual filme deseja remover: ').strip()
        if remover in favoritos:
            favoritos.remove(remover)
            print(f'O filme "{remover}" foi removido do seu favoritos.')
        else:
            print(f'O filme "{remover}" não foi encontrado' 
                  f'na sua lista de favoritos.')
            print(f'Filmes presentes na lista de favoritos: {favoritos}')
    elif resposta == '3':
        print()
        print('-'*70)
        print(f'Lista de favoritos: {favoritos}')
        print('-'*70)
    elif resposta == '4':
        print('\nFilmes que seu amigo já viu:')
        for filme in usuario:
            print(f'{filme}')
    elif resposta == '5':
        print('Saindo...')
        break
    else:
        print('Resposta inválida.')