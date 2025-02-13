import os


os.system('cls')

dicionario = {}
def Receber_listas(*listas):
    for lista in listas:
        dicionario[lista[0]] = {'peso': lista[1], 'idade': lista[2]}

nome = input('Digite um nome: ')
peso = float(input('Digite o peso: '))
idade = int(input('Digite sua idade: '))

lista1 = [nome, peso, idade]
lista2 = ['john', 40, 18]

Receber_listas(lista1, lista2)

print('Dicionário:')
for i, j in dicionario.items():
    print(f'{i}: {j}')
    