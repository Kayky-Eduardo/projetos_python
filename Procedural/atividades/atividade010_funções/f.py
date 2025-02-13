import os


os.system('cls')
from funcoes_usadas import lista_para_dicionario

lista1 = ['nome', 'peso', 'idade']
lista2 = ['john', 40, 18]

dicionario = lista_para_dicionario.Receber_listas(lista1, lista2)

print('Dicionário:')
for i, j in dicionario.items():
    print(f'{i}: {j}')