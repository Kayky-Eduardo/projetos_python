import os


os.system('cls')


def Receber_lista(lista1, lista2):
    dicionario = {}
    dicionario[lista1[0]] = {'peso': lista1[1], 'idade': lista1[2]}
    dicionario[lista2[0]] = {'idade': lista2[1], 'peso': lista2[2]} 
    print(f'\nDicionário:')
    for i, j in dicionario.items():
        print(f'{i}: {j}')

    return dicionario

nome = input('Digite um nome: ')
peso = float(input('Digite o peso: '))
idade = int(input('Digite sua idade: '))

lista1 = [nome, peso, idade]
lista2 = ['john', 40, 1.8]

Receber_lista(lista1, lista2)
