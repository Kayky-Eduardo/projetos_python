import os


os.system('cls')

favoritos = set()
terror = {
    'O Exorcista (1973)',
    'Hereditário (2018)',
    'A Bruxa (2015)',
    'Corra! (2017)',
    'O Iluminado (1980)'
}
acao = {
    'Mad Max: Estrada da Fúria',
    'John Wick',
    'Duro de Matar',
    'O Ultimato Bourne',
    'Gladiador'
}
suspense = {
    'Os Sete Crimes Capitais',
    'A Ilha do Medo',
    'O Silêncio dos Inocentes',
    'Garota Exemplar',
    'Prisioneiros'
}
romance = {
    'Titanic',
    'Diário de uma Paixão',
    'Antes do Amanhecer',
    'La La Land',
    'P.S. Eu Te Amo'
}
aventura = {
    'O Senhor dos Anéis: A Sociedade do Anel',
    'Indiana Jones e os Caçadores da Arca Perdida',
    'Jurassic Park',
    'Piratas do Caribe: A Maldição do Pérola Negra',
    'A Jornada de um Jovem Titã'
}

rom = list(romance)
aven = list(aventura)
ter = list(terror)
aca = list(acao)
sus = list(suspense)

temas = [rom, aven, aca, sus, ter]
temas_mostrar = ['terror', 'ação', 'suspense', 'romance', 'aventura']

print(f'{temas_mostrar}')
questao = input('Qual dos temas citados acima '
                'é o seu favorito de filmes?\n').lower()

# Buscar o tema e se achar mostrar o que tem dentro dele
if questao in temas:
    for i in temas:
        if questao == i:
            print(f'Você escolheu o tema {i}')
            print(f'No tema {questao} temos {len(temas)} filmes: ')
else:
    print('Tema não encontrado.')
if questao in temas:
    temas.remove(questao)
    print(temas)

# Adicionar filmes aos favoritos
adicionar = input('Deseja adicionar algum filme à '
                  'sua lista de favoritos?(s/n)\n').lower()

if adicionar == 's':
    qual = input('Qual filme deseja adicionar: ')
    