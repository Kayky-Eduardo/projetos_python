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

dicio = {'Martelo': 'Martelo com cabeça de metal',
         'Colher': 'Usada para para aplicar e alisar argamassa, concreto'
        'e outros materiais em alvenaria',
        'Cinta': 'Ferramente de ajuste e medição',
        'Linha': 'Ferramente de marcação',
        'Desempenadeira':'Ferramenta de acabamento'
          }


print('Dicionário atual:\n')
print('-'*70)
for ferramenta, descricao in dicio.items():
    print(f"- {ferramenta}: {descricao}")
  
print('='*70)
escolha = input('Escolha uma das ferramentas: ').capitalize()

if escolha in dicio:
    novo_sentido = input(f'Digite uma descrição para a ferramenta '
                         f'{escolha}: ')
    dicio[escolha] = novo_sentido

print('\nFerramentas armazenadas em ordem alfabética:')
for ferramenta in sorted(dicio):
  print('-'*70)
  print(f'{ferramenta}: {dicio[ferramenta]}')

print(f'\nQuantidade total de ferramentas {len(dicio)}')
