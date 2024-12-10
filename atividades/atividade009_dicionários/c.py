import os


os.system('cls')

dicio = {'Martelo': 'Martelo com cabeça de metal',
         'Colher': 'Usada para para aplicar e alisar argamassa, concreto'
        'e outros materiais em alvenaria',
        'Cinta': 'Ferramente de ajuste e medição',
        'Linha': 'Ferramente de marcação',
        'Desempenadeira':'Ferramenta de acabamento'
          }


print(f'Dicionário atual: {dicio}')
escolha = input('Escolha uma das ferramentas: ').capitalize

if escolha in dicio:
    del dicio[escolha]
    valor = input('Escolha um valor para a ferramenta: ')
    dicio[escolha] = valor
    print(dicio)

print(dicio.values())
print(len(dicio))
lista = list(dicio)
ordem = sorted(dicio)


