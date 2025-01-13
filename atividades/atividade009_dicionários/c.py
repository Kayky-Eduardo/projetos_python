#c) Desenvolva um programa que crie um dicionário contendo 5 ferramentas,
# onde o nome de cada ferramenta será a chave e seu respectivo valor será
# uma descrição ou especificação técnica dessa ferramenta (como tipo de uso,
# material, etc.). O programa deve permitir que o usuário altere o valor de
# qualquer ferramenta já inserida. Após a criação e possível modificação do
# dicionário, o programa deve imprimir não apenas os valores de cada
# ferramenta, mas também a quantidade total de elementos presentes no dicio-
# nário. Em seguida, o programa deve listar todas as ferramentas armazenadas,
# juntamente com suas descrições, ordenadas alfabeticamente por nome, e, por
# fim, fornecer um relatório mostrando a quantidade de ferramentas que têm
# mais de uma palavra no nome.


import os


os.system('cls')

dicio = {
  'Martelo': {'Descrição': 'Martelo com cabeça de metal',
              'Material': 'Metal e madeira'},
  'Colher': {'Descrição': 'Usada para aplicar e alisar materiais '
              'em alvenaria', 'Material': 'Aço inoxidável e madeira'},
  'Cinta': {'Descrição': 'Ferramenta de ajuste e medição',
            'Material': 'Metal e plástico'},
  'Linha': {'Descrição': 'Ferramenta de marcação',
            'Material': 'Nylon ou poliéster'},
  'Desempenadeira': {'Descrição': 'Ferramenta de acabamento',
                      'Material': 'Aço inoxidável ou plástico'}
}

print('Dicionário atual:\n')
print('-'*70)
for ferramenta, descricao in dicio.items():
    print(f"- {ferramenta}: {descricao}")
  
print('-'*70)

escolha = input('Escolha uma das ferramentas: ').capitalize()
if escolha in dicio:
    mudar = input(f'O que deseja mudar em {escolha}: ').capitalize()
    if mudar in dicio[escolha]:
      novo_sentido = input('Escreva o que deseja colocar no lugar: ')
      dicio[escolha][mudar] = novo_sentido
    else:
      print('Opção não encontrada')
else:
  print('Ferramenta não presente no dicionário')
  
print('\nFerramentas armazenadas em ordem alfabética:')
for ferramenta in sorted(dicio):
  print('-'*70)
  print(f'{ferramenta}: {dicio[ferramenta]}')

print(f'\nQuantidade total de ferramentas {len(dicio)}')
